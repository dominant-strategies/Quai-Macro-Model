from math import log
import os
import ctypes
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


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

    state["Logistic Classifier Queue X"] = state["Logistic Classifier Queue X"][-100:]
    state["Logistic Classifier Queue Y"] = state["Logistic Classifier Queue Y"][-100:]

    X_transformed = scaler.fit_transform(
        state["Logistic Classifier Queue X"], state["Logistic Classifier Queue Y"]
    )

    prev_beta0 = -2e2
    if state["Estimated Scaled Mining Beta Vector"][0] is not None:
        prev_beta0 = state["Estimated Scaled Mining Beta Vector"][0]


    if len(set(state["Logistic Classifier Queue Y"])) > 1:
        state["Logistic Classifier"].fit(
            prev_beta0,
            X_transformed,
            state["Logistic Classifier Queue Y"],
        )
    try:
        # transform coefficients after scaling to proper values

        scaled_beta = state["Logistic Classifier"].coef_[0][0]
        scaled_int = state["Logistic Classifier"].intercept_[0]

        scaled_betas = np.array([scaled_int, scaled_beta])

        beta = scaled_beta / scaler.scale_
        int = scaled_int - scaled_beta * (scaler.mean_ / scaler.scale_)

        betas = np.array([int[0], beta[0]])

    except Exception as e:
        # print(e)
        # print("Classifier did not converge, using default values of zero coefficients for beta")
        betas = np.array([-0.001, 0.001])
        scaled_betas = np.array([-0.001, 0.001])

    return [spaces[0], {"Beta": betas, "Scaled Beta": scaled_betas}]

