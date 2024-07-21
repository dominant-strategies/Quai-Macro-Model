controller_update_policy = {
    "name": "Controller Update Policy",
    "description": "The policy which determines the update to the K Values.",
    "constraints": [],
    "policy_options": [],
    "domain": [
        "Observable State Space",
    ],
    "codomain": ["K Space"],
    "parameters_used": ["PID Parameterization"],
    "metrics_used": [],
}

controller_policies = [controller_update_policy]
