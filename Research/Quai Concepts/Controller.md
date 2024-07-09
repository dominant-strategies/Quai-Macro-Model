## Requirements

- The controller should be robust over 6-9 orders of magnitude for things like supply
- If the aggregate flows are balanced than the [[controller]] is working

## Considerations
- If there is a potential for the [[Controller]] to be changing in the future, it should be projected out to ensure that users understand this may happen in the future (instead of it happening ad hoc)
- There should be a [[Schelling Point]] that is approached through [[Trade Tokens Wiring|arbitrage]]
## Design Questions

- What are we [[Stability Metrics|stabilizing]] and over what horizons?
- What is the desired [[Controller Equilibrium|equilibrium]]?

## Interventions Available

### Quai - Qi Exchange Rate

### Quai Reward Scaler

- This is possibly not correct, but it looks like in the old code the reward value was proportional to the base2 log of difficulty times $2^{-(1+kquai)}$ where kquai was set by the controller