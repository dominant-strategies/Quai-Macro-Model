## Description

Boundary action which begins the process of price changes.
## Called By

## Followed By
1. [[Price Movements Policy]]

## Constraints

## Codomain Spaces
1. [[Price Movement Space]]

## Boundary Action Options:
### 1. TEST Price Movements Boundary
#### Description
Testing function for price that always returns a 5% and 10% return on assets for Qi and Quai respectively.
#### Logic


### 2. Hashpower Price Movement
#### Description
Movements of the asset prices are based on hashpower for Qi and the conversion rate for Quai with smoothing applied.
#### Logic
Inputs:

1. EWM Parameter - $\lambda$: The exponential decay parameter
2. Conversion Rate Metric - $C_i(...)$: The metric for the current conversion rate, taking in the state variables of difficulty, $k_{qi}$, $k_{quai}$
3. Current Qi Price - $P_{Qi}^t$
4. Current Quai Price - $P_{Quai}^t$
5. Current Hashpower Cost - $H_i$
6. Price Movement Randomness Parameters, assumption of 0 for mean of randomness - $\sigma_{Quai}$, $\sigma_{Qi}$

The price targets:

$$P_{Qi}^{t+1} = \lambda H_i + (1-\lambda)P_{Qi}^{t} + NORM(0, \sigma_{Qi}) P_{Qi}^{t}$$

$$P_{Quai}^{t+1} = \lambda C_i(...)P_{Qi} + (1-\lambda)P_{Quai}^{t} + NORM(0, \sigma_{Quai}) P_{Quai}^{t}$$

Conversion into a return space (for compatibility with the way the block logic works/space output schema):

$$r_{Qi} = \frac{P_{Qi}^{t+1}}{P_{Qi}^{t}} - 1$$
$$r_{Quai} = \frac{P_{Quai}^{t+1}}{P_{Quai}^{t}} - 1$$

