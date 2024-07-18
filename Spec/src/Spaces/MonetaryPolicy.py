quai_space = {
    "name": "Quai Space",
    "schema": {
        "Quai": "Quai Type",
    },
}

qi_space = {
    "name": "Qi Space",
    "schema": {"Qi": "Qi Type"},
}

conversion_space = {
    "name": "Conversion Space",
    "schema": {"Token": "Token Name Type", "Amount": "Token Amount Type"},
}

conversion_log_space = {
    "name": "Conversion Log Space",
    "schema": {
        "Qi Value": "Qi Type",
        "Quai Value": "Quai Type",
        "Time": "Datetime Type",
    },
}


monetary_policy_spaces = [quai_space, qi_space, conversion_space, conversion_log_space]
