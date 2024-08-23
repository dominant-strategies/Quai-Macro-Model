## Description

Boundary action which determines amount of potentially converted Qi or Quai.
## Called By

## Followed By
1. [[Conversions Policy]]

## Constraints

## Codomain Spaces
1. [[Conversion Space]]

## Boundary Action Options:
### 1. Conversions Boundary Action V1
#### Description
Basic boundary action that follows the latest mining ratio
#### Logic
Inputs:

1. Latest mined ratio, pulled from state: $R$
2. Speculator percentage, parameter: $P$
3. Supply of Quai/Qi where Q is which currency to use $S_Q$
4. Conversion percentage mu, the average percentage of traded capital converted, $\mu$
5. Conversion percentage sigma, the standard deviation of the percentage of traded capital converted, $\sigma$
6. Lockup options, $L$

Logic:
1. Decide which side to trade based on mined ratio. Take $R$ as the probability of choosing Quai and use a random sample to determine. We will use $Q$ to denote this side.
2. Determine the potentially traded capital $T$ as $T = S_Q \cdot P$.
3. Find the conversion size as $C = MAX(MIN(NORM(\mu, \sigma), 1),0) \cdot T$
4. Randomly select the lockup horizon $H$ with equal probability from the lockup options L
5. Return space of: {Token: Q,
Amount: C,
Locking Time: H}

### 2. TEST Quai Conversion
#### Description
Test function that moves to exchange 100 Quai and always picks the second lowest lock up period.
#### Logic
Return a space with quai conversion of 100

### 3. TEST Qi Conversion
#### Description
Test function that moves to exchange 100 Qi and always picks the second lowest lock up period.
#### Logic
Return a space with qi conversion of 100

