## For Client

### Block Rewards 

For Quai and Qi block rewards, there is only proportionally right now given, which is:
$$\text { BlockReward }{ }_{Q u a i} \propto \log _2(\text { Difficulty })$$
$$\text { BlockReward }_{Q i} \propto(\text { Difficulty })$$
From the old code, the following relations are used:

$$\text { BlockReward }{ }_{Q u a i} = 2^{-(1+k_{Quai})} \log _2(\text { Difficulty })$$
$$\text { BlockReward }_{Q i} = \frac{\text { Difficulty }}{k_{Qi}}$$
And $k_{Quai}$ is set/modified by the controller

The following are the questions related to this:
1. Is this the final form for block rewards?
2. Should the controller only be setting $k_{Quai}$? If so is $k_{Qi}$ a constant or how else is it set?

### Controller Interventions

- It sounds like the primary intervention for the controller is setting an exchange rate between Qi and Quai that can be acted upon
- The working mental model of how this happens is the following:
1. The controller is modifying $k_{Quai}$ and possibly $k_{Qi}$
2. As these values get modified so do the current block rewards
3. The exchange rate is set to be a the proportion between the latest block reward (or moving average or similar) for the Qi + Quai
4. As long as it is above a minimum amount, a user can convert Qi to Quai or vice versa, and the treasury will burn/mint based on that?

Questions:
1. Is the working model above correct?
2. Does the treasury ever hold balances or is everything passed straight through to minting/burning mechanisms?
3. For the exchange rate, is there any smoothing that we need to use on it or is last block reward fine because controller should have some smoothing?
4. Are there any other interventions besides this exchange rate pricing that the controller will be able to take on?
5. Are there any limitations on when a user would be able to exchange?

## Internal

Only for internal brainstorming right now

1. Is [[Quai Type|Quai]] supposed to always be deflationary or just in aggregate? During first meeting it was said that it was supposed to be a classic deflationary token.
2. Are there any other interventions besides [[Controller Exchange Wiring]] for the [[Controller]]?
	1. Or is it just the constants for block rewards that get toggled
	2. Or is it both and the controller toggles block rewards + exchange rates?
3. What are we [[Stability Metrics|stabilizing]] and over what horizons?
4. What are the priorities between:
	- Having the exchange between [[Quai Type|Quai]] and [[Qi Type|Qi]] be stable / close to the theoretical "no arbitrage price"
	- Have stability in price movements, i.e. low standard deviation in either price returns or log price returns
	- Have stability against energy as a benchmark (likely difficult because it requires an assumption on appropriate benchmarking of electricity prices)
5. What is the appropriate time scale for the simulation?
	- The timescale of the simulation likely will depend on the actuation frequency of the [[controller]]
6. Is the controller going to be called when certain thresholds are breached or will the controller be called at some given frequency of time?
7. "Quai is a digitally scarce asset designed to function as a programmable store-of-value within Quai Network. Quai has an effectively fixed supply in the sense that inflation trends toward zero and there will be a terminal supply amount -- however, [this terminal supply amount will be determined by market dynamics, and is not predefined](https://qu.ai/docs/learn/tokenomics/token-dynamics/supply-growth/)." -> Is there any situation in which inflation can pick up again leading to this not being true?
	1. I believe it should be true with it becoming harder and harder for hashes to be found, but does the reward size going up outpace it?
8. The controller doesn't control anything related to the issuance constant right? I assume it is a constant but if it was a flexible variable then it might be in the purview of the controller.
9. Is Current Block Reward Ratio Metric the same thing as Block Mining Rewards Ratio Metric
10. Do we need to model vesting as part of our process?
11. Do we need to track locked vs. unlocked tokens?
12. To what extent should we model speculators