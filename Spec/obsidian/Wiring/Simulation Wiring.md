## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Dummy")]
EE1[("Global")]
EES0(["Total Length"])
EES0 --- EE0
EES1(["Words"])
EES1 --- EE0
EES2(["Block Number"])
EES2 --- EE1
EES3(["Historical Mined Ratio"])
EES3 --- EE1
EES4(["Historical Qi Hash"])
EES4 --- EE1
end

subgraph X22["Simulation Wiring"]
direction TB
subgraph X2["Price Movements Wiring"]
direction TB
X1["Placeholder"]
end
subgraph X4["Exchanges Wiring"]
direction TB
X3["Placeholder"]
end
subgraph X17["Mine Block Wiring"]
direction TB
X5["Mine Block Boundary Action"]
X6["Block Reward Policy"]
X7["Mining Payment Policy"]
subgraph X16["Mining Mechanisms"]
direction TB
X8["Increment Block Number Mechanism"]
X8 --> EES2
X9["Mint Qi Tokens Mechanism"]
X9 --> EES1
X9 --> EES0
X10["Mint Quai Tokens Mechanism"]
X10 --> EES1
X10 --> EES0
X11["Update Historical Mined Ratio Mechanism"]
X11 --> EES3
X12["Update Historical Qi Hash Mechanism"]
X12 --> EES4
X13["Update Historical Quai Hash Mechanism"]
X13 --> EES4
X14[Domain]

direction LR
direction TB
X14 --> X8
X14 --> X9
X14 --> X10
X14 --> X11
X14 --> X12
X14 --> X13
end
X5--"Block Difficulty Space"--->X6
X6--"Block Reward Options Space"--->X7
X7--->X16
end
subgraph X19["Controller Update Wiring"]
direction TB
X18["Placeholder"]
end
subgraph X21["Log Simulation Wiring"]
direction TB
X20["Placeholder"]
end
X2--->X4
X4--->X17
X17--->X19
X19--->X21
end
```

## Description

Block Type: Stack Block
The wiring of the entire simulation
## Components
1. [[Price Movements Wiring]]
2. [[Exchanges Wiring]]
3. [[Mine Block Wiring]]
4. [[Controller Update Wiring]]
5. [[Log Simulation Wiring]]

## All Blocks
1. [[Block Reward Policy]]
2. [[Increment Block Number Mechanism]]
3. [[Mine Block Boundary Action]]
4. [[Mining Payment Policy]]
5. [[Mint Qi Tokens Mechanism]]
6. [[Mint Quai Tokens Mechanism]]
7. [[Placeholder]]
8. [[Update Historical Mined Ratio Mechanism]]
9. [[Update Historical Qi Hash Mechanism]]
10. [[Update Historical Quai Hash Mechanism]]

## Constraints

## Domain Spaces

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Block Difficulty Space]]
2. [[Block Reward Options Space]]
3. [[Empty Space]]
4. [[Terminating Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Dummy]].[[Dummy State-Total Length|Total Length]]
2. [[Dummy]].[[Dummy State-Words|Words]]
3. [[Global]].[[Global State-Block Number|Block Number]]
4. [[Global]].[[Global State-Historical Mined Ratio|Historical Mined Ratio]]
5. [[Global]].[[Global State-Historical Qi Hash|Historical Qi Hash]]

