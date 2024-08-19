params_base = {
    "Minimum Quai Conversion Amount": 100,
    "Minimum Qi Conversion Amount": 100,
    "Asset Return Parameterization": None,
    "PID Parameterization": None,
    "Initial Block Difficulty": None,
    "Block Difficulty Multiples": {"Prime": 1, "Region": 0.5, "Zone": 0.25},
    "Target Mining Time": 2,
    "Quai Reward Base Parameter": 2,
    "Initial Vesting Schedule": [
        {
            "vesting_amount": 1000000000 * 0.3,
            "vesting_frequency": "Immediate",
            "time": 0,
            "recipient": "Foundation",
            "duration": None,
        }
    ],
    "FP Controller Update Policy": "Linear Controller Policy",
    "FP Conversions Boundary Action": "TEST Quai Conversion",
}
