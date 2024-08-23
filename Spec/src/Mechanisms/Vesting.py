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

append_to_unlock_schedule_mechanism = {
    "name": "Append to Unlock Schedule Mechanism",
    "description": "Mechanism which appends a new unlock schedule entry",
    "constraints": [],
    "logic": "Insert the entry into the unlock schedule",
    "domain": ["Unlock Schedule Entry Space"],
    "parameters_used": [],
    "updates": [
        ("Global", "Quai Unlock Schedule", False),
        ("Global", "Qi Unlock Schedule", False),
    ],
}


vesting_mechanisms = [unlock_tokens_mechanism, append_to_unlock_schedule_mechanism]
