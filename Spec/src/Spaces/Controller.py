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
    "schema": {"K Quai": "Gain Type", "K Qi": "Gain Type"},
}

beta_vector_space = {
    "name": "Beta Vector Space",
    "schema": {"Beta": "Mining Beta Vector Type"},
}


controller_spaces = [observable_state_space, k_space, beta_vector_space]
