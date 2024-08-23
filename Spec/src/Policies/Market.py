conversions_policy_option1 = {
    "name": "Block Reward Ratio Conversion Policy",
    "description": "The conversion ratio is defined by the ratio of the [[Current Block Reward Ratio Metric|current block reward of both Quai and Qi]].",
    "logic": """Find the locking return by looking up in the locking options parameter indexed to the locking timeframe in the space and call this r.

- If the asset is Quai, then return spaces for Quai as -TokenValue and 1/ConversionRate(...) * TokenValue * r for Qi.
- Else return Qi as -Token Value and ConversionRate(...) * TokenValue * r for Quai
    
The minting/burning tokens are this same amount as the locked token updates. Also an entry for unlock in the appropriate currency is added.""",
}

conversions_policy = {
    "name": "Conversions Policy",
    "description": "The policy which determines the amount of Quai or Qi exchanged.",
    "constraints": [
        "Quai/Qi converted must be less than total circulating",
        "Quai/Qi must be greater than the minimum amount parameters",
    ],
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
        "Qi Space",
        "Quai Space",
        "Unlock Schedule Entry Space",
    ],
    "parameters_used": [
        "Minimum Quai Conversion Amount",
        "Minimum Qi Conversion Amount",
        "Lockup Options",
    ],
    "metrics_used": ["Conversion Rate Metric"],
}

price_movements_policy_v1 = {
    "name": "Price Movements Policy V1",
    "description": "Simple policy that only checks that values > -1 for return and then computes new price",
    "logic": "For each asset, multiply the (1+return) in to get final price",
}

price_movements_policy = {
    "name": "Price Movements Policy",
    "description": "The policy for updating the prices.",
    "constraints": [],
    "policy_options": [price_movements_policy_v1],
    "domain": [
        "Price Movement Space",
    ],
    "codomain": ["Price Space"],
    "parameters_used": [],
    "metrics_used": [],
}


market_policies = [conversions_policy, price_movements_policy]
