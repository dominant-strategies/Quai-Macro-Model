## Description

The policy which determines the amount of Quai or Qi exchanged.
## Called By
1. [[Conversions Boundary Action]]
## Domain Spaces
1. [[Conversion Space]]
## Followed By
1. [[Mint Qi Tokens Mechanism]]
2. [[Mint Quai Tokens Mechanism]]
## Codomain Spaces
1. [[Qi Space]]
2. [[Quai Space]]
## Constraints
## Parameters Used
1. [[Minimum Qi Conversion Amount]]
2. [[Minimum Quai Conversion Amount]]
## Metrics Used
1. [[Current Block Reward Ratio Metric]]
## Policy Options
### 1. Block Reward Ratio Conversion Policy
#### Description
The conversion ratio is defined by the ratio of the [[Current Block Reward Ratio Metric|current block reward of both Quai and Qi]].
#### Logic
If the asset is Quai, then return spaces for Quai as -TokenValue and 1/[[Current Block Reward Ratio Metric]] * TokenValue for Qi.
    Else return Qi as -Token Value and [[Current Block Reward Ratio Metric]] * TokenValue for Quai

