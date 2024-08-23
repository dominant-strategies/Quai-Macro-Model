## Description

The policy which determines the amount of Quai or Qi exchanged.
## Called By
1. [[Conversions Boundary Action]]
## Domain Spaces
1. [[Conversion Space]]
## Followed By
1. [[Mint Qi Tokens Mechanism]]
2. [[Mint Quai Tokens Mechanism]]
3. [[Burn Qi Tokens Mechanism]]
4. [[Burn Quai Tokens Mechanism]]
5. [[Update Historical Converted Qi Mechanism]]
6. [[Update Historical Converted Quai Mechanism]]
7. [[Update Locked Qi Mechanism]]
8. [[Update Locked Quai Mechanism]]
9. [[Append to Unlock Schedule Mechanism]]
## Codomain Spaces
1. [[Qi Space]]
2. [[Quai Space]]
3. [[Qi Space]]
4. [[Quai Space]]
5. [[Conversion Log Space]]
6. [[Conversion Log Space]]
7. [[Qi Space]]
8. [[Quai Space]]
9. [[Unlock Schedule Entry Space]]
## Constraints
1. Quai/Qi converted must be less than total circulating
2. Quai/Qi must be greater than the minimum amount parameters
## Parameters Used
1. [[Lockup Options]]
2. [[Minimum Qi Conversion Amount]]
3. [[Minimum Quai Conversion Amount]]
## Metrics Used
1. [[Conversion Rate Metric]]
## Policy Options
### 1. Block Reward Ratio Conversion Policy
#### Description
The conversion ratio is defined by the ratio of the [[Current Block Reward Ratio Metric|current block reward of both Quai and Qi]].
#### Logic
Find the locking return by looking up in the locking options parameter indexed to the locking timeframe in the space and call this r.

- If the asset is Quai, then return spaces for Quai as -TokenValue and 1/ConversionRate(...) * TokenValue * r for Qi.
- Else return Qi as -Token Value and ConversionRate(...) * TokenValue * r for Quai
    
The minting/burning tokens are this same amount as the locked token updates. Also an entry for unlock in the appropriate currency is added.

