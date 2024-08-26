block_reward_options_space = {
    "name": "Block Reward Options Space",
    "schema": {
        "Quai Reward Offered": "Quai Array Type",
        "Qi Reward Offered": "Qi Array Type",
        "Block Difficulty": "Hash Array Type",
        "Mining Time": "Delta Time Type",
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
        "Mined Blocks": "Mined Blocks Array Type",
        "New Difficulty": "Block Difficulty Type",
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

mined_blocks_space = {
    "name": "Mined Blocks Space",
    "schema": {
        "Mining Epochs": "Mining Epoch Array Type",
        "New Difficulty": "Block Difficulty Type",
    },
}

mined_blocks_space2 = {
    "name": "Mined Blocks Space 2",
    "schema": {
        "Quai Reward Offered": "Quai Array Type",
        "Qi Reward Offered": "Qi Array Type",
        "Block Difficulty": "Hash Array Type",
        "Mining Time": "Delta Time Type",
        "Quai Taken": "Quai Array Type",
        "Qi Taken": "Qi Array Type",
        "New Difficulty": "Block Difficulty Type",
        "Mining Time": "Delta Time Type",
    },
}


hash_space = {
    "name": "Hash Space",
    "schema": {
        "Hash": "Hash Type",
    },
}

block_spaces = [
    block_reward_options_space,
    block_difficulty_space,
    block_reward_space,
    mined_ratio_space,
    qi_hash_space,
    quai_hash_space,
    pre_mining_space,
    mined_blocks_space,
    hash_space,
    mined_blocks_space2,
]
