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
        "domain": ["Qi Space"],
        "logic": r"$$qiToHash(Qi) ->  Qi \cdot k_{qi}$$",
        "symbol": None,
    }
)

metrics_rewards.append(
    {
        "type": "Quai Type",
        "name": "Hash to Quai Metric",
        "description": "Metric which converts and amount of Quai to an amount of hash",
        "variables_used": [["Global State", "K Qi"]],
        "parameters_used": [],
        "metrics_used": [],
        "domain": ["Quai Space"],
        "logic": r"$$quaiToHash(Quai) -> \frac{R_{Qi}}{R_{Quai}} \cdot Quai \cdot k_{qi}$$",
        "symbol": None,
    }
)
