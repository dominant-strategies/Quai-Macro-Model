from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression


def build_logistic_classifier(state, params):

    state["Logistic Classifier"] = SGDClassifier(
        loss="log_loss", penalty=None, fit_intercept=False
    )
    return state
