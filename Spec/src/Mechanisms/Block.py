increment_block_number_mechanism = {
    "name": "Increment Block Number Mechanism",
    "description": "A mechanism which increments the current block number",
    "constraints": [],
    "logic": "Add 1 to the current block number",
    "domain": [],
    "parameters_used": [],
    "updates": [("Global", "Block Number", False)],
}

block_mechanisms = [increment_block_number_mechanism]
