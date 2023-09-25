# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Universal Numpad

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Key Tester', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
                (0x202000, '0', [{'key_description': 'Akko Matcha Green'}]),
        (0x202000, '1', [{'key_description': 'Akko Ocean Blue'}]),
        (0x202000, '2', [{'key_description': 'Gateron Green'}]),
        # 2nd row ----------
        (0x202000, '3', [{'key_description': 'Gateron Red'}]),
        (0x202000, '4', [{'key_description': 'Akko Rose Red'}]),
        (0x202000, '5', [{'key_description': 'Akko Radiant Red'}]),
        # 3rd row ----------
        (0x202000, '6', [{'key_description': 'Akko Lavender Purple'}]),
        (0x202000, '7', [{'key_description': 'Akko Jelly Purple'}]),
        (0x202000, '8', [{'key_description': 'Zealio V2'}]),
        # 4th row ----------
        (0xffffff, '9', [{'key_description': 'Akko Vintage White'}]),
        (0xffffff, '10', [{'key_description': 'Test'}]),
        (0xffffff, '11', [{'key_description': 'Gateron White'}]),
        # Encoder button ---
        (0x000000, '', ['#'])
    ]
}
