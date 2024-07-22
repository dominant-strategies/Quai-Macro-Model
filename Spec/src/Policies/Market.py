conversions_policy_option1 = {
    "name": "Block Reward Ratio Conversion Policy",
    "description": "The conversion ratio is defined by the ratio of the [[Current Block Reward Ratio Metric|current block reward of both Quai and Qi]].",
    "logic": """If the asset is Quai, then return spaces for Quai as -TokenValue and 1/[[Current Block Reward Ratio Metric]] * TokenValue for Qi.
    Else return Qi as -Token Value and [[Current Block Reward Ratio Metric]] * TokenValue for Quai""",
}

conversions_policy = {
    "name": "Conversions Policy",
    "description": "The policy which determines the amount of Quai or Qi exchanged.",
    "constraints": [],
    "policy_options": [conversions_policy_option1],
    "domain": [
        "Conversion Space",
    ],
    "codomain": [
        "Qi Space",
        "Quai Space",
        "Qi Space",
        "Quai Space",
        "Conversion Log Space",
        "Conversion Log Space",
    ],
    "parameters_used": [
        "Minimum Quai Conversion Amount",
        "Minimum Qi Conversion Amount",
    ],
    "metrics_used": ["Current Block Reward Ratio Metric"],
}

price_movements_policy = {
    "name": "Price Movements Policy",
    "description": "The policy for updating the prices.",
    "constraints": [],
    "policy_options": [],
    "domain": [
        "Price Movement Space",
    ],
    "codomain": ["Price Space"],
    "parameters_used": [],
    "metrics_used": [],
}


market_policies = [conversions_policy, price_movements_policy]
