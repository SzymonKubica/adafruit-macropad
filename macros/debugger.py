# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Consumer Control codes (media keys)

# The syntax for Consumer Control macros is a little peculiar, in order to
# maintain backward compatibility with the original keycode-only macro files.
# The third item for each macro is a list in brackets, and each value within
# is normally an integer (Keycode), float (delay) or string (typed literally).
# Consumer Control codes are distinguished by enclosing them in a list within
# the list, which is why you'll see double brackets [[ ]] below.
# Like Keycodes, Consumer Control codes can be positive (press) or negative
# (release), and float values can be inserted for pauses.

# To reference Consumer Control codes, import ConsumerControlCode like so...
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode
# You can still import Keycode as well if a macro file mixes types!
# See other macro files for typical Keycode examples.

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'GDB Keybindings', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x002000, 'Break', []),
        (0x002000, 'F8', [Keycode.F8]),
        (0x002000, 'Toggle', [Keycode.F8]),
        # 2nd row ----------
        (0x000000, '', []),
        (0x000020, 'F5', [Keycode.F5]),
        (0x202020, 'Continue', [Keycode.F5]),
        # 3rd row ----------
        (0x000000, '', []),
        (0x000020, 'F10', [Keycode.F10]),
        (0x202020, 'Next', [Keycode.F10]),
        # 4th row ----------
        (0x000000, '', []),
        (0x000020, 'F11', [Keycode.F11]),
        (0x202020, 'Step', [Keycode.F11]),
        # Encoder button ---
        (0x000000, '', [Keycode.ESCAPE])
    ]
}
