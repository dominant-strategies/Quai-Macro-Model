## Description

The policy for updating the prices.
## Called By
1. [[Price Movements Boundary Action]]
## Domain Spaces
1. [[Price Movement Space]]
## Followed By
1. [[Update Prices Mechanism]]
## Codomain Spaces
1. [[Price Space]]
## Constraints
## Parameters Used
## Metrics Used
## Policy Options
### 1. Price Movements Policy V1
#### Description
Simple policy that only checks that values > -1 for return and then computes new price
#### Logic
For each asset, multiply the (1+return) in to get final price

