from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.base import BaseEstimator
from scipy.optimize import minimize
import numpy as np


def build_logistic_classifier(state, params):
    if params["FP Beta Estimation Policy"] == "Rolling Logistic Regression Estimation":
        state["Logistic Classifier"] = LogisticRegression(
            penalty='l2', fit_intercept=True, warm_start=True,
            class_weight = 'balanced', max_iter = 500
        )
        state["Logistic Classifier Queue X"] = []
        state["Logistic Classifier Queue Y"] = []
    elif params["FP Beta Estimation Policy"] == "SGD Logistic Classifier Training":
        state["Logistic Classifier"] = SGDClassifier(
            loss="log_loss", penalty=None, fit_intercept=False
        )
    elif params["FP Beta Estimation Policy"] == "Fixed B1 logistic Regression":
        state["Logistic Classifier"] = FixedB1LogisticRegression()
        state["Logistic Classifier Queue X"] = []
        state["Logistic Classifier Queue Y"] = []
    else:
        state["Logistic Classifier Queue X"] = []
        state["Logistic Classifier Queue Y"] = []
    return state

class FixedB1LogisticRegression:
    def __init__(self, learning_rate=0.01, max_iter=1000):
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.b0 = None  # Intercept
        self.b1 = 0.5  # Coefficient for the first feature

    def _sigmoid(self, z):
        """Sigmoid function."""
        return 1 / (1 + np.exp(-z))

    def _log_loss(self, y, y_pred):
        """Log-loss function."""
        # Convert inputs to NumPy arrays
        y = np.array(y)
        y_pred = np.array(y_pred)
        return -np.mean(y * np.log(y_pred + 1e-15) + (1 - y) * np.log(1 - y_pred + 1e-15))

    def fit(self, b0, X, y):
        """Fit the logistic regression model using gradient descent."""
        # Ensure inputs are NumPy arrays
        X = np.array(X)
        y = np.array(y)

        # Initialize coefficients
        self.b0 = b0

        for i in range(self.max_iter):
            # Compute predictions
            z = self.b0 + self.b1 * X[:, 0]
            y_pred = self._sigmoid(z)

            # Compute gradients
            gradient_b0 = np.mean(y_pred - y)

            # Update coefficients
            self.b0 -= self.learning_rate * gradient_b0

            # Print loss every 100 iterations
            if i % 500 == 0:
                loss = self._log_loss(y, y_pred)
                print(f"Iteration {i}, Loss: {loss}")
                
        # Set sklearn-style attributes
        self.coef_ = np.array([[self.b1]])  # 2D array for coefficients
        self.intercept_ = np.array([self.b0])  # 1D array for intercept

    def predict_proba(self, X):
        """Predict probabilities for each class."""
        z = self.b0 + self.b1 * X[:, 0]
        probs = self._sigmoid(z)
        return np.vstack([1 - probs, probs]).T

    def predict(self, X):
        """Predict binary class labels."""
        probs = self.predict_proba(X)
        return (probs[:, 1] >= 0.5).astype(int)