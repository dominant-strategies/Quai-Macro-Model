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
EES5(["Locked Qi Supply"])
EES5 --- EE0
EES6(["Qi Price"])
EES6 --- EE0
EES7(["Qi Supply"])
EES7 --- EE0
EES8(["Qi Unlock Schedule"])
EES8 --- EE0
EES9(["Quai Price"])
EES9 --- EE0
EES10(["Quai Supply"])
EES10 --- EE0
EES11(["Quai Unlock Schedule"])
EES11 --- EE0
EES12(["Simulation History Log"])
EES12 --- EE0
end

subgraph X35["Simulation Wiring"]
direction TB
subgraph X4["Price Movements Wiring"]
direction TB
X1["Price Movements Boundary Action"]
X2["Price Movements Policy"]
X3["Update Prices Mechanism"]
X3 --> EES9
X3 --> EES6
X1--"Price Movement Space"--->X2
X2--"Price Space"--->X3
end
subgraph X19["Conversions Wiring"]
direction TB
X5["Conversions Boundary Action"]
X6["Conversions Policy"]
subgraph X18["Conversions Mechanisms Wiring"]
direction TB
X7["Mint Qi Tokens Mechanism"]
X7 --> EES7
X8["Mint Quai Tokens Mechanism"]
X8 --> EES10
X9["Burn Qi Tokens Mechanism"]
X9 --> EES7
X10["Burn Quai Tokens Mechanism"]
X10 --> EES10
X11["Update Historical Converted Qi Mechanism"]
X11 --> EES1
X12["Update Historical Converted Quai Mechanism"]
X12 --> EES2
X13["Update Locked Qi Mechanism"]
X13 --> EES5
X14["Update Locked Quai Mechanism"]
X14 --> EES5
X15["Append to Unlock Schedule Mechanism"]
X15 --> EES11
X15 --> EES8
X16[Domain]

direction LR
direction TB
X16 --"Qi Space"--> X7
X16 --"Quai Space"--> X8
X16 --"Qi Space"--> X9
X16 --"Quai Space"--> X10
X16 --"Conversion Log Space"--> X11
X16 --"Conversion Log Space"--> X12
X16 --"Qi Space"--> X13
X16 --"Quai Space"--> X14
X16 --"Unlock Schedule Entry Space"--> X15
end
X5--"Conversion Space"--->X6
X6--"Qi Space
Quai Space
Qi Space
Quai Space
Conversion Log Space
Conversion Log Space
Qi Space
Quai Space
Unlock Schedule Entry Space"----------->X18
end
subgraph X33["Mine Block Wiring"]
direction TB
X20["Mine Block Boundary Action"]
X21["Mining Policy"]
X22["Block Reward Policy"]
X23["Mining Payment Policy"]
subgraph X32["Mining Mechanisms"]
direction TB
X24["Increment Block Number Mechanism"]
X24 --> EES0
X25["Mint Qi Tokens Mechanism"]
X25 --> EES7
X26["Mint Quai Tokens Mechanism"]
X26 --> EES10
X27["Update Historical Mined Ratio Mechanism"]
X27 --> EES3
X28["Update Historical Qi Hash Mechanism"]
X28 --> EES4
X29["Update Historical Quai Hash Mechanism"]
X29 --> EES4
X30[Domain]

direction LR
direction TB
X30 --> X24
X30 --"Qi Space"--> X25
X30 --"Quai Space"--> X26
X30 --"Mined Ratio Space"--> X27
X30 --"Qi Hash Space"--> X28
X30 --"Quai Hash Space"--> X29
end
X20--"Pre-Mining Space"--->X21
X21--"Mined Blocks Space"--->X22
X22--"Block Reward Options Space"--->X23
X23--"Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space"------->X32
end
X34["Log Simulation Data Mechanism"]
X34 --> EES12
X4--->X19
X19--->X33
X33--->X34
end
```

## Description

Block Type: Stack Block
The wiring of the entire simulation
## Components
1. [[Price Movements Wiring]]
2. [[Conversions Wiring]]
3. [[Mine Block Wiring]]
4. [[Log Simulation Data Mechanism]]

## All Blocks
1. [[Append to Unlock Schedule Mechanism]]
2. [[Block Reward Policy]]
3. [[Burn Qi Tokens Mechanism]]
4. [[Burn Quai Tokens Mechanism]]
5. [[Conversions Boundary Action]]
6. [[Conversions Policy]]
7. [[Increment Block Number Mechanism]]
8. [[Log Simulation Data Mechanism]]
9. [[Mine Block Boundary Action]]
10. [[Mining Payment Policy]]
11. [[Mining Policy]]
12. [[Mint Qi Tokens Mechanism]]
13. [[Mint Quai Tokens Mechanism]]
14. [[Price Movements Boundary Action]]
15. [[Price Movements Policy]]
16. [[Update Historical Converted Qi Mechanism]]
17. [[Update Historical Converted Quai Mechanism]]
18. [[Update Historical Mined Ratio Mechanism]]
19. [[Update Historical Qi Hash Mechanism]]
20. [[Update Historical Quai Hash Mechanism]]
21. [[Update Locked Qi Mechanism]]
22. [[Update Locked Quai Mechanism]]
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
5. [[Mined Blocks Space]]
6. [[Mined Ratio Space]]
7. [[Pre-Mining Space]]
8. [[Price Movement Space]]
9. [[Price Space]]
10. [[Qi Hash Space]]
11. [[Qi Space]]
12. [[Quai Hash Space]]
13. [[Quai Space]]
14. [[Terminating Space]]
15. [[Unlock Schedule Entry Space]]

## Parameters Used
1. [[Aggregate Hashpower Series]]
2. [[Asset Return Parameterization]]
3. [[Conversion Percentage Mu]]
4. [[Conversion Percentage Sigma]]
5. [[Hashpower Cost Series]]
6. [[Lockup Options]]
7. [[Minimum Qi Conversion Amount]]
8. [[Minimum Quai Conversion Amount]]
9. [[Price EWMA Lambda]]
10. [[Qi Price Movemement Sigma]]
11. [[Quai Price Movemement Sigma]]
12. [[Quai Reward Base Parameter]]
13. [[Speculator Percentage]]

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Block Number|Block Number]]
2. [[Global]].[[Global State-Historical Converted Qi|Historical Converted Qi]]
3. [[Global]].[[Global State-Historical Converted Quai|Historical Converted Quai]]
4. [[Global]].[[Global State-Historical Mined Ratio|Historical Mined Ratio]]
5. [[Global]].[[Global State-Historical Qi Hash|Historical Qi Hash]]
6. [[Global]].[[Global State-Locked Qi Supply|Locked Qi Supply]]
7. [[Global]].[[Global State-Qi Price|Qi Price]]
8. [[Global]].[[Global State-Qi Supply|Qi Supply]]
9. [[Global]].[[Global State-Qi Unlock Schedule|Qi Unlock Schedule]]
10. [[Global]].[[Global State-Quai Price|Quai Price]]
11. [[Global]].[[Global State-Quai Supply|Quai Supply]]
12. [[Global]].[[Global State-Quai Unlock Schedule|Quai Unlock Schedule]]
13. [[Global]].[[Global State-Simulation History Log|Simulation History Log]]

