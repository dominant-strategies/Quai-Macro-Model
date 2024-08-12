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

subgraph X14["Mine Block Wiring"]
direction TB
X1["Mine Block Boundary Action"]
X2["Mining Policy"]
X3["Block Reward Policy"]
X4["Mining Payment Policy"]
subgraph X13["Mining Mechanisms"]
direction TB
X5["Increment Block Number Mechanism"]
X5 --> EES0
X6["Mint Qi Tokens Mechanism"]
X6 --> EES3
X7["Mint Quai Tokens Mechanism"]
X7 --> EES4
X8["Update Historical Mined Ratio Mechanism"]
X8 --> EES1
X9["Update Historical Qi Hash Mechanism"]
X9 --> EES2
X10["Update Historical Quai Hash Mechanism"]
X10 --> EES2
X11[Domain]

direction LR
direction TB
X11 --> X5
X11 --"Qi Space"--> X6
X11 --"Quai Space"--> X7
X11 --"Mined Ratio Space"--> X8
X11 --"Qi Hash Space"--> X9
X11 --"Quai Hash Space"--> X10
end
X1--"Pre-Mining Space"--->X2
X2--"Mined Blocks Space"--->X3
X3--"Block Reward Options Space"--->X4
X4--"Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space"------->X13
end
```

## Description

Block Type: Stack Block
The wiring for mining a block
## Components
1. [[Mine Block Boundary Action]]
2. [[Mining Policy]]
3. [[Block Reward Policy]]
4. [[Mining Payment Policy]]
5. [[Mining Mechanisms]]

## All Blocks
1. [[Block Reward Policy]]
2. [[Increment Block Number Mechanism]]
3. [[Mine Block Boundary Action]]
4. [[Mining Payment Policy]]
5. [[Mining Policy]]
6. [[Mint Qi Tokens Mechanism]]
7. [[Mint Quai Tokens Mechanism]]
8. [[Update Historical Mined Ratio Mechanism]]
9. [[Update Historical Qi Hash Mechanism]]
10. [[Update Historical Quai Hash Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Block Reward Options Space]]
2. [[Empty Space]]
3. [[Mined Blocks Space]]
4. [[Mined Ratio Space]]
5. [[Pre-Mining Space]]
6. [[Qi Hash Space]]
7. [[Qi Space]]
8. [[Quai Hash Space]]
9. [[Quai Space]]
10. [[Terminating Space]]

## Parameters Used
1. [[Quai Reward Base Parameter]]

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Block Number|Block Number]]
2. [[Global]].[[Global State-Historical Mined Ratio|Historical Mined Ratio]]
3. [[Global]].[[Global State-Historical Qi Hash|Historical Qi Hash]]
4. [[Global]].[[Global State-Qi Supply|Qi Supply]]
5. [[Global]].[[Global State-Quai Supply|Quai Supply]]

