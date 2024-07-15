## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
end

subgraph X11["Simulation Wiring"]
direction TB
subgraph X2["Price Movements Wiring"]
direction TB
X1["Placeholder"]
end
subgraph X4["Exchanges Wiring"]
direction TB
X3["Placeholder"]
end
subgraph X6["Mine Block Wiring"]
direction TB
X5["Block Reward Policy"]
end
subgraph X8["Controller Update Wiring"]
direction TB
X7["Placeholder"]
end
subgraph X10["Log Simulation Wiring"]
direction TB
X9["Placeholder"]
end
X2--->X4
X4--->X6
X6--->X8
X8--->X10
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
2. [[Placeholder]]

## Constraints

## Domain Spaces

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Empty Space]]

## Parameters Used

## Called By

## Calls

## All State Updates

