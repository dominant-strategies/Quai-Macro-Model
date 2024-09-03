controller_parameter_set = {
    "name": "Controller Parameter Set",
    "notes": "The parameters related to the controller",
    "parameters": [
        {
            "variable_type": "PID Parameters Type",
            "name": "PID Parameterization",
            "description": "The PID parameters",
            "symbol": None,
            "domain": None,
            "parameter_class": "System",
        },
        {
            "variable_type": "Block Difficulty Type",
            "name": "Initial Block Difficulty",
            "description": "The starting block difficulty",
            "symbol": None,
            "domain": None,
            "parameter_class": "System",
        },
        {
            "variable_type": "Gain Type",
            "name": "Controller Alpha Parameter",
            "description": "The alpha parameter for tuning the adjustment speed",
            "symbol": None,
            "domain": None,
            "parameter_class": "System",
        },
        {
            "variable_type": "String Array Type",
            "name": "State Update Skipping Parameter",
            "description": "A list of state updates to turn off for debugging and testing purposes",
            "symbol": None,
            "domain": None,
            "parameter_class": "Functional",
        },
        {
            "variable_type": "Vector Array Type",
            "name": "Population Beta Signal",
            "description": "A list of population beta vectors to use in simulation",
            "symbol": None,
            "domain": None,
            "parameter_class": "Behavioral",
        },
    ],
}


controller_parameter_sets = [controller_parameter_set]
