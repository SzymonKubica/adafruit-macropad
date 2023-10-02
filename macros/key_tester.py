# SPDX-FileCopyrightText: 2023 Szymon Kubica
#
# SPDX-License-Identifier: MIT

app = {  # REQUIRED dict, must be named 'app'
    "name": "Switch Tester",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (
            0x34710E,
            "",
            [
                {
                    "switch_name": "Akko Matcha Green",
                    "switch_type": "Linear",
                    "force": "50g",
                    "total_travel": "4.0mm",
                    "pre_travel": "1.9mm",
                }
            ],
        ),
        (
            0x0F0275,
            "",
            [
                {
                    "switch_name": "Akko Ocean Blue",
                    "switch_type": "Tactile",
                    "force": "36g / 45g",
                    "total_travel": "4.0mm",
                    "pre_travel": "1.9mm",
                }
            ],
        ),
        (
            0x004000,
            "",
            [
                {
                    "switch_name": "Gateron Green",
                    "switch_type": "Clicky",
                    "force": "65g / 80g",
                    "total_travel": "4.0mm",
                    "pre_travel": "2.3mm",
                }
            ],
        ),
        # 2nd row ----------
        (
            0x7A0202,
            "",
            [
                {
                    "switch_name": "Gateron Red",
                    "switch_type": "Linear",
                    "force": "45g",
                    "total_travel": "4.0mm",
                    "pre_travel": "2.0mm",
                }
            ],
        ),
        (
            0x920F16,
            "",
            [
                {
                    "switch_name": "Akko Rose Red",
                    "switch_type": "Linear",
                    "force": "45g",
                    "total_travel": "4.0mm",
                    "pre_travel": "2.0mm",
                }
            ],
        ),
        (
            0xA30000,
            "",
            [
                {
                    "switch_name": "Akko Radiant Red",
                    "switch_type": "Linear",
                    "force": "53g",
                    "total_travel": "3.5mm",
                    "pre_travel": "1.9mm",
                }
            ],
        ),
        # 3rd row ----------
        (
            0x0A0622,
            "",
            [
                {
                    "switch_name": "Akko Lavender Purple",
                    "switch_type": "Tactile",
                    "force": "36g / 50g",
                    "total_travel": "4.0mm",
                    "pre_travel": "1.9mm",
                }
            ],
        ),
        (
            0x2F1153,
            "",
            [
                {
                    "switch_name": "Akko Jelly Purple",
                    "switch_type": "Tactile",
                    "force": "40g / 56g",
                    "total_travel": "4.0mm",
                    "pre_travel": "2.0mm",
                }
            ],
        ),
        (
            0x150B21,
            "",
            [
                {
                    "switch_name": "Zealio V2",
                    "switch_type": "Tactile",
                    "force": "62g",
                    "total_travel": "4.0mm",
                    "pre_travel": "2.6mm",
                }
            ],
        ),
        # 4th row ----------
        (
            0x505050,
            "",
            [
                {
                    "switch_name": "Akko Vintage White",
                    "switch_type": "Linear",
                    "force": "35g",
                    "total_travel": "4.0mm",
                    "pre_travel": "1.9mm",
                }
            ],
        ),
        (
            0x505050,
            "",
            [
                {
                    "switch_name": "Gateron Clear",
                    "switch_type": "Linear",
                    "force": "35g",
                    "total_travel": "4.0mm",
                    "pre_travel": "2.0mm",
                }
            ],
        ),
        (
            0x50507F,
            "",
            [
                {
                    "switch_name": "Kailh Speed Silver",
                    "switch_type": "Linear",
                    "force": "40g",
                    "total_travel": "3.5mm",
                    "pre_travel": "1.1mm",
                }
            ],
        ),
        # Encoder button ---
        (0x000000, "", [{"switch_name": "reset"}]),
    ],
}
