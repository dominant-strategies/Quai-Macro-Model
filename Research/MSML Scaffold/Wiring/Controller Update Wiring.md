## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["K Qi"])
EES0 --- EE0
EES1(["K Quai"])
EES1 --- EE0
end

subgraph X4["Controller Update Wiring"]
direction TB
X1["Controller Update Control Action"]
X2["Controller Update Policy"]
X3["Set K Mechanism"]
X3 --> EES1
X3 --> EES0
X1--"Observable State Space"--->X2
X2--"K Space"--->X3
end
```

## Description

Block Type: Stack Block
The wiring for the controller actions
## Components
1. [[Controller Update Control Action]]
2. [[Controller Update Policy]]
3. [[Set K Mechanism]]

## All Blocks
1. [[Controller Update Control Action]]
2. [[Controller Update Policy]]
3. [[Set K Mechanism]]

## Constraints

## Domain Spaces

## Codomain Spaces
1. [[Terminating Space]]

## All Spaces Used
1. [[K Space]]
2. [[Observable State Space]]
3. [[Terminating Space]]

## Parameters Used
1. [[PID Parameterization]]

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-K Qi|K Qi]]
2. [[Global]].[[Global State-K Quai|K Quai]]

