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

subgraph X16["Conversions Wiring"]
direction TB
X1["Conversions Boundary Action"]
X2["Conversions Policy"]
subgraph X15["Conversions Mechanisms Wiring"]
direction TB
X3["Update Hash Rate Mechanism"]
X3 --> EES0
X4["Mint Qi Tokens Mechanism"]
X4 --> EES4
X5["Mint Quai Tokens Mechanism"]
X5 --> EES6
X6["Burn Qi Tokens Mechanism"]
X6 --> EES4
X7["Burn Quai Tokens Mechanism"]
X7 --> EES6
X8["Update Historical Converted Qi Mechanism"]
X8 --> EES1
X9["Update Historical Converted Quai Mechanism"]
X9 --> EES2
X10["Update Locked Qi Mechanism"]
X10 --> EES3
X11["Update Locked Quai Mechanism"]
X11 --> EES3
X12["Append to Unlock Schedule Mechanism"]
X12 --> EES7
X12 --> EES5
X13[Domain]

direction LR
direction TB
X13 --> X3
X13 --"Qi Space"--> X4
X13 --"Quai Space"--> X5
X13 --"Qi Space"--> X6
X13 --"Quai Space"--> X7
X13 --"Conversion Log Space"--> X8
X13 --"Conversion Log Space"--> X9
X13 --"Qi Space"--> X10
X13 --"Quai Space"--> X11
X13 --"Unlock Schedule Entry Space"--> X12
end
X1--"Conversion Space"--->X2
X2--"Qi Space
Quai Space
Qi Space
Quai Space
Conversion Log Space
Conversion Log Space
Qi Space
Quai Space
Unlock Schedule Entry Space"----------->X15
end
```

## Description

Block Type: Stack Block
While the [[Mining Payment Policy|election to receive block rewards in Quai or Qi is reserved for miners]], the ability to [[Conversions Wiring|convert Qi and Quai tokens is embedded natively in the protocol]], and is available to any [[Network Participant]] to utilize at any time. The conversion ratio is defined by the ratio of the [[Current Block Reward Ratio Metric|current block reward of both Quai and Qi]].

For example, if the current Quai block reward is 1 and the current Qi block reward is 2, any [[Network Participant]] would be able to [[Burn Qi Tokens Mechanism|burn Qi tokens]] to [[Mint Quai Tokens Mechanism|mint new Quai tokens]] at a rate of 2:1.

This mechanism allows for greater responsiveness in the [[Qi Supply Metric|supply of Qi]], allowing all [[Network Participant|network participants]], not just [[Miner|miners]], to participate in the ongoing [[Trade Tokens Wiring|arbitrage]] between [[Qi Demand]] and [[Qi Supply Metric|Qi supply]].
## Components
1. [[Conversions Boundary Action]]
2. [[Conversions Policy]]
3. [[Conversions Mechanisms Wiring]]

## All Blocks
1. [[Append to Unlock Schedule Mechanism]]
2. [[Burn Qi Tokens Mechanism]]
3. [[Burn Quai Tokens Mechanism]]
4. [[Conversions Boundary Action]]
5. [[Conversions Policy]]
6. [[Mint Qi Tokens Mechanism]]
7. [[Mint Quai Tokens Mechanism]]
8. [[Update Hash Rate Mechanism]]
9. [[Update Historical Converted Qi Mechanism]]
10. [[Update Historical Converted Quai Mechanism]]
11. [[Update Locked Qi Mechanism]]
12. [[Update Locked Quai Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Conversion Log Space]]
2. [[Conversion Space]]
3. [[Empty Space]]
4. [[Qi Space]]
5. [[Quai Space]]
6. [[Terminating Space]]
7. [[Unlock Schedule Entry Space]]

## Parameters Used
1. [[Conversion Percentage Mu]]
2. [[Conversion Percentage Sigma]]
3. [[Lockup Options]]
4. [[Minimum Qi Conversion Amount]]
5. [[Minimum Quai Conversion Amount]]
6. [[Speculator Percentage]]

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

