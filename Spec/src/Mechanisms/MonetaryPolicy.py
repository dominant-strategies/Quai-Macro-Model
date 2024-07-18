mint_qi_mechanism = {
    "name": "Mint Qi Tokens Mechanism",
    "description": "A mechanism which deals with minting Qi",
    "constraints": [],
    "logic": "Update total supply by DOMAIN[0]['Qi']",
    "domain": ["Qi Space"],
    "parameters_used": [],
    "updates": [("Global", "Qi Supply", False)],
}

mint_quai_mechanism = {
    "name": "Mint Quai Tokens Mechanism",
    "description": "A mechanism which deals with minting Quai",
    "constraints": [],
    "logic": "Update total supply by DOMAIN[0]['Quai']",
    "domain": ["Quai Space"],
    "parameters_used": [],
    "updates": [("Global", "Quai Supply", False)],
}

burn_qi_mechanism = {
    "name": "Burn Qi Tokens Mechanism",
    "description": "A mechanism which deals with burning Qi",
    "constraints": [],
    "logic": "Reduce total supply by DOMAIN[0]['Qi']",
    "domain": ["Qi Space"],
    "parameters_used": [],
    "updates": [("Global", "Qi Supply", False)],
}

burn_quai_mechanism = {
    "name": "Burn Quai Tokens Mechanism",
    "description": "A mechanism which deals with burning Quai",
    "constraints": [],
    "logic": "Reduce total supply by DOMAIN[0]['Quai']",
    "domain": ["Quai Space"],
    "parameters_used": [],
    "updates": [("Global", "Quai Supply", False)],
}

monetary_policy_mechanisms = [
    mint_qi_mechanism,
    mint_quai_mechanism,
    burn_qi_mechanism,
    burn_quai_mechanism,
]
