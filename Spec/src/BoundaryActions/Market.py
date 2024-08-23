conversions_boundary_action_v1 = {
    "name": "Conversions Boundary Action V1",
    "description": "Basic boundary action that follows the latest mining ratio",
    "logic": r"""Inputs:

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
Locking Time: H}""",
}

test_quai_conversion = {
    "name": "TEST Quai Conversion",
    "description": "Test function that moves to exchange 100 Quai and always picks the second lowest lock up period.",
    "logic": "Return a space with quai conversion of 100",
}

test_qi_conversion = {
    "name": "TEST Qi Conversion",
    "description": "Test function that moves to exchange 100 Qi and always picks the second lowest lock up period.",
    "logic": "Return a space with qi conversion of 100",
}

conversions_boundary_action = {
    "name": "Conversions Boundary Action",
    "description": "Boundary action which determines amount of potentially converted Qi or Quai.",
    "constraints": [],
    "boundary_action_options": [
        conversions_boundary_action_v1,
        test_quai_conversion,
        test_qi_conversion,
    ],
    "called_by": [],
    "codomain": ["Conversion Space"],
    "parameters_used": ["Lockup Options"],
    "metrics_used": ["Conversion Rate Metric"],
}

test_price_movements = {
    "name": "TEST Price Movements Boundary",
    "description": r"Testing function for price that always returns a 5% and 10% return on assets for Qi and Quai respectively.",
    "logic": "",
}


hashpower_price_movement = {
    "name": "Hashpower Price Movement",
    "description": r"Movements of the asset prices are based on hashpower for Qi and the conversion rate for Quai with smoothing applied.",
    "logic": r"""Inputs:

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
$$r_{Quai} = \frac{P_{Quai}^{t+1}}{P_{Quai}^{t}} - 1$$""",
}

price_movements_boundary_action = {
    "name": "Price Movements Boundary Action",
    "description": "Boundary action which begins the process of price changes.",
    "constraints": [],
    "boundary_action_options": [test_price_movements, hashpower_price_movement],
    "called_by": [],
    "codomain": ["Price Movement Space"],
    "parameters_used": [
        "Asset Return Parameterization",
        "Price EWMA Lambda",
        "Hashpower Cost Series",
        "Qi Price Movemement Sigma",
        "Quai Price Movemement Sigma",
    ],
    "metrics_used": ["Conversion Rate"],
}


market_boundary_actions = [conversions_boundary_action, price_movements_boundary_action]
