market_parameter_set = {
    "name": "Market Parameter Set",
    "notes": "The parameters related to the market",
    "parameters": [
        {
            "variable_type": "Quai Type",
            "name": "Minimum Quai Conversion Amount",
            "description": "The minimum amount of Quai that can be converted",
            "symbol": None,
            "domain": None,
            "parameter_class": "System",
        },
        {
            "variable_type": "Qi Type",
            "name": "Minimum Qi Conversion Amount",
            "description": "The minimum amount of Qi that can be converted",
            "symbol": None,
            "domain": None,
            "parameter_class": "System",
        },
        {
            "variable_type": "Return Parameterization Type",
            "name": "Asset Return Parameterization",
            "description": "The parameters for determining random assets returns with correlations",
            "symbol": None,
            "domain": None,
            "parameter_class": "Behavioral",
        },
        {
            "variable_type": "Float Type",
            "name": "Price EWMA Lambda",
            "description": "The exponential decay rate for price signals",
            "symbol": None,
            "domain": None,
            "parameter_class": "Behavioral",
        },
        {
            "variable_type": "USD Array Type",
            "name": "Hashpower Cost Series",
            "description": "The cost of hashpower by block number",
            "symbol": None,
            "domain": None,
            "parameter_class": "Behavioral",
        },
        {
            "variable_type": "Float Type",
            "name": "Qi Price Movemement Sigma",
            "description": "The standard deviation of qi price movements",
            "symbol": None,
            "domain": None,
            "parameter_class": "Behavioral",
        },
        {
            "variable_type": "Float Type",
            "name": "Quai Price Movemement Sigma",
            "description": "The standard deviation of quai price movements",
            "symbol": None,
            "domain": None,
            "parameter_class": "Behavioral",
        },
    ],
}


market_parameter_sets = [market_parameter_set]
