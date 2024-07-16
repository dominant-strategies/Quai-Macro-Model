metrics_hash = []


metrics_hash.append(
    {
        "type": "Hash Type",
        "name": "Qi to Hash Metric",
        "description": "Metric which converts an amount of Qi to an amount of hash. This may change in the future depending on parameterization.",
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

metrics_hash.append(
    {
        "type": "Hash Type",
        "name": "Quai to Hash Metric",
        "description": "Metric which converts and amount of Quai to an amount of hash",
        "variables_used": [["Global State", "K Qi"]],
        "parameters_used": [],
        "metrics_used": [
            "Current Qi Block Reward Stateful Metric",
            "Current Quai Block Reward Stateful Metric",
        ],
        "domain": ["Quai Space"],
        "logic": r"$$quaiToHash(Quai) -> \frac{R_{Qi}}{R_{Quai}} \cdot Quai \cdot k_{qi}$$",
        "symbol": None,
    }
)
