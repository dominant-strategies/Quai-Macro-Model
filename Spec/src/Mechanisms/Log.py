update_historical_mined_ration_mechanism = {
    "name": "Update Historical Mined Ratio Mechanism",
    "description": "A mechanism which appends the latest mined ratio to historical mined ratio",
    "constraints": [],
    "logic": "Append the first space to the historical array",
    "domain": ["Mined Ratio Space"],
    "parameters_used": [],
    "updates": [("Global", "Historical Mined Ratio", False)],
}

update_historical_qi_hash_mechanism = {
    "name": "Update Historical Qi Hash Mechanism",
    "description": "A mechanism which appends the latest qi has to historical qi hash",
    "constraints": [],
    "logic": "Append the first space to the historical array",
    "domain": ["Qi Hash Space"],
    "parameters_used": [],
    "updates": [("Global", "Historical Qi Hash", False)],
}

update_historical_quai_hash_mechanism = {
    "name": "Update Historical Quai Hash Mechanism",
    "description": "A mechanism which appends the latest quai hash to historical quai hash",
    "constraints": [],
    "logic": "Append the first space to the historical array",
    "domain": ["Quai Hash Space"],
    "parameters_used": [],
    "updates": [("Global", "Historical Qi Hash", False)],
}

log_mechanisms = [
    update_historical_mined_ration_mechanism,
    update_historical_qi_hash_mechanism,
    update_historical_quai_hash_mechanism,
]
