block_reward_stateful_metric = {
    "name": "Block Reward Stateful Metrics",
    "notes": "",
    "metrics": [
        {
            "type": "Quai Type",
            "name": "Current Quai Block Reward Stateful Metric",
            "description": r"""The Quai block reward offered.
$$Quai = 2^{-(1+k_{Quai})} \cdot \log_2(d)$$

where d is the current difficulty""",
            "variables_used": [
                ("Global State", "Block Difficulty"),
                ("Global State", "K Quai"),
            ],
            "parameters_used": [],
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Qi Type",
            "name": "Current Qi Block Reward Stateful Metric",
            "description": r"""The Qi block reward offered.
$$Qi = \frac{d}{k_{Qi}}$$

where d is the current difficulty""",
            "variables_used": [
                ("Global State", "Block Difficulty"),
                ("Global State", "K Qi"),
            ],
            "parameters_used": [],
            "symbol": None,
            "domain": None,
        },
    ],
}

block_reward_stateful_metrics = [block_reward_stateful_metric]
