# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
A macro/hotkey program for Adafruit MACROPAD. Macro setups are stored in the
/macros folder (configurable below), load up just the ones you're likely to
use. Plug into computer's USB port, use dial to select an application macro
set, press MACROPAD keys to send key sequences and other USB protocols.
"""

# pylint: disable=import-error, unused-import, too-few-public-methods
import os
import time
import math
import displayio
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad


# CONFIGURABLES ------------------------

MACRO_FOLDER = "/macros"
SCREENSAVER_START_TIME = 1 * 60 # seconds of inactivity will clear oled to avoid burn in

# CLASSES AND FUNCTIONS ----------------


class App:
    """Class representing a host-side application, for which we have a set
    of macro sequences. Project code was originally more complex and
    this was helpful, but maybe it's excessive now?"""

    last_activity_time = time.monotonic()
    in_screensaver_mode = False
    breathing_brightness = 0.1  # Initial brightness
    breathing_direction = 1  # 1 for increasing brightness, -1 for decreasing

    def __init__(self, appdata):
        self.name = appdata["name"]
        self.macros = appdata["macros"]

    def switch(self):
        """Activate application settings; update OLED labels and LED
        colors."""
        App.last_activity_time = time.monotonic()
        group[13].text = self.name  # Application name
        for i in range(12):
            if i < len(self.macros):  # Key in use, set label + LED color
                macropad.pixels[i] = self.macros[i][0]
                group[i].text = self.macros[i][1]
            else:  # Key not in use, no label or LED
                macropad.pixels[i] = 0
                group[i].text = ""
        macropad.keyboard.release_all()
        macropad.consumer_control.release()
        macropad.mouse.release_all()
        macropad.stop_tone()
        macropad.pixels.show()
        macropad.display.refresh()

        # SCREENSAVER MODE HELPERS -------------

def enter_screensaver_mode():
    macropad.display.auto_refresh = False
    macropad.display_sleep = True
    for i in range(12):
        macropad.pixels[i] = 0  # Turn off all key LEDs
    macropad.pixels.show()
    App.in_screensaver_mode = True

def wake_from_screensaver():
    App.in_screensaver_mode = False
    macropad.display_sleep = False
    macropad.display.auto_refresh = True
    apps[app_index].switch()  # Redraw the OLED and LEDs

def screensaver_breathing_effect():
    App.breathing_brightness += 0.001 * App.breathing_direction
    if App.breathing_brightness >= 1.0 or App.breathing_brightness <= 0.1:
        App.breathing_direction *= -1  # Reverse direction
    pixel_brightness = int(255 * App.breathing_brightness)
    for i in range(12):
        min_distance = 0.5
        scale:float = min_distance / get_pixel_distance_from_center(i)
        macropad.pixels[i] = (int(pixel_brightness*scale), 0, 0) # Red because it's cool
    macropad.pixels.show()


def get_pixel_distance_from_center(pixel_idx: int) -> float:
    """
    Given an index of the LED pixel under each of the keys, return its distance
    from the center of the grid. This is used to create a nice radiating breathing
    effect when running in the screen saver mode.
    """
    if pixel_idx in [0, 2, 9, 11]:
        return math.sqrt(1.5**2 + 1**2)
    if pixel_idx in [1, 10]:
        return 1.5
    if pixel_idx in [3, 5, 6, 8]:
        return math.sqrt(0.5**2 + 1**2)
    if pixel_idx in [4, 7]:
        return 0.5
    return 1



class KeyDescriptionScreen:
    def __init__(
        self, switch_name, switch_type, force, total_travel, pre_travel
    ):
        self.switch_name = switch_name
        self.switch_type = switch_type
        self.force = force
        self.total_travel = total_travel
        self.pre_travel = pre_travel

    def show_screen(self):
        group[13].text = self.switch_name
        for i in range(12):
            group[i].text = ""
        group[0].text = "Type"
        group[2].text = self.switch_type
        group[3].text = "Force"
        group[5].text = self.force
        group[6].text = "Total Travel"
        group[8].text = self.total_travel
        group[9].text = "Pre Travel"
        group[11].text = self.pre_travel
        macropad.display.refresh()


# INITIALIZATION -----------------------


macropad = MacroPad()
macropad.display.auto_refresh = False
macropad.pixels.auto_write = False

# Set up displayio group with all the labels
group = displayio.Group()
for key_index in range(12):
    x = key_index % 3
    y = key_index // 3
    group.append(
        label.Label(
            terminalio.FONT,
            text="",
            color=0xFFFFFF,
            anchored_position=(
                (macropad.display.width - 1) * x / 2,
                macropad.display.height - 1 - (3 - y) * 12,
            ),
            anchor_point=(x / 2, 1.0),
        )
    )
