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

block_mechanisms = [increment_block_number_mechanism, update_block_difficulty]
