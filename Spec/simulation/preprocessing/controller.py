from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression


def build_logistic_classifier(state, params):
    if params["FP Beta Estimation Policy"] == "Rolling Logistic Regression Estimation":
        state["Logistic Classifier"] = LogisticRegression(
            penalty=None, fit_intercept=False, warm_start=True
        )
        state["Logistic Classifier Queue X"] = []
        state["Logistic Classifier Queue Y"] = []
    else:
        state["Logistic Classifier"] = SGDClassifier(
            loss="log_loss", penalty=None, fit_intercept=False
        )
    return state
