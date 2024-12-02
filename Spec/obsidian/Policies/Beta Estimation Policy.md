## Description

The policy which determines the update to beta vector estimates.
## Called By
1. [[Mining Payment Policy]]
## Domain Spaces
1. [[Mined Blocks Space 2]]
## Followed By
1. [[Controller Update Policy]]
2. [[Controller Update Policy]]
## Codomain Spaces
1. [[Mined Blocks Space 2]]
2. [[Beta Vector Space]]
## Constraints
## Parameters Used
## Metrics Used
## Policy Options
### 1. SGD Logistic Classifier Training
#### Description
Simple SGD training with partial fit.
#### Logic
X = [[1, x / log(x, params["Quai Reward Base Parameter"])] for x in spaces[0]["Block Difficulty"]]
Y = [x > 0 for x in spaces[0]["Quai Taken"]]

state["Logistic Classifier"].partial_fit(X, Y, classes=[0, 1])
betas = state["Logistic Classifier"].coef_[0]

### 2. Rolling Logistic Regression Estimation
#### Description
Rolling window of the last 1000 observations used for training the logistic regression.
#### Logic


### 3. Go-Quai implementation of the logistic regression
#### Description
Go-Quai implementation of the logistic regression
#### Logic


### 4. Fixed B1 logistic Regression
#### Description
Logistic Regression with fixed Beta1
#### Logic


