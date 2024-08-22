metrics_hash = []


metrics_hash.append(
    {
        "type": "Hash Type",
        "name": "Qi to Hash Metric",
        "description": "Metric which converts an amount of Qi to an amount of hash.",
        "variables_used": [
            ["Global State", "K Qi"],
        ],
        "parameters_used": [],
        "metrics_used": [],
        "domain": ["Qi Space"],
        "logic": r"$$qiToHash(Qi) ->  \frac{Qi}{k_{qi}}$$",
        "symbol": None,
    }
)

metrics_hash.append(
    {
        "type": "Hash Type",
        "name": "Quai to Hash Metric",
        "description": "Metric which converts and amount of Quai to an amount of hash",
        "variables_used": [["Global State", "K Quai"]],
        "parameters_used": ["Quai Reward Base Parameter"],
        "metrics_used": [],
        "domain": ["Quai Space"],
        "logic": r"$$quaiToHash(Quai) -> QuaiRewardBaseParameter^{\frac{Quai}{k_{quai}}}$$",
        "symbol": None,
    }
)
