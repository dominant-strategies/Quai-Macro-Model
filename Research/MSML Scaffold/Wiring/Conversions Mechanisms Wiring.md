## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Historical Converted Qi"])
EES0 --- EE0
EES1(["Historical Converted Quai"])
EES1 --- EE0
EES2(["Locked Qi Supply"])
EES2 --- EE0
EES3(["Qi Supply"])
EES3 --- EE0
EES4(["Qi Unlock Schedule"])
EES4 --- EE0
EES5(["Quai Supply"])
EES5 --- EE0
EES6(["Quai Unlock Schedule"])
EES6 --- EE0
end

subgraph X12["Conversions Mechanisms Wiring"]
direction TB
X1["Mint Qi Tokens Mechanism"]
X1 --> EES3
X2["Mint Quai Tokens Mechanism"]
X2 --> EES5
X3["Burn Qi Tokens Mechanism"]
X3 --> EES3
X4["Burn Quai Tokens Mechanism"]
X4 --> EES5
X5["Update Historical Converted Qi Mechanism"]
X5 --> EES0
X6["Update Historical Converted Quai Mechanism"]
X6 --> EES1
X7["Update Locked Qi Mechanism"]
X7 --> EES2
X8["Update Locked Quai Mechanism"]
X8 --> EES2
X9["Append to Unlock Schedule Mechanism"]
X9 --> EES6
X9 --> EES4
X10[Domain]

direction LR
direction TB
X10 --"Qi Space"--> X1
X10 --"Quai Space"--> X2
X10 --"Qi Space"--> X3
X10 --"Quai Space"--> X4
X10 --"Conversion Log Space"--> X5
X10 --"Conversion Log Space"--> X6
X10 --"Qi Space"--> X7
X10 --"Quai Space"--> X8
X10 --"Unlock Schedule Entry Space"--> X9
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
7. [[Update Locked Qi Mechanism]]
8. [[Update Locked Quai Mechanism]]
9. [[Append to Unlock Schedule Mechanism]]

## All Blocks
1. [[Append to Unlock Schedule Mechanism]]
2. [[Burn Qi Tokens Mechanism]]
3. [[Burn Quai Tokens Mechanism]]
4. [[Mint Qi Tokens Mechanism]]
5. [[Mint Quai Tokens Mechanism]]
6. [[Update Historical Converted Qi Mechanism]]
7. [[Update Historical Converted Quai Mechanism]]
8. [[Update Locked Qi Mechanism]]
9. [[Update Locked Quai Mechanism]]

## Constraints

## Domain Spaces
1. [[Qi Space]]
2. [[Quai Space]]
3. [[Qi Space]]
4. [[Quai Space]]
5. [[Conversion Log Space]]
6. [[Conversion Log Space]]
7. [[Qi Space]]
8. [[Quai Space]]
9. [[Unlock Schedule Entry Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Conversion Log Space]]
2. [[Empty Space]]
3. [[Qi Space]]
4. [[Quai Space]]
5. [[Terminating Space]]
6. [[Unlock Schedule Entry Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Historical Converted Qi|Historical Converted Qi]]
2. [[Global]].[[Global State-Historical Converted Quai|Historical Converted Quai]]
3. [[Global]].[[Global State-Locked Qi Supply|Locked Qi Supply]]
4. [[Global]].[[Global State-Qi Supply|Qi Supply]]
5. [[Global]].[[Global State-Qi Unlock Schedule|Qi Unlock Schedule]]
6. [[Global]].[[Global State-Quai Supply|Quai Supply]]
7. [[Global]].[[Global State-Quai Unlock Schedule|Quai Unlock Schedule]]

