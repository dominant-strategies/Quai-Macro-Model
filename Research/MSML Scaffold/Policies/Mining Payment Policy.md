## Description

Policy which determines what amount of Quai vs. Qi is taken as payment.
## Called By
1. [[Block Reward Policy]]
## Domain Spaces
1. [[Block Reward Options Space]]
## Followed By
1. [[Beta Estimation Policy]]
2. [[Mezzanine Wiring Passthrough]]
3. [[Mezzanine Wiring Passthrough]]
4. [[Mezzanine Wiring Passthrough]]
5. [[Mezzanine Wiring Passthrough]]
6. [[Mezzanine Wiring Passthrough]]
## Codomain Spaces
1. [[Mined Blocks Space 2]]
2. [[Qi Space]]
3. [[Quai Space]]
4. [[Mined Ratio Space]]
5. [[Qi Hash Space]]
6. [[Quai Hash Space]]
## Constraints
## Parameters Used
## Metrics Used
1. [[Qi to Hash Metric]]
2. [[Quai to Hash Metric]]
## Policy Options
### 1. Deterministic Mining Payment Policy
#### Description
User chooses either all Qi or all Quai based on which is more valuable based on USD prices.
#### Logic

Compare the price of Qi times Qi amount to price of Quai times Quai amount and pick the larger sum. Then the values for each iteration loop are as follows:
1. Qi Space is equal to 0 or the Qi amount
2. Quai Space is equal to 0 or the Quai amount
3. Mined Ratio Space has 0 if Qi was chosen, 1 if Quai was chosen
4. Qi Hash Space has 0 if Quai was chosen, otherwise $QiToHashMetric(Qi)$
5. Quai Hash Space has 0 if Qi was chosen, otherwise $QuaiToHashMetric(Quai)$


Aggregate all the data into total values after iteration.

