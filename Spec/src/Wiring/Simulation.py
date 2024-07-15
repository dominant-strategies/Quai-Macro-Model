simulation_wiring = []

simulation_wiring.append(
    {
        "name": "Simulation Wiring",
        "components": [
            "Price Movements Wiring",
            "Exchanges Wiring",
            "Mine Block Wiring",
            # "Controller Update Wiring",
            # "Log Simulation Wiring",
        ],
        "description": "The wiring of the entire simulation",
        "constraints": [],
        "type": "Stack",
    }
)

simulation_wiring.append(
    {
        "name": "Log Simulation Wiring",
        "components": ["Placeholder"],
        "description": "The logging functionality for the simulation",
        "constraints": [],
        "type": "Stack",
    }
)
