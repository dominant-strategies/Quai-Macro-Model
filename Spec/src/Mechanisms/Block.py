increment_block_number_mechanism = {
    "name": "Increment Block Number Mechanism",
    "description": "A mechanism which increments the current block number",
    "constraints": [],
    "logic": "Add 1 to the current block number",
    "domain": [],
    "parameters_used": [],
    "updates": [("Global", "Block Number", False)],
}

update_block_difficulty = {
    "name": "Update Block Difficulty Mechanism",
    "description": "A mechanism which slowly updates the difficulty over an adjustment period.",
    "constraints": [],
    "logic": "(CurrentDifficulty * (Period-1) + NewDifficulty) / Period",
    "domain": ["Block Difficulty Space"],
    "parameters_used": ["Difficulty Adjustment Period"],
    "updates": [("Global", "Block Difficulty", False)],
}

increment_time_mechanism = {
    "name": "Increment Time Mechanism",
    "description": "Mechanism for moving forward the simulation clock",
    "constraints": [],
    "logic": "Adds time",
    "domain": ["Mined Blocks Space 2"],
    "parameters_used": [],
    "updates": [("Global", "Time", False)],
}

log_mined_blocks_mechanism = {
    "name": "Log Mined Blocks Mechanism",
    "description": "Mechanism for logging of blocks that were mined",
    "constraints": [],
    "logic": "Append the space to the ",
    "domain": ["Mined Blocks Space 2"],
    "parameters_used": [],
    "updates": [("Global", "Mining Log", False)],
}

block_mechanisms = [
    increment_block_number_mechanism,
    update_block_difficulty,
    increment_time_mechanism,
    log_mined_blocks_mechanism,
]