group.append(Rect(0, 0, macropad.display.width, 12, fill=0xFFFFFF))
group.append(
    label.Label(
        terminalio.FONT,
        text="",
        color=0x000000,
        anchored_position=(macropad.display.width // 2, -2),
        anchor_point=(0.5, -0.1),
    )
)
macropad.display.show(group)

# Load all the macro key setups from .py files in MACRO_FOLDER
apps = []
files = os.listdir(MACRO_FOLDER)
files.sort()
for filename in files:
    if filename.endswith(".py") and not filename.startswith("._"):
        try:
            module = __import__(MACRO_FOLDER + "/" + filename[:-3])
            apps.append(App(module.app))
        except (
            SyntaxError,
            ImportError,
            AttributeError,
            KeyError,
            NameError,
            IndexError,
            TypeError,
        ) as err:
            print("ERROR in", filename)
            import traceback

            traceback.print_exception(err, err, err.__traceback__)

if not apps:
    group[13].text = "NO MACRO FILES FOUND"
    macropad.display.refresh()
    while True:
        pass

last_position = 0
last_encoder_switch = macropad.encoder_switch_debounced.pressed
app_index = 0
apps[app_index].switch()


# MAIN LOOP ----------------------------

# This is needed for debouncing the encoder inputs.
last_encoder_poll_time = time.monotonic()
DEBOUNCE_DELAY = 0.5

current_app = None
last_tested_switch_name = None
while True:
    # Read encoder position. If it's changed, switch apps.
    position = macropad.encoder
    current_time = time.monotonic()
    if position != last_position :
        print(f"Last position: {last_position}, current position: {position}")
        if App.in_screensaver_mode:
            wake_from_screensaver()
        if (current_time - last_encoder_poll_time) > DEBOUNCE_DELAY:
            new_index = 0
            if int(position) > int(last_position):
                new_index = app_index + 1
            else:
                new_index = app_index - 1
            app_index = new_index % len(apps)
            current_app = apps[app_index]
            current_app.switch()
            last_encoder_poll_time = current_time
        last_position = position
        current_app_index = app_index

    # Handle encoder button. If state has changed, and if there's a
    # corresponding macro, set up variables to act on this just like
    # the keypad keys, as if it were a 13th key/macro.
    macropad.encoder_switch_debounced.update()
    encoder_switch = macropad.encoder_switch_debounced.pressed
    if encoder_switch != last_encoder_switch:
        last_encoder_switch = encoder_switch
        if len(apps[app_index].macros) < 13:
            continue  # No 13th macro, just resume main loop
        key_number = 12  # else process below as 13th macro
        pressed = encoder_switch
    else:
        event = macropad.keys.events.get()
        if not event or event.key_number >= len(apps[app_index].macros):
            if App.in_screensaver_mode:
                screensaver_breathing_effect()  # Continue breathing effect in screensaver mode
            else:
                time_since_last_activity = current_time - App.last_activity_time
                if time_since_last_activity > SCREENSAVER_START_TIME:
                    enter_screensaver_mode()
            continue  # No key events, or no corresponding macro, resume loop
        key_number = event.key_number
        pressed = event.pressed

    # If code reaches here, a key or the encoder button WAS pressed/released
    # and there IS a corresponding macro available for it...other situations
    # are avoided by 'continue' statements above which resume the loop.

    App.last_activity_time = current_time # Reset inactivity timer
    sequence = apps[app_index].macros[key_number][2]
    if pressed:
        if App.in_screensaver_mode:
            wake_from_screensaver()
            continue    # Skip this event, as it was used for screen wake up
        # 'sequence' is an arbitrary-length list, each item is one of:
        # Positive integer (e.g. Keycode.KEYPAD_MINUS): key pressed
        # Negative integer: (absolute value) key released
        # Float (e.g. 0.25): delay in seconds
        # String (e.g. "Foo"): corresponding keys pressed & released
        # List []: one or more Consumer Control codes (can also do float delay)
        # Dict {}: mouse buttons/motion (might extend in future)
        if key_number < 12:  # No pixel for encoder button
            macropad.pixels[key_number] = 0xFFFFFF
            macropad.pixels.show()
        for item in sequence:
            if isinstance(item, int):
                if item >= 0:
                    macropad.keyboard.press(item)
                else:
                    macropad.keyboard.release(-item)
            elif isinstance(item, float):
                time.sleep(item)
            elif isinstance(item, str):
                macropad.keyboard_layout.write(item)
            elif isinstance(item, list):
                for code in item:
                    if isinstance(code, int):
                        macropad.consumer_control.release()
                        macropad.consumer_control.press(code)
                    if isinstance(code, float):
                        time.sleep(code)
            elif isinstance(item, dict):
                if "buttons" in item:
                    if item["buttons"] >= 0:
                        macropad.mouse.press(item["buttons"])
                    else:
                        macropad.mouse.release(-item["buttons"])
                macropad.mouse.move(
                    item["x"] if "x" in item else 0,
                    item["y"] if "y" in item else 0,
                    item["wheel"] if "wheel" in item else 0,
                )
                if "switch_name" in item:
                    switch_name = item["switch_name"]
                    if switch_name == "reset" and current_app is not None:
                        last_tested_switch_name = None
                        current_app.switch()
                        continue
                    key_switch_description = KeyDescriptionScreen(
                        switch_name,
                        item["switch_type"],
                        item["force"],
                        item["total_travel"],
                        item["pre_travel"],
                    )
                    if switch_name != last_tested_switch_name:
                        last_tested_switch_name = switch_name
                        key_switch_description.show_screen()

                if "tone" in item:
                    if item["tone"] > 0:
                        macropad.stop_tone()
                        macropad.start_tone(item["tone"])
                    else:
                        macropad.stop_tone()
                elif "play" in item:
                    macropad.play_file(item["play"])

    else:
        # Release any still-pressed keys, consumer codes, mouse buttons
        # Keys and mouse buttons are individually released this way (rather
        # than release_all()) because pad supports multi-key rollover, e.g.
        # could have a meta key or right-mouse held down by one macro and
        # press/release keys/buttons with others. Navigate popups, etc.
        for item in sequence:
            if isinstance(item, int):
                if item >= 0:
                    macropad.keyboard.release(item)
            elif isinstance(item, dict):
                if "buttons" in item:
                    if item["buttons"] >= 0:
                        macropad.mouse.release(item["buttons"])
                elif "tone" in item:
                    macropad.stop_tone()
        macropad.consumer_control.release()
        if key_number < 12:  # No pixel for encoder button
            macropad.pixels[key_number] = apps[app_index].macros[key_number][0]
            macropad.pixels.show()
