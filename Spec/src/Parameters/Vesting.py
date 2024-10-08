vesting_parameter_set = {
    "name": "Vesting Parameter Set",
    "notes": "The parameters for vesting in the system",
    "parameters": [
        {
            "variable_type": "Vesting Schedule Type",
            "name": "Initial Vesting Schedule",
            "description": "The vesting schedule for initial allocations",
            "symbol": None,
            "domain": None,
            "parameter_class": "System",
        },
        {
            "variable_type": "Lockup Table Type",
            "name": "Lockup Options",
            "description": "The options for locking up for different time frames",
            "symbol": None,
            "domain": None,
            "parameter_class": "System",
        },
    ],
}


vesting_parameter_sets = [vesting_parameter_set]
