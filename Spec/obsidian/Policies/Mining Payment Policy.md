## Description

Policy which determines what amount of Quai vs. Qi is taken as payment.
## Called By
1. [[Block Reward Policy]]
## Domain Spaces
1. [[Block Reward Options Space]]
## Followed By
1. [[Increment Block Number Mechanism]]
2. [[Mint Qi Tokens Mechanism]]
3. [[Mint Quai Tokens Mechanism]]
4. [[Update Historical Mined Ratio Mechanism]]
5. [[Update Historical Qi Hash Mechanism]]
6. [[Update Historical Quai Hash Mechanism]]
## Codomain Spaces
1. [[Empty Space]]
## Constraints
## Parameters Used
## Metrics Used
## Policy Options
### 1. Deterministic Mining Payment Policy
#### Description
User chooses either all Qi or all Quai based on which is more valuable.
#### Logic
Compare the price of Qi times Qi amount to price of Quai times Quai amount and pick the larger sum.

