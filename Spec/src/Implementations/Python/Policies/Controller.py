from math import log
import os
import ctypes
import numpy as np
from sklearn.preprocessing import StandardScaler


def sgd_logistic_classifier_training(state, params, spaces):
    X = [
        [1, x / log(x, params["Quai Reward Base Parameter"])]
        for x in spaces[0]["Block Difficulty"]
    ]
    Y = [x > 0 for x in spaces[0]["Qi Taken"]]

    state["Logistic Classifier"].partial_fit(X, Y, classes=[0, 1])
    betas = state["Logistic Classifier"].coef_[0]
    return [spaces[0], {"Beta": betas}]


def reward_ratio_gain(state, params, spaces):
    k_qi = state["K Qi"]
    alpha = params["Controller Alpha Parameter"]
    D = spaces[0]["Block Difficulty"]
    D = sum(D) / len(D)
    d1 = D
    d2 = log(D, params["Quai Reward Base Parameter"])
    x_d = d1 / d2
    x_b_star = -spaces[1]["Beta"][0] / spaces[1]["Beta"][1]
    k_qi += alpha * (x_d / x_b_star - 1) * k_qi
    spaces = [{"K Qi": k_qi, "K Quai": state["K Quai"]}, spaces[1]]
    return spaces


def reward_ratio_gain_kquai(state, params, spaces):
    k_quai = state["K Quai"]
    alpha = params["Controller Alpha Parameter"]
    D = spaces[0]["Block Difficulty"]
    D = sum(D) / len(D)
    d1 = D
    d2 = log(D, params["Quai Reward Base Parameter"])
    x_d = d1 / d2
    x_b_star = -spaces[1]["Beta"][0] / spaces[1]["Beta"][1]
    k_quai += alpha * (x_b_star / x_d - 1) * k_quai
    spaces = [{"K Qi": state["K Qi"], "K Quai": k_quai}, spaces[1]]
    return spaces


def mezzanine_wiring_passthrough(state, params, spaces):
    return spaces


def rolling_logistic_regression_estimation(state, params, spaces):

    scaler = StandardScaler()

    # X = [
    #    [1.0, x / log(x, params["Quai Reward Base Parameter"])]
    #    for x in spaces[0]["Block Difficulty"]
    # ]

    X = [
        [x / log(x, params["Quai Reward Base Parameter"])]
        for x in spaces[0]["Block Difficulty"]
    ]

    Y = [x > 0 for x in spaces[0]["Qi Taken"]]

    state["Logistic Classifier Queue X"].extend(X)
    state["Logistic Classifier Queue Y"].extend(Y)

    state["Logistic Classifier Queue X"] = state["Logistic Classifier Queue X"][-1000:]
    state["Logistic Classifier Queue Y"] = state["Logistic Classifier Queue Y"][-1000:]

    X_transformed = scaler.fit_transform(
        state["Logistic Classifier Queue X"], state["Logistic Classifier Queue Y"]
    )

    if len(set(state["Logistic Classifier Queue Y"])) > 1:
        state["Logistic Classifier"].fit(
            X_transformed,
            state["Logistic Classifier Queue Y"],
        )
    try:
        # transform coefficients after scaling to proper values

        scaled_beta = state["Logistic Classifier"].coef_[0][0]
        scaled_int = state["Logistic Classifier"].intercept_[0]

        beta = scaled_beta / scaler.scale_
        int = scaled_int - scaled_beta * (scaler.mean_ / scaler.scale_)

        betas = np.array([int[0], beta[0]])

    except Exception as e:
        # print(e)
        # print("Classifier did not converge, using default values of zero coefficients for beta")
        betas = np.array([-0.001, 0.001])
    return [spaces[0], {"Beta": betas}]

def logistic_regression_goquai(state, params, spaces):

    # Resolve library path
    library_name = "../logistic/logistic.so"
    library_path = os.path.abspath(library_name)

    # Check if the library exists
    if not os.path.exists(library_path):
        raise FileNotFoundError(f"Shared library not found at {library_path}")

    # Load the shared library
    logistic = ctypes.CDLL(library_path)

    # Define the Train function's argument and return types
    logistic.Train.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

    scaler = StandardScaler()

    X = [
        [x / log(x, params["Quai Reward Base Parameter"])]
        for x in spaces[0]["Block Difficulty"]
    ]

    Y = [x > 0 for x in spaces[0]["Qi Taken"]]

    state["Logistic Classifier Queue X"].extend(X)
    state["Logistic Classifier Queue Y"].extend(Y)

    state["Logistic Classifier Queue X"] = state["Logistic Classifier Queue X"][-1000:]
    state["Logistic Classifier Queue Y"] = state["Logistic Classifier Queue Y"][-1000:]

    X_transformed = scaler.fit_transform(
        state["Logistic Classifier Queue X"], state["Logistic Classifier Queue Y"]
    )

    # Initialize the betas
    b0 = 0
    b1 = 0

    if len(set(state["Logistic Classifier Queue Y"])) > 1:

        # Create sample data
        x = np.array(X_transformed, dtype=np.int32)
        y = np.array(state["Logistic Classifier Queue Y"], dtype=np.int32)
        n = len(x)

        # Call the Train function
        x_ptr = x.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
        y_ptr = y.ctypes.data_as(ctypes.POINTER(ctypes.c_int))

        b0 = ctypes.c_double()
        b1 = ctypes.c_double()

        logistic.Train(x_ptr, y_ptr, ctypes.c_int(n), ctypes.byref(b0), ctypes.byref(b1))

    try:
        # transform coefficients after scaling to proper values

        scaled_beta = b0
        scaled_int = b1

        beta = scaled_beta / scaler.scale_
        int = scaled_int - scaled_beta * (scaler.mean_ / scaler.scale_)

        betas = np.array([int[0], beta[0]])

    except Exception as e:
        # print(e)
        # print("Classifier did not converge, using default values of zero coefficients for beta")
        betas = np.array([-0.001, 0.001])

    return [spaces[0], {"Beta": betas}]