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

update_prices_mechanism = {
    "name": "Update Prices Mechanism",
    "description": "Mechanism for updating prices",
    "constraints": [],
    "logic": "Set the values",
    "domain": ["Price Space"],
    "parameters_used": [],
    "updates": [("Global", "Quai Price", False), ("Global", "Qi Price", False)],
}

update_locked_qi_mechanism = {
    "name": "Update Locked Qi Mechanism",
    "description": "Mechanism for updating the locked Qi amount",
    "constraints": [],
    "logic": "Add the domain to the value",
    "domain": ["Qi Space"],
    "parameters_used": [],
    "updates": [("Global", "Locked Qi Supply", False)],
}


update_locked_quai_mechanism = {
    "name": "Update Locked Quai Mechanism",
    "description": "Mechanism for updating prices",
    "constraints": [],
    "logic": "Add the domain to the value",
    "domain": ["Quai Space"],
    "parameters_used": [],
    "updates": [("Global", "Locked Qi Supply", False)],
}


monetary_policy_mechanisms = [
    mint_qi_mechanism,
    mint_quai_mechanism,
    burn_qi_mechanism,
    burn_quai_mechanism,
    update_prices_mechanism,
    update_locked_qi_mechanism,
    update_locked_quai_mechanism,
]
