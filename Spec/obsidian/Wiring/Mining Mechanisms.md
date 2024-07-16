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

subgraph X9["Mining Mechanisms"]
direction TB
X1["Increment Block Number Mechanism"]
X1 --> EES0
X2["Mint Qi Tokens Mechanism"]
X2 --> EES3
X3["Mint Quai Tokens Mechanism"]
X3 --> EES4
X4["Update Historical Mined Ratio Mechanism"]
X4 --> EES1
X5["Update Historical Qi Hash Mechanism"]
X5 --> EES2
X6["Update Historical Quai Hash Mechanism"]
X6 --> EES2
X7[Domain]

direction LR
direction TB
X7 --> X1
X7 --"Qi Space"--> X2
X7 --"Quai Space"--> X3
X7 --"Mined Ratio Space"--> X4
X7 --"Qi Hash Space"--> X5
X7 --"Quai Hash Space"--> X6
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
1. [[Qi Space]]
2. [[Quai Space]]
3. [[Mined Ratio Space]]
4. [[Qi Hash Space]]
5. [[Quai Hash Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Empty Space]]
2. [[Mined Ratio Space]]
3. [[Qi Hash Space]]
4. [[Qi Space]]
5. [[Quai Hash Space]]
6. [[Quai Space]]
7. [[Terminating Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Block Number|Block Number]]
2. [[Global]].[[Global State-Historical Mined Ratio|Historical Mined Ratio]]
3. [[Global]].[[Global State-Historical Qi Hash|Historical Qi Hash]]
4. [[Global]].[[Global State-Qi Supply|Qi Supply]]
5. [[Global]].[[Global State-Quai Supply|Quai Supply]]

