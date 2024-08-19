unlock_tokens_policy_option1 = {
    "name": "Unlock Tokens Policy V1",
    "description": "Basic version of token unlocking, any values that have a time less than the current time are added to the tokens to be released count",
    "logic": "",
}

unlock_tokens_policy = {
    "name": "Unlock Tokens Policy",
    "description": "The policy for unlocking tokens.",
    "constraints": [],
    "policy_options": [unlock_tokens_policy_option1],
    "domain": [],
    "codomain": ["Unlock Tokens Space"],
    "parameters_used": [],
    "metrics_used": [],
}


vesting_policies = [unlock_tokens_policy]
