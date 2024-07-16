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

subgraph X9["Mining Mechanisms"]
direction TB
X1["Increment Block Number Mechanism"]
X1 --> EES1
X1 --> EES0
X2["Mint Qi Tokens Mechanism"]
X2 --> EES1
X2 --> EES0
X3["Mint Quai Tokens Mechanism"]
X3 --> EES1
X3 --> EES0
X4["Update Historical Mined Ratio Mechanism"]
X4 --> EES1
X4 --> EES0
X5["Update Historical Qi Hash Mechanism"]
X5 --> EES1
X5 --> EES0
X6["Update Historical Quai Hash Mechanism"]
X6 --> EES1
X6 --> EES0
X7[Domain]

direction LR
direction TB
X7 --> X1
X7 --> X2
X7 --> X3
X7 --> X4
X7 --> X5
X7 --> X6
end
```

## Description

Block Type: Parallel Block
The mechanisms associated with mining a block
## Components
1. [[Increment Block Number Mechanism]]
2. [[Mint Qi Tokens Mechanism]]
3. [[Mint Quai Tokens Mechanism]]
4. [[Update Historical Mined Ratio Mechanism]]
5. [[Update Historical Qi Hash Mechanism]]
6. [[Update Historical Quai Hash Mechanism]]

## All Blocks
1. [[Increment Block Number Mechanism]]
2. [[Mint Qi Tokens Mechanism]]
3. [[Mint Quai Tokens Mechanism]]
4. [[Update Historical Mined Ratio Mechanism]]
5. [[Update Historical Qi Hash Mechanism]]
6. [[Update Historical Quai Hash Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Empty Space]]
2. [[Terminating Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Dummy]].[[Dummy State-Total Length|Total Length]]
2. [[Dummy]].[[Dummy State-Words|Words]]

