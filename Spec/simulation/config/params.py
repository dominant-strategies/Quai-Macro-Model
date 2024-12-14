import numpy as np
from copy import deepcopy

initial_vesting_allocation = 5000000000

params_base = {
    "Minimum Quai Conversion Amount": 0,
    "Minimum Qi Conversion Amount": 0,
    "Asset Return Parameterization": None,
    "PID Parameterization": None,
    "Initial Block Difficulty": None,
    "Block Difficulty Multiples": None,
    "Target Mining Time": 5,
    "Quai Reward Base Parameter": 2,
    "Initial Vesting Schedule": [
        {
            "vesting_amount": initial_vesting_allocation / 3 * 0.3,
            "vesting_frequency": "Immediate",
            "time": 0,
            "recipient": "Foundation",
            "duration": None,
        },
        {
            "vesting_amount": initial_vesting_allocation / 3 * 0.7,
            "vesting_frequency": "Monthly",
            "time": 0,
            "recipient": "Foundation",
            "duration": 6,
        },
        {
            "vesting_amount": initial_vesting_allocation * 7 / 30,
            "vesting_frequency": "Monthly",
            "time": 0,
            "recipient": "Community Incentives",
            "duration": 4,
        },
        {
            "vesting_amount": initial_vesting_allocation * 0.2 * 0.25,
            "vesting_frequency": "Immediate",
            "time": 0,
            "recipient": "Investors",
            "duration": None,
        },
        {
            "vesting_amount": initial_vesting_allocation * 0.2 * 0.75,
            "vesting_frequency": "Monthly",
            "time": 0,
            "recipient": "Investors",
            "duration": 3,
        },
        {
            "vesting_amount": initial_vesting_allocation * 49 / 3 / 100 * 0.25,
            "vesting_frequency": "Immediate",
            "time": 1,
            "recipient": "Founders & Team",
            "duration": None,
        },
        {
            "vesting_amount": initial_vesting_allocation * 49 / 3 / 100 * 0.75,
            "vesting_frequency": "Monthly",
            "time": 1,
            "recipient": "Founders & Team",
            "duration": 3,
        },
        {
            "vesting_amount": initial_vesting_allocation * 0.02,
            "vesting_frequency": "Immediate",
            "time": 0,
            "recipient": "Exchanges & MMs",
            "duration": None,
        },
        {
            "vesting_amount": initial_vesting_allocation * 11 / 3 / 100,
            "vesting_frequency": "Immediate",
            "time": 0,
            "recipient": "Testnet",
            "duration": None,
        },
        {
            "vesting_amount": initial_vesting_allocation * 4 / 3 / 100 * 0.25,
            "vesting_frequency": "Immediate",
            "time": 0,
            "recipient": "Earn Program",
            "duration": None,
        },
        {
            "vesting_amount": initial_vesting_allocation * 4 / 3 / 100 * 0.75,
            "vesting_frequency": "Monthly",
            "time": 0,
            "recipient": "Earn Program",
            "duration": 2,
        },
    ],
    "Aggregate Hashpower Series": [2.5e8 for _ in range(1, 10002)],
    "Difficulty Adjustment Period": 700 / 16,  # Adjusting prime blocks into zone blocks
    "Price EWMA Lambda": 0.1,
    "Hashpower Cost Series": [2.8e-8 for x in range(1, 10002)],
    "Hashpower Cost Series Sigma": 2.8e-10,
    "Qi Price Movemement Sigma": 0.01,
    "Quai Price Movemement Sigma": 0.01,
    "Lockup Options": {
        0: {2 / 52: 1, 3 / 12: 1.035, 6 / 12: 1.1, 1: 1.25},
        1: {2 / 52: 1, 3 / 12: 1.035, 6 / 12: 1.1, 1: 1.25},
        2: {2 / 52: 1, 3 / 12: 1.0175, 6 / 12: 1.05, 1: 1.15},
        3: {2 / 52: 1, 3 / 12: 1.00875, 6 / 12: 1.025, 1: 1.0625},
        4: {2 / 52: 1, 3 / 12: 1.004375, 6 / 12: 1.0125, 1: 1.03125},
        5: {2 / 52: 1, 3 / 12: 1.002188, 6 / 12: 1.00625, 1: 1.015625},
    },
    "Speculator Percentage": 0.01,
    "Conversion Percentage Mu": 0.01,
    "Conversion Percentage Sigma": 0.001,
    "Controller Alpha Parameter": 0.05,
    "Difficulty Randomness Sigma": 0.2,
    "Difficulty Randomness Mu": 1,
    "Speculator Rationality Ratio": 0.5,
    "State Update Skipping Parameter": [],
    "Population Beta Signal": [np.array([-300000, 0.5])] * 10000,
    "Minimum K Qi": 0,
    "Minimum K Quai": 0,
    "Maximum Conversion Rate": 1000,
    "Probability of Rational Miners": 0.8,
    "FP Controller Update Policy": "Reward Ratio Gain KQuai",
    "FP Conversions Boundary Action": "Conversions Boundary Action V1",
    "FP Mine Block Boundary Action": "Mine Block Boundary Action V3",
    "FP Price Movements Boundary Action": "Hashpower Price Movement",
    "FP Mining Payment Policy": "Deterministic Mining Payment Policy",
    "FP Beta Estimation Policy": "Rolling Logistic Regression Estimation",
}

params_goquai_test = deepcopy(params_base)
params_goquai_test["FP Beta Estimation Policy"] = "Go-Quai implementation of the logistic regression"

params_fixed_beta = deepcopy(params_base)
params_fixed_beta["FP Beta Estimation Policy"] = "Fixed B1 logistic Regression"

params_sample_estimation = deepcopy(params_base)
params_sample_estimation["FP Beta Estimation Policy"] = "Sample Estimation of Betas"
