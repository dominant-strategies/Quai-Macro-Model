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

pre_mining_space = {
    "name": "Pre-Mining Space",
    "schema": {
        "Blocks to Mine": "Block Array Type",
        "Aggregate Hashpower": "Hashpower per Second",
    },
}


block_reward_space = {
    "name": "Block Reward Space",
    "schema": {
        "Quai Reward Offered": "Quai Type",
        "Qi Reward Offered": "Qi Type",
        "Block Difficulty": "Block Difficulty Type",
        "Quai Amount": "Quai Type",
        "Qi Amount": "Qi Type",
    },
}

mined_ratio_space = {
    "name": "Mined Ratio Space",
    "schema": {"Block Number": "Block Number Type", "Ratio": "Mined Ratio Type"},
}

qi_hash_space = {
    "name": "Qi Hash Space",
    "schema": {"Block Number": "Block Number Type", "Hash Value": "Hash Type"},
}

quai_hash_space = {
    "name": "Quai Hash Space",
    "schema": {"Block Number": "Block Number Type", "Hash Value": "Hash Type"},
}


block_spaces = [
    block_reward_options_space,
    block_difficulty_space,
    block_reward_space,
    mined_ratio_space,
    qi_hash_space,
    quai_hash_space,
    pre_mining_space,
]
