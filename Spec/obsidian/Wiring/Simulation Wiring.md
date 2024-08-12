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
EES7(["Qi Price"])
EES7 --- EE0
EES8(["Qi Supply"])
EES8 --- EE0
EES9(["Quai Price"])
EES9 --- EE0
EES10(["Quai Supply"])
EES10 --- EE0
EES11(["Simulation History Log"])
EES11 --- EE0
end

subgraph X36["Simulation Wiring"]
direction TB
subgraph X4["Price Movements Wiring"]
direction TB
X1["Price Movements Boundary Action"]
X2["Price Movements Policy"]
X3["Update Prices Mechanism"]
X3 --> EES9
X3 --> EES7
X1--"Price Movement Space"--->X2
X2--"Price Space"--->X3
end
subgraph X16["Conversions Wiring"]
direction TB
X5["Conversions Boundary Action"]
X6["Conversions Policy"]
subgraph X15["Conversions Mechanisms Wiring"]
direction TB
X7["Mint Qi Tokens Mechanism"]
X7 --> EES8
X8["Mint Quai Tokens Mechanism"]
X8 --> EES10
X9["Burn Qi Tokens Mechanism"]
X9 --> EES8
X10["Burn Quai Tokens Mechanism"]
X10 --> EES10
X11["Update Historical Converted Qi Mechanism"]
X11 --> EES1
X12["Update Historical Converted Quai Mechanism"]
X12 --> EES2
X13[Domain]

direction LR
direction TB
X13 --"Qi Space"--> X7
X13 --"Quai Space"--> X8
X13 --"Qi Space"--> X9
X13 --"Quai Space"--> X10
X13 --"Conversion Log Space"--> X11
X13 --"Conversion Log Space"--> X12
end
X5--"Conversion Space"--->X6
X6--"Qi Space
Quai Space
Qi Space
Quai Space
Conversion Log Space
Conversion Log Space"-------->X15
end
subgraph X30["Mine Block Wiring"]
direction TB
X17["Mine Block Boundary Action"]
X18["Mining Policy"]
X19["Block Reward Policy"]
X20["Mining Payment Policy"]
subgraph X29["Mining Mechanisms"]
direction TB
X21["Increment Block Number Mechanism"]
X21 --> EES0
X22["Mint Qi Tokens Mechanism"]
X22 --> EES8
X23["Mint Quai Tokens Mechanism"]
X23 --> EES10
X24["Update Historical Mined Ratio Mechanism"]
X24 --> EES3
X25["Update Historical Qi Hash Mechanism"]
X25 --> EES4
X26["Update Historical Quai Hash Mechanism"]
X26 --> EES4
X27[Domain]

direction LR
direction TB
X27 --> X21
X27 --"Qi Space"--> X22
X27 --"Quai Space"--> X23
X27 --"Mined Ratio Space"--> X24
X27 --"Qi Hash Space"--> X25
X27 --"Quai Hash Space"--> X26
end
X17--"Pre-Mining Space"--->X18
X18--"Mined Blocks Space"--->X19
X19--"Block Reward Options Space"--->X20
X20--"Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space"------->X29
end
subgraph X34["Controller Update Wiring"]
direction TB
X31["Controller Update Control Action"]
X32["Controller Update Policy"]
X33["Set K Mechanism"]
X33 --> EES6
X33 --> EES5
X31--"Observable State Space"--->X32
X32--"K Space"--->X33
end
X35["Log Simulation Data Mechanism"]
X35 --> EES11
X4--->X16
X16--->X30
X30--->X34
X34--->X35
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
5. [[Log Simulation Data Mechanism]]

## All Blocks
1. [[Block Reward Policy]]
2. [[Burn Qi Tokens Mechanism]]
3. [[Burn Quai Tokens Mechanism]]
4. [[Controller Update Control Action]]
5. [[Controller Update Policy]]
6. [[Conversions Boundary Action]]
7. [[Conversions Policy]]
8. [[Increment Block Number Mechanism]]
9. [[Log Simulation Data Mechanism]]
10. [[Mine Block Boundary Action]]
11. [[Mining Payment Policy]]
12. [[Mining Policy]]
13. [[Mint Qi Tokens Mechanism]]
14. [[Mint Quai Tokens Mechanism]]
15. [[Price Movements Boundary Action]]
16. [[Price Movements Policy]]
17. [[Set K Mechanism]]
18. [[Update Historical Converted Qi Mechanism]]
19. [[Update Historical Converted Quai Mechanism]]
20. [[Update Historical Mined Ratio Mechanism]]
21. [[Update Historical Qi Hash Mechanism]]
22. [[Update Historical Quai Hash Mechanism]]
23. [[Update Prices Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Terminating Space]]

## All Spaces Used
1. [[Block Reward Options Space]]
2. [[Conversion Log Space]]
3. [[Conversion Space]]
4. [[Empty Space]]
5. [[K Space]]
6. [[Mined Blocks Space]]
7. [[Mined Ratio Space]]
8. [[Observable State Space]]
9. [[Pre-Mining Space]]
10. [[Price Movement Space]]
11. [[Price Space]]
12. [[Qi Hash Space]]
13. [[Qi Space]]
14. [[Quai Hash Space]]
15. [[Quai Space]]
16. [[Terminating Space]]

## Parameters Used
1. [[Asset Return Parameterization]]
2. [[Initial Block Difficulty]]
3. [[Minimum Qi Conversion Amount]]
4. [[Minimum Quai Conversion Amount]]
5. [[PID Parameterization]]
6. [[Quai Reward Base Parameter]]

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
8. [[Global]].[[Global State-Qi Price|Qi Price]]
9. [[Global]].[[Global State-Qi Supply|Qi Supply]]
10. [[Global]].[[Global State-Quai Price|Quai Price]]
11. [[Global]].[[Global State-Quai Supply|Quai Supply]]
12. [[Global]].[[Global State-Simulation History Log|Simulation History Log]]

