metrics_hash = []


metrics_hash.append(
    {
        "type": "Hash Type",
        "name": "Qi to Hash Metric",
        "description": "Metric which converts an amount of Qi to an amount of hash. This may change in the future depending on parameterization.",
        "variables_used": [
            ["Global State", "Block Difficulty"],
        ],
        "parameters_used": ["DUMMY Length Multiplier"],
        "metrics_used": [],
        "domain": ["Dummy Space 1"],
        "logic": "",
        "symbol": None,
    }
)

metrics_hash.append(
    {
        "type": "Hash Type",
        "name": "Quai to Hash Metric",
        "description": "Metric which converts and amount of Quai to an amount of hash",
        "variables_used": [["Dummy State", "Total Length"]],
        "parameters_used": ["DUMMY Length Multiplier"],
        "metrics_used": [],
        "domain": ["Dummy Space 1"],
        "logic": "",
        "symbol": None,
    }
)
