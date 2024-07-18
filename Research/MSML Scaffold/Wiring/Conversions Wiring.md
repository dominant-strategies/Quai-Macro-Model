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

subgraph X12["Conversions Wiring"]
direction TB
X1["Conversions Boundary Action"]
X2["Conversions Policy"]
subgraph X11["Conversions Mechanisms Wiring"]
direction TB
X3["Mint Qi Tokens Mechanism"]
X3 --> EES2
X4["Mint Quai Tokens Mechanism"]
X4 --> EES3
X5["Burn Qi Tokens Mechanism"]
X5 --> EES2
X6["Burn Quai Tokens Mechanism"]
X6 --> EES3
X7["Update Historical Converted Qi Mechanism"]
X7 --> EES0
X8["Update Historical Converted Quai Mechanism"]
X8 --> EES1
X9[Domain]

direction LR
direction TB
X9 --"Qi Space"--> X3
X9 --"Quai Space"--> X4
X9 --"Qi Space"--> X5
X9 --"Quai Space"--> X6
X9 --"Conversion Log Space"--> X7
X9 --"Conversion Log Space"--> X8
end
X1--"Conversion Space"--->X2
X2--"Qi Space
Quai Space
Qi Space
Quai Space
Conversion Log Space
Conversion Log Space"-------->X11
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
1. [[Burn Qi Tokens Mechanism]]
2. [[Burn Quai Tokens Mechanism]]
3. [[Conversions Boundary Action]]
4. [[Conversions Policy]]
5. [[Mint Qi Tokens Mechanism]]
6. [[Mint Quai Tokens Mechanism]]
7. [[Update Historical Converted Qi Mechanism]]
8. [[Update Historical Converted Quai Mechanism]]

## Constraints

## Domain Spaces

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Conversion Log Space]]
2. [[Conversion Space]]
3. [[Empty Space]]
4. [[Qi Space]]
5. [[Quai Space]]
6. [[Terminating Space]]

## Parameters Used
1. [[Minimum Qi Conversion Amount]]
2. [[Minimum Quai Conversion Amount]]

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Historical Converted Qi|Historical Converted Qi]]
2. [[Global]].[[Global State-Historical Converted Quai|Historical Converted Quai]]
3. [[Global]].[[Global State-Qi Supply|Qi Supply]]
4. [[Global]].[[Global State-Quai Supply|Quai Supply]]