def sample_estimation_betas(state, params, spaces):
    
    X = [
        [x / log(x, params["Quai Reward Base Parameter"])]
        for x in spaces[0]["Block Difficulty"]
    ]

    Y = [x > 0 for x in spaces[0]["Qi Taken"]]

    state["Logistic Classifier Queue X"].extend(X)
    state["Logistic Classifier Queue Y"].extend(Y)

    # Start with the past miner choices and then add the conversion choices just
    # in time
    regression_x = state["Logistic Classifier Queue X"][-1000:]
    regression_y = state["Logistic Classifier Queue Y"][-1000:]
    
    state["Logistic Classifier Queue X"] = state["Logistic Classifier Queue X"][-1000:]
    state["Logistic Classifier Queue Y"] = state["Logistic Classifier Queue Y"][-1000:]

    # Have to go through the conversions that have happened in the past 100
    # blocks Since the Historical Converted Quai represents the total number of
    # Quai converted and its stored per blocks basis.     
    num_blocks = len(state["Historical Block Difficulty"])
    if num_blocks > 100:
        num_blocks = 100

    for i in range (0, num_blocks):
        difficulty = state["Historical Block Difficulty"][state["Block Number"]-i]
        # Normalizing the Total Quai converted into the number of miner choices by
        # dividing the value by the block reward
        quai_reward = state["Metrics"]["Hash to Quai Metric"](state, params, [{"Hash": difficulty}])
        # Normalizing the Total Qi converted into the number of miner choices by
        # dividing the value by the block reward
        qi_reward = state["Metrics"]["Hash to Qi Metric"](state, params, [{"Hash": difficulty}])
        
        n_quai = 0
        n_qi = 0
        if len(state["Historical Converted Quai"]) > 0 and len(state["Historical Converted Qi"]) > 0:
            # If the amount of Qi converted is more than the amount of Quai conveted
            # the historical converted Qi will have the Quai value that was conveted
            if state["Historical Converted Qi"][state["Block Number"]-i]["Qi"] < 0: # More Qi was burned
                # doing an assertion to check the impossible case, Quai also cannot be burned in net
                assert state["Historical Converted Qi"][state["Block Number"]-i]["Quai"] > 0
                assert state["Historical Converted Quai"][state["Block Number"]-i]["Quai"] == 0
                assert state["Historical Converted Quai"][state["Block Number"]-i]["Qi"] == 0

                # Historical Converted Quai stores the amount of Qi the Quai was
                # converted to if more Quai was converted to Qi. Otherwise it stores
                # 0. 
                converted_quai = state["Historical Converted Qi"][state["Block Number"]-i]["Quai"]
                n_quai = converted_quai/quai_reward

            elif state["Historical Converted Quai"][state["Block Number"]-i]["Quai"] < 0: # More Qi was created
                # doing an assertion to check the impossible case, More Quai
                # also cannot be created at the same time
                assert state["Historical Converted Quai"][state["Block Number"]-i]["Qi"] > 0
                assert state["Historical Converted Qi"][state["Block Number"]-i]["Quai"] == 0
                assert state["Historical Converted Qi"][state["Block Number"]-i]["Qi"] == 0

                converted_qi = state["Historical Converted Quai"][state["Block Number"]-i]["Qi"]
                n_qi = converted_qi/qi_reward
            else: # No conversion happened
                assert state["Historical Converted Quai"][state["Block Number"]-i]["Quai"] == 0
                assert state["Historical Converted Quai"][state["Block Number"]-i]["Qi"] == 0
                assert state["Historical Converted Qi"][state["Block Number"]-i]["Qi"] == 0
                assert state["Historical Converted Qi"][state["Block Number"]-i]["Quai"] == 0

            converted_x = difficulty/log(difficulty, params["Quai Reward Base Parameter"])
            # Accumulate the logistic classifier queue x with the conversion outpoints 
            regression_x.append(converted_x)
            
            print("n quai", n_quai, "n qi", n_qi)

            if n_quai > 0:
                regression_y.append(-n_quai)                
            elif n_qi > 0:
                regression_y.append(n_qi)                

    # Need to flatten the regression_x list because some of the values in the
    # list are list themselves TODO: check why the above is happening
    regression_x = [x[0] if isinstance(x, (list, tuple, np.ndarray)) else x for x in regression_x]

    # Combine and sort by x values
    data = sorted(zip(regression_x, regression_y))  # Sorted by x
    x_sorted, y_sorted = zip(*data)

    # Initialize counters
    total_ones, total_zeros = 0, 0
    for i in range(0, len(y_sorted)):
        if y_sorted[i] < 0:
            total_zeros += -y_sorted[i]  
        elif y_sorted[i] == 0:
            total_zeros += 1
        elif y_sorted[i] > 0:
            total_ones += y_sorted[i]

    left_zeros = 0
    right_zeros = 0
    left_ones = 0
    right_ones = 0

    best_score = -1000000000
    best_x = None

    scores = []

    x_sorted_flat = [x[0] if isinstance(x, (list, tuple, np.ndarray)) else x for x in x_sorted]
    # Iterate through sorted x values
    for i in range(len(x_sorted_flat)):
        if y_sorted[i] == 0: # Mining choice Quai
            left_zeros += 1
        elif y_sorted[i] == 1: # Mining choice Qi
            right_ones += 1  
        elif y_sorted[i] > 0: # Conversion from Quai to Qi
            right_ones += y_sorted[i]  
        else: # Conversion from Qi to Quai
            left_zeros += -y_sorted[i]

        left_ones = total_ones - right_ones
        right_zeros = total_zeros - left_zeros

        # Calculate score
        score = left_zeros - right_zeros + right_ones - left_ones

        # Update best score and x value
        if score > best_score:
            best_score = score
            best_x = x_sorted[i]
        
        scores.append(score)

    if state["Block Number"] % 100 == 0:
        print("Block Number", state["Block Number"])
        print("x sorted", x_sorted_flat[:i], "scores", scores[:i])
        plt.scatter(x_sorted_flat[:i], scores[:i], s=1)
        plt.xlabel("Block Difficulty")
        plt.ylabel("Scores")
        plt.show()
    
    print("Best x value:", best_x)
    print("Best score:", best_score/100)

    # update the mu value of the diff over log diff
    prev_mu = state["Mu"]
    if type(best_x) == list:
        best_x = best_x[0]

    state["Mu"] = 0.97 * prev_mu + 0.03 * best_x

    return [spaces[0], {"Beta": np.array([-state["Mu"]/2, 0.5]), "Scaled Beta": np.array([-state["Mu"]/2, 0.5])}]

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