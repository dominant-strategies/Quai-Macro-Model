circulating_stateful_metric = {
    "name": "Circulating Stateful Metrics",
    "notes": "Metrics of circulating supply",
    "metrics": [
        {
            "type": "Quai Type",
            "name": "Circulating Quai Supply",
            "description": "The total Quai supply minus the locked supply",
            "variables_used": [
                ("Global State", "Quai Supply"),
                ("Global State", "Locked Quai Supply"),
            ],
            "parameters_used": [],
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Qi Type",
            "name": "Circulating Qi Supply",
            "description": "The total Qi supply minus the locked supply",
            "variables_used": [
                ("Global State", "Qi Supply"),
                ("Global State", "Locked Qi Supply"),
            ],
            "parameters_used": [],
            "symbol": None,
            "domain": None,
        },
    ],
}

vesting_stateful_metrics = [circulating_stateful_metric]
