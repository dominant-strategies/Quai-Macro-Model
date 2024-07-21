observable_state_space = {
    "name": "Observable State Space",
    "schema": {
        "Historical Mined Ratio": "Mined Ratio Array Type",
        "Historical Quai Hash": "Hash Array Type",
        "Historical Qi Hash": "Hash Array Type",
        "Block Difficulty": "Block Difficulty Type",
        "Current Quai Block Reward": "Quai Type",
        "Current Qi Block Reward": "Qi Type",
    },
}

k_space = {
    "name": "K Space",
    "schema": {"K Quai": "Coeffecient Type", "K Qi": "Coeffecient Type"},
}

controller_spaces = [observable_state_space, k_space]
