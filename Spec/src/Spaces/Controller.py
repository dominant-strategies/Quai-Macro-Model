observable_state_space = {
    "name": "Observable State Space",
    "schema": {"Historical Mined Ratio": "Mined Ratio Array Type"},
}

k_space = {
    "name": "K Space",
    "schema": {"K Quai": "Coeffecient Type", "K Qi": "Coeffecient Type"},
}

controller_spaces = [observable_state_space, k_space]
