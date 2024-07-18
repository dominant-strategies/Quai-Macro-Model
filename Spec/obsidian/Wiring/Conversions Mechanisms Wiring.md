## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Historical Converted Qi"])
EES0 --- EE0
EES1(["Historical Converted Quai"])
EES1 --- EE0
EES2(["Qi Supply"])
EES2 --- EE0
EES3(["Quai Supply"])
EES3 --- EE0
end

subgraph X9["Conversions Mechanisms Wiring"]
direction TB
X1["Mint Qi Tokens Mechanism"]
X1 --> EES2
X2["Mint Quai Tokens Mechanism"]
X2 --> EES3
X3["Burn Qi Tokens Mechanism"]
X3 --> EES2
X4["Burn Quai Tokens Mechanism"]
X4 --> EES3
X5["Update Historical Converted Qi Mechanism"]
X5 --> EES0
X6["Update Historical Converted Quai Mechanism"]
X6 --> EES1
X7[Domain]

direction LR
direction TB
X7 --"Qi Space"--> X1
X7 --"Quai Space"--> X2
X7 --"Qi Space"--> X3
X7 --"Quai Space"--> X4
X7 --"Conversion Log Space"--> X5
X7 --"Conversion Log Space"--> X6
end
```

## Description

Block Type: Parallel Block

## Components
1. [[Mint Qi Tokens Mechanism]]
2. [[Mint Quai Tokens Mechanism]]
3. [[Burn Qi Tokens Mechanism]]
4. [[Burn Quai Tokens Mechanism]]
5. [[Update Historical Converted Qi Mechanism]]
6. [[Update Historical Converted Quai Mechanism]]

## All Blocks
1. [[Burn Qi Tokens Mechanism]]
2. [[Burn Quai Tokens Mechanism]]
3. [[Mint Qi Tokens Mechanism]]
4. [[Mint Quai Tokens Mechanism]]
5. [[Update Historical Converted Qi Mechanism]]
6. [[Update Historical Converted Quai Mechanism]]

## Constraints

## Domain Spaces
1. [[Qi Space]]
2. [[Quai Space]]
3. [[Qi Space]]
4. [[Quai Space]]
5. [[Conversion Log Space]]
6. [[Conversion Log Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Conversion Log Space]]
2. [[Empty Space]]
3. [[Qi Space]]
4. [[Quai Space]]
5. [[Terminating Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Historical Converted Qi|Historical Converted Qi]]
2. [[Global]].[[Global State-Historical Converted Quai|Historical Converted Quai]]
3. [[Global]].[[Global State-Qi Supply|Qi Supply]]
4. [[Global]].[[Global State-Quai Supply|Quai Supply]]

