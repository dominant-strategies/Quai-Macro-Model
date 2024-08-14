metrics_market = []


metrics_market.append(
    {
        "type": "Ratio Type",
        "name": "Current Block Reward Ratio Metric",
        "description": r"""$$\frac{R_{Quai}}{R_{Qi}}$$""",
        "variables_used": [["Global State", "Block Difficulty"]],
        "parameters_used": [],
        "metrics_used": [
            "Hash to Qi Metric",
            "Hash to Quai Metric",
        ],
        "domain": [],
        "logic": r"$$\frac{R_{Quai}}{R_{Qi}}$$",
        "symbol": None,
    }
)
