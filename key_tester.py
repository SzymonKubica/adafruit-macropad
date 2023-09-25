# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Universal Numpad

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Key Tester', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
                (0x74A12E, '0', [{'key_description': 'Akko Matcha Green'}]),
        (0x4f42b5 , '1', [{'key_description': 'Akko Ocean Blue'}]),
        (0x008000, '2', [{'key_description': 'Gateron Green'}]),
        # 2nd row ----------
        (0xd30000, '3', [{'key_description': 'Gateron Red'}]),
        (0xc21e56, '4', [{'key_description': 'Akko Rose Red'}]),
        (0x8A1522, '5', [{'key_description': 'Akko Radiant Red'}]),
        # 3rd row ----------
        (0x4a3662, '6', [{'key_description': 'Akko Lavender Purple'}]),
        (0x6f5193, '7', [{'key_description': 'Akko Jelly Purple'}]),
        (0x251b31, '8', [{'key_description': 'Zealio V2'}]),
        # 4th row ----------
        (0x909090, '9', [{'key_description': 'Akko Vintage White'}]),
        (0x909090, '10', [{'key_description': 'Gateron White'}]),
        (0x9090af, '11', [{'key_description': 'Kailh Speed Silver'}]),
        # Encoder button ---
        (0x000000, '', ['#'])
    ]
}
