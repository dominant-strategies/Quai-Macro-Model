unlock_tokens_mechanism = {
    "name": "Unlock Tokens Mechanism",
    "description": "Mechanism which takes care of unlocking of tokens",
    "constraints": [],
    "logic": "Reduce the locked tokens by the domain inputs and set the unlock schedule to the domain input",
    "domain": ["Unlock Tokens Space"],
    "parameters_used": [],
    "updates": [
        ("Global", "Locked Quai Supply", False),
        ("Global", "Locked Qi Supply", False),
        ("Global", "Quai Unlock Schedule", False),
        ("Global", "Qi Unlock Schedule", False),
    ],
}

vesting_mechanisms = [unlock_tokens_mechanism]
