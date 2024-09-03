user_population_beta_policy_option1 = {
    "name": "Update Population Beta Policy Passthrough",
    "description": "Simple passthrough policy",
    "logic": "Check constraints and if all pass then pass the space along",
}

user_population_beta_policy = {
    "name": "Update Population Beta Policy",
    "description": "Policy for making any revisions or changes to population beta.",
    "constraints": ["Beta0 < 0 and Beta1 > 0"],
    "policy_options": [user_population_beta_policy_option1],
    "domain": ["Beta Vector Space"],
    "codomain": ["Beta Vector Space"],
    "parameters_used": [],
    "metrics_used": [],
}


user_policies = [user_population_beta_policy]
