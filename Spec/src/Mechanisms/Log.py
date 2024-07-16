update_historical_mined_ration_mechanism = {
    "name": "Update Historical Mined Ratio Mechanism",
    "description": "A mechanism which appends the word just added and also increments the total length",
    "constraints": [],
    "logic": "",
    "domain": [],
    "parameters_used": [],
    "updates": [("Global", "Historical Mined Ratio", False)],
}

update_historical_qi_hash_mechanism = {
    "name": "Update Historical Qi Hash Mechanism",
    "description": "A mechanism which appends the word just added and also increments the total length",
    "constraints": [],
    "logic": "",
    "domain": [],
    "parameters_used": [],
    "updates": [("Global", "Historical Qi Hash", False)],
}

update_historical_quai_hash_mechanism = {
    "name": "Update Historical Quai Hash Mechanism",
    "description": "A mechanism which appends the word just added and also increments the total length",
    "constraints": [],
    "logic": "",
    "domain": [],
    "parameters_used": [],
    "updates": [("Global", "Historical Qi Hash", False)],
}

log_mechanisms = [
    update_historical_mined_ration_mechanism,
    update_historical_qi_hash_mechanism,
    update_historical_quai_hash_mechanism,
]
