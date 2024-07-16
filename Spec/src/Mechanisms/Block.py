increment_block_number_mechanism = {
    "name": "Increment Block Number Mechanism",
    "description": "A mechanism which appends the word just added and also increments the total length",
    "constraints": [],
    "logic": "",
    "domain": [],
    "parameters_used": [],
    "updates": [("Dummy", "Words", False), ("Dummy", "Total Length", False)],
}

block_mechanisms = [increment_block_number_mechanism]
