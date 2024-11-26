## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Locked Qi Supply"])
EES0 --- EE0
EES1(["Locked Quai Supply"])
EES1 --- EE0
EES2(["Qi Unlock Schedule"])
EES2 --- EE0
EES3(["Quai Unlock Schedule"])
EES3 --- EE0
end

subgraph X5["DO NOT USE Unlock Tokens Wiring"]
direction TB
X1["Unlock Tokens Control Action"]
X2["Unlock Tokens Policy"]
X3["Unlock Tokens Mechanism"]
X3 --> EES1
X3 --> EES0
X3 --> EES3
X3 --> EES2
X4["DO NOT USE Print Hello Boundary Action"]
X1--->X2
X2--"Unlock Tokens Space"--->X3
X3--->X4
end
```

## Description

Block Type: Stack Block
The wiring for movements on the price of Qi and Quai
## Components
1. [[Unlock Tokens Control Action]]
2. [[Unlock Tokens Policy]]
3. [[Unlock Tokens Mechanism]]
4. [[DO NOT USE Print Hello Boundary Action]]

## All Blocks
1. [[DO NOT USE Print Hello Boundary Action]]
2. [[Unlock Tokens Control Action]]
3. [[Unlock Tokens Mechanism]]
4. [[Unlock Tokens Policy]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Empty Space]]
2. [[Terminating Space]]
3. [[Unlock Tokens Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Locked Qi Supply|Locked Qi Supply]]
2. [[Global]].[[Global State-Locked Quai Supply|Locked Quai Supply]]
3. [[Global]].[[Global State-Qi Unlock Schedule|Qi Unlock Schedule]]
4. [[Global]].[[Global State-Quai Unlock Schedule|Quai Unlock Schedule]]

