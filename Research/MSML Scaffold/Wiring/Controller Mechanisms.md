## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Estimated Mining Beta Vector"])
EES0 --- EE0
EES1(["K Qi"])
EES1 --- EE0
EES2(["K Quai"])
EES2 --- EE0
end

subgraph X5["Controller Mechanisms"]
direction TB
X1["Set K Mechanism"]
X1 --> EES2
X1 --> EES1
X2["Set Estimated Beta Vector Mechanism"]
X2 --> EES0
X3[Domain]

direction LR
direction TB
X3 --"K Space"--> X1
X3 --"Beta Vector Space"--> X2
end
```

## Description

Block Type: Parallel Block
The wiring for mechanisms for controllers
## Components
1. [[Set K Mechanism]]
2. [[Set Estimated Beta Vector Mechanism]]

## All Blocks
1. [[Set Estimated Beta Vector Mechanism]]
2. [[Set K Mechanism]]

## Constraints

## Domain Spaces
1. [[K Space]]
2. [[Beta Vector Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Beta Vector Space]]
2. [[Empty Space]]
3. [[K Space]]
4. [[Terminating Space]]

## Parameters Used
1. [[Minimum K Qi]]
2. [[State Update Skipping Parameter]]

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Estimated Mining Beta Vector|Estimated Mining Beta Vector]]
2. [[Global]].[[Global State-K Qi|K Qi]]
3. [[Global]].[[Global State-K Quai|K Quai]]

