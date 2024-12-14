import numpy as np

state_base = {
    "Qi Supply": 1e6,  # Set in state preperation function
    "Quai Supply": 1000000,  # Set in state preperation function
    "Locked Qi Supply": None,  # Set in state preperation function
    "Locked Quai Supply": None,  # Set in state preperation function
    "Ratio of Miners not Mining": 0.01,
    "Block Number": 0,
    "Block Difficulty": 1e7,
    "Historical Block Difficulty": [1e7],
    "Number of Regions": 2,
    "Zones per Region": 2,
    "Historical Converted Qi": [],
    "Historical Converted Quai": [],
    "Historical Mined Ratio": [],
    "Historical Qi Hash": [],
    "Historical Quai Hash": [],
    "K Qi": 2.98e-8,
    "K Quai": 0.019,
    "Quai Price": 1,
    "Qi Price": 1,
    "Simulation History Log": [],
    "Dummy": None,
    "Time": 0,
    "Delta Time": 0,
    "Quai Unlock Schedule": None,  # Set in state preperation function
    "Qi Unlock Schedule": None,  # Set in state preperation functions
    "Population Mining Beta Vector": np.array([-0.0001, 0.0001]),
    "Estimated Mining Beta Vector": [None, None],
    "Estimated Scaled Mining Beta Vector": [None, None],
    "Mu": 433000,
    "Population Mining Hashrate": 2e6,
    "Market Qi Supply Demand": 1e6,
    "Logistic Classifier": None,  # Set in state preperation functions
    "Mining Log": None,  # Set in state preperation functions
}
