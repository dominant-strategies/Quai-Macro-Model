## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Dummy")]
EE1[("Global")]
EES0(["Total Length"])
EES0 --- EE0
EES1(["Words"])
EES1 --- EE0
EES2(["Block Number"])
EES2 --- EE1
EES3(["Historical Mined Ratio"])
EES3 --- EE1
EES4(["Historical Qi Hash"])
EES4 --- EE1
end

subgraph X9["Mining Mechanisms"]
direction TB
X1["Increment Block Number Mechanism"]
X1 --> EES2
X2["Mint Qi Tokens Mechanism"]
X2 --> EES1
X2 --> EES0
X3["Mint Quai Tokens Mechanism"]
X3 --> EES1
X3 --> EES0
X4["Update Historical Mined Ratio Mechanism"]
X4 --> EES3
X5["Update Historical Qi Hash Mechanism"]
X5 --> EES4
X6["Update Historical Quai Hash Mechanism"]
X6 --> EES4
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
3. [[Global]].[[Global State-Block Number|Block Number]]
4. [[Global]].[[Global State-Historical Mined Ratio|Historical Mined Ratio]]
5. [[Global]].[[Global State-Historical Qi Hash|Historical Qi Hash]]

