## Description

Policy which determines what amount of Quai vs. Qi is taken as payment.
## Called By
1. [[Block Reward Policy]]
## Domain Spaces
1. [[Block Reward Options Space]]
## Followed By
1. [[Mint Qi Tokens Mechanism]]
2. [[Mint Quai Tokens Mechanism]]
3. [[Update Historical Mined Ratio Mechanism]]
4. [[Update Historical Qi Hash Mechanism]]
5. [[Update Historical Quai Hash Mechanism]]
## Codomain Spaces
1. [[Qi Space]]
2. [[Quai Space]]
3. [[Mined Ratio Space]]
4. [[Qi Hash Space]]
5. [[Quai Hash Space]]
## Constraints
## Parameters Used
## Metrics Used
## Policy Options
### 1. Deterministic Mining Payment Policy
#### Description
User chooses either all Qi or all Quai based on which is more valuable.
#### Logic
Compare the price of Qi times Qi amount to price of Quai times Quai amount and pick the larger sum.

