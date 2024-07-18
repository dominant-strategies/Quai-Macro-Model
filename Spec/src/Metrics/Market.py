metrics_market = []


metrics_market.append(
    {
        "type": "Ratio Type",
        "name": "Current Block Reward Ratio Metric",
        "description": r"""$$\frac{R_{Quai}}{R_{Qi}}$$""",
        "variables_used": [],
        "parameters_used": [],
        "metrics_used": [
            "Current Qi Block Reward Stateful Metric",
            "Current Quai Block Reward Stateful Metric",
        ],
        "domain": [],
        "logic": r"$$\frac{R_{Quai}}{R_{Qi}}$$",
        "symbol": None,
    }
)
