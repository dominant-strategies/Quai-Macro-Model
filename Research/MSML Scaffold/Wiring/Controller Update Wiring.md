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

subgraph X8["Controller Update Wiring"]
direction TB
X1["Beta Estimation Policy"]
X2["Controller Update Policy"]
subgraph X7["Controller Mechanisms"]
direction TB
X3["Set K Mechanism"]
X3 --> EES2
X3 --> EES1
X4["Set Estimated Beta Vector Mechanism"]
X4 --> EES0
X5[Domain]

direction LR
direction TB
X5 --"K Space"--> X3
X5 --"Beta Vector Space"--> X4
end
X1--"Mined Blocks Space 2
Beta Vector Space"---->X2
X2--"K Space
Beta Vector Space"---->X7
end
```

## Description

Block Type: Stack Block
The wiring for the controller actions
## Components
1. [[Beta Estimation Policy]]
2. [[Controller Update Policy]]
3. [[Controller Mechanisms]]

## All Blocks
1. [[Beta Estimation Policy]]
2. [[Controller Update Policy]]
3. [[Set Estimated Beta Vector Mechanism]]
4. [[Set K Mechanism]]

## Constraints

## Domain Spaces
1. [[Mined Blocks Space 2]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Beta Vector Space]]
2. [[Empty Space]]
3. [[K Space]]
4. [[Mined Blocks Space 2]]
5. [[Terminating Space]]

## Parameters Used
1. [[Controller Alpha Parameter]]
2. [[Initial Block Difficulty]]
3. [[PID Parameterization]]
4. [[State Update Skipping Parameter]]

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Estimated Mining Beta Vector|Estimated Mining Beta Vector]]
2. [[Global]].[[Global State-K Qi|K Qi]]
3. [[Global]].[[Global State-K Quai|K Quai]]

