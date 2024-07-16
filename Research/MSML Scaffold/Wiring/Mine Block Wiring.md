## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Dummy")]
EES0(["Total Length"])
EES0 --- EE0
EES1(["Words"])
EES1 --- EE0
end

subgraph X13["Mine Block Wiring"]
direction TB
X1["Mine Block Boundary Action"]
X2["Block Reward Policy"]
X3["Mining Payment Policy"]
subgraph X12["Mining Mechanisms"]
direction TB
X4["Increment Block Number Mechanism"]
X4 --> EES1
X4 --> EES0
X5["Mint Qi Tokens Mechanism"]
X5 --> EES1
X5 --> EES0
X6["Mint Quai Tokens Mechanism"]
X6 --> EES1
X6 --> EES0
X7["Update Historical Mined Ratio Mechanism"]
X7 --> EES1
X7 --> EES0
X8["Update Historical Qi Hash Mechanism"]
X8 --> EES1
X8 --> EES0
X9["Update Historical Quai Hash Mechanism"]
X9 --> EES1
X9 --> EES0
X10[Domain]

direction LR
direction TB
X10 --> X4
X10 --> X5
X10 --> X6
X10 --> X7
X10 --> X8
X10 --> X9
end
X1--"Block Difficulty Space"--->X2
X2--"Block Reward Options Space"--->X3
X3--->X12
end
```

## Description

Block Type: Stack Block
The wiring for mining a block
## Components
1. [[Mine Block Boundary Action]]
2. [[Block Reward Policy]]
3. [[Mining Payment Policy]]
4. [[Mining Mechanisms]]

## All Blocks
1. [[Block Reward Policy]]
2. [[Increment Block Number Mechanism]]
3. [[Mine Block Boundary Action]]
4. [[Mining Payment Policy]]
5. [[Mint Qi Tokens Mechanism]]
6. [[Mint Quai Tokens Mechanism]]
7. [[Update Historical Mined Ratio Mechanism]]
8. [[Update Historical Qi Hash Mechanism]]
9. [[Update Historical Quai Hash Mechanism]]

## Constraints

## Domain Spaces

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Block Difficulty Space]]
2. [[Block Reward Options Space]]
3. [[Empty Space]]
4. [[Terminating Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Dummy]].[[Dummy State-Total Length|Total Length]]
2. [[Dummy]].[[Dummy State-Words|Words]]

