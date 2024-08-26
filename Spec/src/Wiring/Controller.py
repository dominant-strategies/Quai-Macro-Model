controller_wiring = []

controller_wiring.append(
    {
        "name": "Controller Update Wiring",
        "components": [
            "Beta Estimation Policy",
            "Controller Update Policy",
            "Controller Mechanisms",
        ],
        "description": "The wiring for the controller actions",
        "constraints": [],
        "type": "Stack",
    }
)

controller_wiring.append(
    {
        "name": "Controller Mechanisms",
        "components": ["Set K Mechanism", "Set Estimated Beta Vector Mechanism"],
        "description": "The wiring for mechanisms for controllers",
        "constraints": [],
        "type": "Parallel",
    }
)
