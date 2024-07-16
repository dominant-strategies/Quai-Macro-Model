## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Block Number"])
EES0 --- EE0
EES1(["Historical Mined Ratio"])
EES1 --- EE0
EES2(["Historical Qi Hash"])
EES2 --- EE0
EES3(["Qi Supply"])
EES3 --- EE0
EES4(["Quai Supply"])
EES4 --- EE0
end

subgraph X13["Mine Block Wiring"]
direction TB
X1["Mine Block Boundary Action"]
X2["Block Reward Policy"]
X3["Mining Payment Policy"]
subgraph X12["Mining Mechanisms"]
direction TB
X4["Increment Block Number Mechanism"]
X4 --> EES0
X5["Mint Qi Tokens Mechanism"]
X5 --> EES3
X6["Mint Quai Tokens Mechanism"]
X6 --> EES4
X7["Update Historical Mined Ratio Mechanism"]
X7 --> EES1
X8["Update Historical Qi Hash Mechanism"]
X8 --> EES2
X9["Update Historical Quai Hash Mechanism"]
X9 --> EES2
X10[Domain]

direction LR
direction TB
X10 --> X4
X10 --"Qi Space"--> X5
X10 --"Quai Space"--> X6
X10 --"Mined Ratio Space"--> X7
X10 --"Qi Hash Space"--> X8
X10 --"Quai Hash Space"--> X9
end
X1--"Block Difficulty Space"--->X2
X2--"Block Reward Options Space"--->X3
X3--"Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space"------->X12
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
4. [[Mined Ratio Space]]
5. [[Qi Hash Space]]
6. [[Qi Space]]
7. [[Quai Hash Space]]
8. [[Quai Space]]
9. [[Terminating Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Block Number|Block Number]]
2. [[Global]].[[Global State-Historical Mined Ratio|Historical Mined Ratio]]
3. [[Global]].[[Global State-Historical Qi Hash|Historical Qi Hash]]
4. [[Global]].[[Global State-Qi Supply|Qi Supply]]
5. [[Global]].[[Global State-Quai Supply|Quai Supply]]

