## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
end

subgraph X13["Simulation Wiring"]
direction TB
subgraph X2["Price Movements Wiring"]
direction TB
X1["Placeholder"]
end
subgraph X4["Exchanges Wiring"]
direction TB
X3["Placeholder"]
end
subgraph X12["Mine Block Wiring"]
direction TB
X5["Mine Block Boundary Action"]
X6["Block Reward Policy"]
X7["Mining Payment Policy"]
subgraph X11["Mining Mechanisms"]
direction TB
X8["Placeholder"]
X9[Domain]

direction LR
direction TB
X9 --> X8
end
X5--"Block Difficulty Space"--->X6
X6--"Block Reward Options Space"--->X7
X7--->X11
end
X2--->X4
X4--->X12
end
```

## Description

Block Type: Stack Block
The wiring of the entire simulation
## Components
1. [[Price Movements Wiring]]
2. [[Exchanges Wiring]]
3. [[Mine Block Wiring]]

## All Blocks
1. [[Block Reward Policy]]
2. [[Mine Block Boundary Action]]
3. [[Mining Payment Policy]]
4. [[Placeholder]]

## Constraints

## Domain Spaces

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Block Difficulty Space]]
2. [[Block Reward Options Space]]
3. [[Empty Space]]

## Parameters Used

## Called By

## Calls

## All State Updates

