mining_parameter_set = {
    "name": "Mining Parameter Set",
    "notes": "The parameters related to the mining",
    "parameters": [
        {
            "variable_type": "Block Difficulty Multiples Type",
            "name": "Block Difficulty Multiples",
            "description": "The difficulty of different levels of blocks as multipliers on global difficulty",
            "symbol": None,
            "domain": None,
            "parameter_class": "System",
        },
        {
            "variable_type": "Seconds Type",
            "name": "Target Mining Time",
            "description": "The target time for mining to take",
            "symbol": None,
            "domain": None,
            "parameter_class": "System",
        },
        {
            "variable_type": "Integer Type",
            "name": "Quai Reward Base Parameter",
            "description": "The base used for Quai reward computation",
            "symbol": "B",
            "domain": None,
            "parameter_class": "System",
        },
        {
            "variable_type": "Hash Array Type",
            "name": "Aggregate Hashpower Series",
            "description": "A series of the aggregate hashpower to be used at each block number",
            "symbol": None,
            "domain": None,
            "parameter_class": "Behavioral",
        },
    ],
}


block_parameter_sets = [mining_parameter_set]
