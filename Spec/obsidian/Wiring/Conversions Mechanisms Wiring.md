## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Aggregate Hashpower"])
EES0 --- EE0
EES1(["Historical Converted Qi"])
EES1 --- EE0
EES2(["Historical Converted Quai"])
EES2 --- EE0
EES3(["Locked Qi Supply"])
EES3 --- EE0
EES4(["Qi Supply"])
EES4 --- EE0
EES5(["Qi Unlock Schedule"])
EES5 --- EE0
EES6(["Quai Supply"])
EES6 --- EE0
EES7(["Quai Unlock Schedule"])
EES7 --- EE0
end

subgraph X13["Conversions Mechanisms Wiring"]
direction TB
X1["Update Hash Rate Mechanism"]
X1 --> EES0
X2["Mint Qi Tokens Mechanism"]
X2 --> EES4
X3["Mint Quai Tokens Mechanism"]
X3 --> EES6
X4["Burn Qi Tokens Mechanism"]
X4 --> EES4
X5["Burn Quai Tokens Mechanism"]
X5 --> EES6
X6["Update Historical Converted Qi Mechanism"]
X6 --> EES1
X7["Update Historical Converted Quai Mechanism"]
X7 --> EES2
X8["Update Locked Qi Mechanism"]
X8 --> EES3
X9["Update Locked Quai Mechanism"]
X9 --> EES3
X10["Append to Unlock Schedule Mechanism"]
X10 --> EES7
X10 --> EES5
X11[Domain]

direction LR
direction TB
X11 --> X1
X11 --"Qi Space"--> X2
X11 --"Quai Space"--> X3
X11 --"Qi Space"--> X4
X11 --"Quai Space"--> X5
X11 --"Conversion Log Space"--> X6
X11 --"Conversion Log Space"--> X7
X11 --"Qi Space"--> X8
X11 --"Quai Space"--> X9
X11 --"Unlock Schedule Entry Space"--> X10
end
```

## Description

Block Type: Parallel Block

## Components
1. [[Update Hash Rate Mechanism]]
2. [[Mint Qi Tokens Mechanism]]
3. [[Mint Quai Tokens Mechanism]]
4. [[Burn Qi Tokens Mechanism]]
5. [[Burn Quai Tokens Mechanism]]
6. [[Update Historical Converted Qi Mechanism]]
7. [[Update Historical Converted Quai Mechanism]]
8. [[Update Locked Qi Mechanism]]
9. [[Update Locked Quai Mechanism]]
10. [[Append to Unlock Schedule Mechanism]]

## All Blocks
1. [[Append to Unlock Schedule Mechanism]]
2. [[Burn Qi Tokens Mechanism]]
3. [[Burn Quai Tokens Mechanism]]
4. [[Mint Qi Tokens Mechanism]]
5. [[Mint Quai Tokens Mechanism]]
6. [[Update Hash Rate Mechanism]]
7. [[Update Historical Converted Qi Mechanism]]
8. [[Update Historical Converted Quai Mechanism]]
9. [[Update Locked Qi Mechanism]]
10. [[Update Locked Quai Mechanism]]

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
1. [[Global]].[[Global State-Aggregate Hashpower|Aggregate Hashpower]]
2. [[Global]].[[Global State-Historical Converted Qi|Historical Converted Qi]]
3. [[Global]].[[Global State-Historical Converted Quai|Historical Converted Quai]]
4. [[Global]].[[Global State-Locked Qi Supply|Locked Qi Supply]]
5. [[Global]].[[Global State-Qi Supply|Qi Supply]]
6. [[Global]].[[Global State-Qi Unlock Schedule|Qi Unlock Schedule]]
7. [[Global]].[[Global State-Quai Supply|Quai Supply]]
8. [[Global]].[[Global State-Quai Unlock Schedule|Quai Unlock Schedule]]

