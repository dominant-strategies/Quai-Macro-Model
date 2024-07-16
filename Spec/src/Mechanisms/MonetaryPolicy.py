mint_qi_mechanism = {
    "name": "Mint Qi Tokens Mechanism",
    "description": "A mechanism which appends the word just added and also increments the total length",
    "constraints": [],
    "logic": "",
    "domain": [],
    "parameters_used": [],
    "updates": [("Dummy", "Words", False), ("Dummy", "Total Length", False)],
}

mint_quai_mechanism = {
    "name": "Mint Quai Tokens Mechanism",
    "description": "A mechanism which appends the word just added and also increments the total length",
    "constraints": [],
    "logic": "",
    "domain": [],
    "parameters_used": [],
    "updates": [("Dummy", "Words", False), ("Dummy", "Total Length", False)],
}

monetary_policy_mechanisms = [mint_qi_mechanism, mint_quai_mechanism]
