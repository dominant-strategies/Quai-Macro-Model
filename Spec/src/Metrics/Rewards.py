metrics_rewards = []


metrics_rewards.append(
    {
        "type": "Qi Type",
        "name": "Hash to Qi Metric",
        "description": "Metric which converts an amount of hash to an amount of Qi.",
        "variables_used": [
            ["Global State", "K Qi"],
        ],
        "parameters_used": [],
        "metrics_used": [],
        "domain": ["Hash Space"],
        "logic": r"$$hashToQi(Hash) -> Hash \cdot k_{qi}$$",
        "symbol": None,
    }
)

metrics_rewards.append(
    {
        "type": "Quai Type",
        "name": "Hash to Quai Metric",
        "description": "Metric which converts and amount of Quai to an amount of hash",
        "variables_used": [["Global State", "K Quai"]],
        "parameters_used": ["Quai Reward Base Parameter"],
        "metrics_used": [],
        "domain": ["Hash Space"],
        "logic": r"$$hashToQuai(Hash) -> k_{quai} \cdot log_{QuaiRewardBaseParameter}(Hash)$$",
        "symbol": None,
    }
)
