## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Qi Supply"])
EES0 --- EE0
EES1(["Quai Supply"])
EES1 --- EE0
end

subgraph X7["Conversions Mechanisms Wiring"]
direction TB
X1["Mint Qi Tokens Mechanism"]
X1 --> EES0
X2["Mint Quai Tokens Mechanism"]
X2 --> EES1
X3["Burn Qi Tokens Mechanism"]
X3 --> EES0
X4["Burn Quai Tokens Mechanism"]
X4 --> EES1
X5[Domain]

direction LR
direction TB
X5 --"Qi Space"--> X1
X5 --"Quai Space"--> X2
X5 --"Qi Space"--> X3
X5 --"Quai Space"--> X4
end
```

## Description

Block Type: Parallel Block

## Components
1. [[Mint Qi Tokens Mechanism]]
2. [[Mint Quai Tokens Mechanism]]
3. [[Burn Qi Tokens Mechanism]]
4. [[Burn Quai Tokens Mechanism]]

## All Blocks
1. [[Burn Qi Tokens Mechanism]]
2. [[Burn Quai Tokens Mechanism]]
3. [[Mint Qi Tokens Mechanism]]
4. [[Mint Quai Tokens Mechanism]]

## Constraints

## Domain Spaces
1. [[Qi Space]]
2. [[Quai Space]]
3. [[Qi Space]]
4. [[Quai Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Empty Space]]
2. [[Qi Space]]
3. [[Quai Space]]
4. [[Terminating Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Qi Supply|Qi Supply]]
2. [[Global]].[[Global State-Quai Supply|Quai Supply]]

