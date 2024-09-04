from math import log


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
    # To be set to a parameter soon
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


def mezzanine_wiring_passthrough(state, params, spaces):
    return spaces


def rolling_logistic_regression_estimation(state, params, spaces):
    X = [
        [1, x / log(x, params["Quai Reward Base Parameter"])]
        for x in spaces[0]["Block Difficulty"]
    ]
    Y = [x > 0 for x in spaces[0]["Qi Taken"]]

    state["Logistic Classifier Queue X"].extend(X)
    state["Logistic Classifier Queue Y"].extend(Y)

    state["Logistic Classifier Queue X"] = state["Logistic Classifier Queue X"][-1000:]
    state["Logistic Classifier Queue Y"] = state["Logistic Classifier Queue Y"][-1000:]

    state["Logistic Classifier"].fit(
        state["Logistic Classifier Queue X"],
        state["Logistic Classifier Queue Y"],
    )

    betas = state["Logistic Classifier"].coef_[0]
    return [spaces[0], {"Beta": betas}]
