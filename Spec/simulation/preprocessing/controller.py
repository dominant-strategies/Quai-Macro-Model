from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression


def build_logistic_classifier(state, params):
    if params["FP Beta Estimation Policy"] == "Rolling Logistic Regression Estimation":
        state["Logistic Classifier"] = LogisticRegression(
            penalty='l2', fit_intercept=True, warm_start=True,
            class_weight = 'balanced', max_iter = 500
        )
        state["Logistic Classifier Queue X"] = []
        state["Logistic Classifier Queue Y"] = []
    else:
        state["Logistic Classifier"] = SGDClassifier(
            loss="log_loss", penalty=None, fit_intercept=False
        )
    return state
