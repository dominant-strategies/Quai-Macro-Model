## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Block Number"])
EES0 --- EE0
EES1(["Historical Converted Qi"])
EES1 --- EE0
EES2(["Historical Converted Quai"])
EES2 --- EE0
EES3(["Historical Mined Ratio"])
EES3 --- EE0
EES4(["Historical Qi Hash"])
EES4 --- EE0
EES5(["K Qi"])
EES5 --- EE0
EES6(["K Quai"])
EES6 --- EE0
EES7(["Qi Supply"])
EES7 --- EE0
EES8(["Quai Supply"])
EES8 --- EE0
end

subgraph X35["Simulation Wiring"]
direction TB
subgraph X3["Price Movements Wiring"]
direction TB
X1["Price Movements Boundary Action"]
X2["Price Movements Policy"]
X1--"Price Movement Space"--->X2
end
subgraph X15["Conversions Wiring"]
direction TB
X4["Conversions Boundary Action"]
X5["Conversions Policy"]
subgraph X14["Conversions Mechanisms Wiring"]
direction TB
X6["Mint Qi Tokens Mechanism"]
X6 --> EES7
X7["Mint Quai Tokens Mechanism"]
X7 --> EES8
X8["Burn Qi Tokens Mechanism"]
X8 --> EES7
X9["Burn Quai Tokens Mechanism"]
X9 --> EES8
X10["Update Historical Converted Qi Mechanism"]
X10 --> EES1
X11["Update Historical Converted Quai Mechanism"]
X11 --> EES2
X12[Domain]

direction LR
direction TB
X12 --"Qi Space"--> X6
X12 --"Quai Space"--> X7
X12 --"Qi Space"--> X8
X12 --"Quai Space"--> X9
X12 --"Conversion Log Space"--> X10
X12 --"Conversion Log Space"--> X11
end
X4--"Conversion Space"--->X5
X5--"Qi Space
Quai Space
Qi Space
Quai Space
Conversion Log Space
Conversion Log Space"-------->X14
end
subgraph X28["Mine Block Wiring"]
direction TB
X16["Mine Block Boundary Action"]
X17["Block Reward Policy"]
X18["Mining Payment Policy"]
subgraph X27["Mining Mechanisms"]
direction TB
X19["Increment Block Number Mechanism"]
X19 --> EES0
X20["Mint Qi Tokens Mechanism"]
X20 --> EES7
X21["Mint Quai Tokens Mechanism"]
X21 --> EES8
X22["Update Historical Mined Ratio Mechanism"]
X22 --> EES3
X23["Update Historical Qi Hash Mechanism"]
X23 --> EES4
X24["Update Historical Quai Hash Mechanism"]
X24 --> EES4
X25[Domain]

direction LR
direction TB
X25 --> X19
X25 --"Qi Space"--> X20
X25 --"Quai Space"--> X21
X25 --"Mined Ratio Space"--> X22
X25 --"Qi Hash Space"--> X23
X25 --"Quai Hash Space"--> X24
end
X16--"Block Difficulty Space"--->X17
X17--"Block Reward Options Space"--->X18
X18--"Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space"------->X27
end
subgraph X32["Controller Update Wiring"]
direction TB
X29["Controller Update Control Action"]
X30["Controller Update Policy"]
X31["Set K Mechanism"]
X31 --> EES6
X31 --> EES5
X29--"Observable State Space"--->X30
X30--"K Space"--->X31
end
subgraph X34["Log Simulation Wiring"]
direction TB
X33["Placeholder"]
end
X3--->X15
X15--->X28
X28--->X32
X32--->X34
end
```

## Description

Block Type: Stack Block
The wiring of the entire simulation
## Components
1. [[Price Movements Wiring]]
2. [[Conversions Wiring]]
3. [[Mine Block Wiring]]
4. [[Controller Update Wiring]]
5. [[Log Simulation Wiring]]

## All Blocks
1. [[Block Reward Policy]]
2. [[Burn Qi Tokens Mechanism]]
3. [[Burn Quai Tokens Mechanism]]
4. [[Controller Update Control Action]]
5. [[Controller Update Policy]]
6. [[Conversions Boundary Action]]
7. [[Conversions Policy]]
8. [[Increment Block Number Mechanism]]
9. [[Mine Block Boundary Action]]
10. [[Mining Payment Policy]]
11. [[Mint Qi Tokens Mechanism]]
12. [[Mint Quai Tokens Mechanism]]
13. [[Placeholder]]
14. [[Price Movements Boundary Action]]
15. [[Price Movements Policy]]
16. [[Set K Mechanism]]
17. [[Update Historical Converted Qi Mechanism]]
18. [[Update Historical Converted Quai Mechanism]]
19. [[Update Historical Mined Ratio Mechanism]]
20. [[Update Historical Qi Hash Mechanism]]
21. [[Update Historical Quai Hash Mechanism]]

## Constraints

## Domain Spaces

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Block Difficulty Space]]
2. [[Block Reward Options Space]]
3. [[Conversion Log Space]]
4. [[Conversion Space]]
5. [[Empty Space]]
6. [[K Space]]
7. [[Mined Ratio Space]]
8. [[Observable State Space]]
9. [[Price Movement Space]]
10. [[Qi Hash Space]]
11. [[Qi Space]]
12. [[Quai Hash Space]]
13. [[Quai Space]]
14. [[Terminating Space]]

## Parameters Used
1. [[Asset Return Parameterization]]
2. [[Initial Block Difficulty]]
3. [[Minimum Qi Conversion Amount]]
4. [[Minimum Quai Conversion Amount]]
5. [[PID Parameterization]]

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Block Number|Block Number]]
2. [[Global]].[[Global State-Historical Converted Qi|Historical Converted Qi]]
3. [[Global]].[[Global State-Historical Converted Quai|Historical Converted Quai]]
4. [[Global]].[[Global State-Historical Mined Ratio|Historical Mined Ratio]]
5. [[Global]].[[Global State-Historical Qi Hash|Historical Qi Hash]]
6. [[Global]].[[Global State-K Qi|K Qi]]
7. [[Global]].[[Global State-K Quai|K Quai]]
8. [[Global]].[[Global State-Qi Supply|Qi Supply]]
9. [[Global]].[[Global State-Quai Supply|Quai Supply]]

