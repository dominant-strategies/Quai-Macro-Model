block_reward_options_space = {
    "name": "Block Reward Options Space",
    "schema": {
        "Quai Reward Offered": "Quai Type",
        "Qi Reward Offered": "Qi Type",
        "Block Difficulty": "Block Difficulty Type",
    },
}

block_difficulty_space = {
    "name": "Block Difficulty Space",
    "schema": {"Block Difficulty": "Block Difficulty Type"},
}


block_spaces = [block_reward_options_space, block_difficulty_space]
