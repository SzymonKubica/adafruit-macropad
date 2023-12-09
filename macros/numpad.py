# SPDX-FileCopyrightText: 2021 Emma Humphries for Ad40ruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Numpad', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x202020, '7', ['7']),
        (0x202020, '8', ['8']),
        (0x202020, '9', ['9']),
        # 2nd row ----------
        (0x202020, '4', ['4']),
        (0x202020, '5', ['5']),
        (0x202020, '6', ['6']),
        # 3rd row ----------
        (0x202020, '1', ['1']),
        (0x202020, '2', ['2']),
        (0x202020, '3', ['3']),
        # 4th row ----------
        (0x400000, 'Backspace', [Keycode.BACKSPACE]),
        (0x202020, '0', ['0']),
        (0x004000, 'Enter', [Keycode.ENTER]),
        # Encoder button ---
        (0x000000, '', ['#'])
    ]
}
