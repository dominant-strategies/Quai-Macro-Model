global_state = {
    "name": "Global State",
    "notes": "",
    "variables": [
        {
            "type": "Entity Type",
            "name": "Dummy",
            "description": "The dummy entity",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Block Number Type",
            "name": "Block Number",
            "description": "The current block that the system is on",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Block Difficulty Type",
            "name": "Block Difficulty",
            "description": "The latest difficulty for blocks",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Hash Type",
            "name": "Current Hash Difference",
            "description": "",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Conversions Array Type",
            "name": "Historical Converted Qi",
            "description": "An array of the conversions from Qi to Quai. The Qi Values will be negative in each entry and Quai values will be positive. Time is also logged in the entries of the array.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Conversions Array Type",
            "name": "Historical Converted Quai",
            "description": "An array of the conversions from Quai to Qi. The Quai Values will be negative in each entry and Qi values will be positive. Time is also logged in the entries of the array.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Mined Ratio Array Type",
            "name": "Historical Mined Ratio",
            "description": "An array of the historical ratios of mining between Qi and Quai which the miners had chosen at given times.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Hash Array Type",
            "name": "Historical Qi Hash",
            "description": "An array of the historical amount of hash attributed to Qi in block rewards with block numbers attatched to each entry.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Hash Array Type",
            "name": "Historical Quai Hash",
            "description": "An array of the historical amount of hash attributed to Quai in block rewards with block numbers attatched to each entry.",
            "symbol": None,
            "domain": None,
        },
    ],
}


"Block Number Type",
"Block Difficulty Type"  # Dimensionless comparitive measure, i.e. 10 means 10X more difficult
"Hash Type",
"Conversions Array Type"  # Qi Value, Quai Value, Time, negative for which one the user offers up for exchange that is burned
"Mined Ratio Array Type"  # Ratio, Block Number
"Hash Array Type"  # Hash amount, block number
