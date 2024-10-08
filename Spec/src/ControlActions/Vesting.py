unlock_tokens_control_action_option1 = {
    "name": "Unlock Tokens Control Action V1",
    "description": "Simple pass through to start chain of actions",
    "logic": "",
}

unlock_tokens_control_action = {
    "name": "Unlock Tokens Control Action",
    "description": "Control action that triggers unlocking of tokens. No space is passed out since with this implementation it just meant to start the policy.",
    "constraints": [],
    "control_action_options": [unlock_tokens_control_action_option1],
    "codomain": [],
    "parameters_used": [],
}

vesting_control_actions = [unlock_tokens_control_action]
