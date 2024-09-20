
## Overview

Each of the following scenarios was run under two hashpower regimes:
1. A regime where the aggregate hashpower was held constant over the simulation (contained in the "Spec/Controller Basic Scenarios.ipynb" notebook), and
2. A regime where the aggregate hashpower grew across 5 orders of magnitude over the simulation (contained in the "Spec/Controller Basic Scenarios - Variable Difficulty.ipynb" notebook).

## Sanity Check

### Scenario A: fixed controller parameters

Premise: Ensure the simulation framework is operating as intended, without complications from the controller.

Condition(s): Fix the values of:
- $\mathbf u$, the controller update parameters ($k_{qi}, k_{quai}$); and
- $\pmb{\beta}$, the _miner decision population parameter vector_, i.e. the parameter vector for the miner's probabilistic decision on which token to receive as block reward.

## Controller Testing

### Scenario B: fixed population parameters, miner model

Premise: To test the controller's ability to learn the miner decision population parameter vector when it is fixed, and to analyze the resulting time series.

**Condition(s)**: Fix the values of:
- $k_{qi}$ (control parameter $u_1$), as this is a _numeraire_ for the system; and
- $\pmb{\beta}$, the _miner decision population parameter vector_.

### Scenario C: variable population parameters, miner model

Premise: To test the controller's ability to learn the miner decision population parameter vector when it changes, and to analyze the resulting time series.

**Condition(s)**: 
- Fix the values of:
    - $k_{qi}$ (control parameter $u_1$), as this is a _numeraire_ for the system.
- Draw a realization of $\pmb{\beta}$ from a fixed distribution at two times:
    - Prior to the beginning of each run; and
    - Halfway through each run.

### Scenario D: additional reward ratio feature, miner model

Premise: To test the controller's responsiveness when the miner's actual population parameter vector includes a dependence upon the observed proposed block reward ratio, and to analyze the resulting time series.

**Condition(s)**: 
- Fix the values of:
    - $k_{qi}$ (control parameter $u_1$), as this is a _numeraire_ for the system.
- Draw a realization of $\pmb{\beta}$ from a fixed distribution at two times:
    - Prior to the beginning of each run; and
    - Halfway through each run.


### Scenario E: additional log(reward ratio) feature, miner behavior

Premise: To test the controller's responsiveness when the miner's actual population parameter vector includes a dependence upon the _natural logarithm_ of the observed proposed block reward ratio, and to analyze the resulting time series.

**Condition(s)**: 
- Fix the values of:
    - $k_{qi}$ (control parameter $u_1$), as this is a _numeraire_ for the system.
- Draw a realization of $\pmb{\beta}$ from a fixed distribution at two times:
    - Prior to the beginning of each run; and
    - Halfway through each run.
