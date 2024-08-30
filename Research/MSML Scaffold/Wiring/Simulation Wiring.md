## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Block Number"])
EES0 --- EE0
EES1(["Estimated Mining Beta Vector"])
EES1 --- EE0
EES2(["Historical Converted Qi"])
EES2 --- EE0
EES3(["Historical Converted Quai"])
EES3 --- EE0
EES4(["Historical Mined Ratio"])
EES4 --- EE0
EES5(["Historical Qi Hash"])
EES5 --- EE0
EES6(["K Qi"])
EES6 --- EE0
EES7(["K Quai"])
EES7 --- EE0
EES8(["Locked Qi Supply"])
EES8 --- EE0
EES9(["Locked Quai Supply"])
EES9 --- EE0
EES10(["Mining Log"])
EES10 --- EE0
EES11(["Qi Price"])
EES11 --- EE0
EES12(["Qi Supply"])
EES12 --- EE0
EES13(["Qi Unlock Schedule"])
EES13 --- EE0
EES14(["Quai Price"])
EES14 --- EE0
EES15(["Quai Supply"])
EES15 --- EE0
EES16(["Quai Unlock Schedule"])
EES16 --- EE0
EES17(["Simulation History Log"])
EES17 --- EE0
EES18(["Time"])
EES18 --- EE0
end

subgraph X56["Simulation Wiring"]
direction TB
subgraph X4["Price Movements Wiring"]
direction TB
X1["Price Movements Boundary Action"]
X2["Price Movements Policy"]
X3["Update Prices Mechanism"]
X3 --> EES14
X3 --> EES11
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
X7 --> EES12
X8["Mint Quai Tokens Mechanism"]
X8 --> EES15
X9["Burn Qi Tokens Mechanism"]
X9 --> EES12
X10["Burn Quai Tokens Mechanism"]
X10 --> EES15
X11["Update Historical Converted Qi Mechanism"]
X11 --> EES2
X12["Update Historical Converted Quai Mechanism"]
X12 --> EES3
X13["Update Locked Qi Mechanism"]
X13 --> EES8
X14["Update Locked Quai Mechanism"]
X14 --> EES8
X15["Append to Unlock Schedule Mechanism"]
X15 --> EES16
X15 --> EES13
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
subgraph X50["Mine Block Wiring"]
direction TB
X20["Mine Block Boundary Action"]
X21["Mining Policy"]
X22["Block Reward Policy"]
X23["Mining Payment Policy"]
subgraph X35["Mezzanine Mining Wiring"]
direction TB
subgraph X31["Controller Update Wiring"]
direction TB
X24["Beta Estimation Policy"]
X25["Controller Update Policy"]
subgraph X30["Controller Mechanisms"]
direction TB
X26["Set K Mechanism"]
X26 --> EES7
X26 --> EES6
X27["Set Estimated Beta Vector Mechanism"]
X27 --> EES1
X28[Domain]

direction LR
direction TB
X28 --"K Space"--> X26
X28 --"Beta Vector Space"--> X27
end
X24--"Mined Blocks Space 2
Beta Vector Space"---->X25
X25--"K Space
Beta Vector Space"---->X30
end
X32["Mezzanine Wiring Passthrough"]
X33[Domain]
X34[Codomain]
direction LR
direction TB
X33 --"Mined Blocks Space 2"--> X31
X33 --"Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space
Qi Space
Quai Space
Unlock Schedule Entry Space
Mined Blocks Space 2
Mined Blocks Space 2"-----------> X32
X32 --"Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space
Qi Space
Quai Space
Unlock Schedule Entry Space
Mined Blocks Space 2
Mined Blocks Space 2"--> X34
end
subgraph X49["Mining Mechanisms"]
direction TB
X36["Increment Block Number Mechanism"]
X36 --> EES0
X37["Mint Qi Tokens Mechanism"]
X37 --> EES12
X38["Mint Quai Tokens Mechanism"]
X38 --> EES15
X39["Update Historical Mined Ratio Mechanism"]
X39 --> EES4
X40["Update Historical Qi Hash Mechanism"]
X40 --> EES5
X41["Update Historical Quai Hash Mechanism"]
X41 --> EES5
X42["Update Locked Qi Mechanism"]
X42 --> EES8
X43["Update Locked Quai Mechanism"]
X43 --> EES8
X44["Append to Unlock Schedule Mechanism"]
X44 --> EES16
X44 --> EES13
X45["Increment Time Mechanism"]
X45 --> EES18
X46["Log Mined Blocks Mechanism"]
X46 --> EES10
X47[Domain]

direction LR
direction TB
X47 --> X36
X47 --"Qi Space"--> X37
X47 --"Quai Space"--> X38
X47 --"Mined Ratio Space"--> X39
X47 --"Qi Hash Space"--> X40
X47 --"Quai Hash Space"--> X41
X47 --"Qi Space"--> X42
X47 --"Quai Space"--> X43
X47 --"Unlock Schedule Entry Space"--> X44
X47 --"Mined Blocks Space 2"--> X45
X47 --"Mined Blocks Space 2"--> X46
end
X20--"Pre-Mining Space"--->X21
X21--"Mined Blocks Space"--->X22
X22--"Block Reward Options Space"--->X23
X23--"Mined Blocks Space 2
Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space
Qi Space
Quai Space
Unlock Schedule Entry Space
Mined Blocks Space 2
Mined Blocks Space 2"------------->X35
X35--"Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space
Qi Space
Quai Space
Unlock Schedule Entry Space
Mined Blocks Space 2
Mined Blocks Space 2"------------>X49
end
subgraph X54["Unlock Tokens Wiring"]
direction TB
X51["Unlock Tokens Control Action"]
X52["Unlock Tokens Policy"]
X53["Unlock Tokens Mechanism"]
X53 --> EES9
X53 --> EES8
X53 --> EES16
X53 --> EES13
X51--->X52
X52--"Unlock Tokens Space"--->X53
end
X55["Log Simulation Data Mechanism"]
X55 --> EES17
X4--->X19
X19--->X50
X50--->X54
X54--->X55
end
```

## Description

Block Type: Stack Block
The wiring of the entire simulation
## Components
1. [[Price Movements Wiring]]
2. [[Conversions Wiring]]
3. [[Mine Block Wiring]]
4. [[Unlock Tokens Wiring]]
5. [[Log Simulation Data Mechanism]]

## All Blocks
1. [[Append to Unlock Schedule Mechanism]]
2. [[Beta Estimation Policy]]
3. [[Block Reward Policy]]
4. [[Burn Qi Tokens Mechanism]]
5. [[Burn Quai Tokens Mechanism]]
6. [[Controller Update Policy]]
7. [[Conversions Boundary Action]]
8. [[Conversions Policy]]
9. [[Increment Block Number Mechanism]]
10. [[Increment Time Mechanism]]
11. [[Log Mined Blocks Mechanism]]
12. [[Log Simulation Data Mechanism]]
13. [[Mezzanine Wiring Passthrough]]
14. [[Mine Block Boundary Action]]
15. [[Mining Payment Policy]]
16. [[Mining Policy]]
17. [[Mint Qi Tokens Mechanism]]
18. [[Mint Quai Tokens Mechanism]]
19. [[Price Movements Boundary Action]]
20. [[Price Movements Policy]]
21. [[Set Estimated Beta Vector Mechanism]]
22. [[Set K Mechanism]]
23. [[Unlock Tokens Control Action]]
24. [[Unlock Tokens Mechanism]]
25. [[Unlock Tokens Policy]]
26. [[Update Historical Converted Qi Mechanism]]
27. [[Update Historical Converted Quai Mechanism]]
28. [[Update Historical Mined Ratio Mechanism]]
29. [[Update Historical Qi Hash Mechanism]]
30. [[Update Historical Quai Hash Mechanism]]
31. [[Update Locked Qi Mechanism]]
32. [[Update Locked Quai Mechanism]]
33. [[Update Prices Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Terminating Space]]

## All Spaces Used
1. [[Beta Vector Space]]
2. [[Block Reward Options Space]]
3. [[Conversion Log Space]]
4. [[Conversion Space]]
5. [[Empty Space]]
6. [[K Space]]
7. [[Mined Blocks Space]]
8. [[Mined Blocks Space 2]]
9. [[Mined Ratio Space]]
10. [[Pre-Mining Space]]
11. [[Price Movement Space]]
12. [[Price Space]]
13. [[Qi Hash Space]]
14. [[Qi Space]]
15. [[Quai Hash Space]]
16. [[Quai Space]]
17. [[Terminating Space]]
18. [[Unlock Schedule Entry Space]]
19. [[Unlock Tokens Space]]

## Parameters Used
1. [[Aggregate Hashpower Series]]
2. [[Asset Return Parameterization]]
3. [[Controller Alpha Parameter]]
4. [[Conversion Percentage Mu]]
5. [[Conversion Percentage Sigma]]
6. [[Difficulty Randomness Mu]]
7. [[Difficulty Randomness Sigma]]
8. [[Hashpower Cost Series]]
9. [[Initial Block Difficulty]]
10. [[Lockup Options]]
11. [[Minimum Qi Conversion Amount]]
12. [[Minimum Quai Conversion Amount]]
13. [[PID Parameterization]]
14. [[Price EWMA Lambda]]
15. [[Qi Price Movemement Sigma]]
16. [[Quai Price Movemement Sigma]]
17. [[Quai Reward Base Parameter]]
18. [[Speculator Percentage]]

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Block Number|Block Number]]
2. [[Global]].[[Global State-Estimated Mining Beta Vector|Estimated Mining Beta Vector]]
3. [[Global]].[[Global State-Historical Converted Qi|Historical Converted Qi]]
4. [[Global]].[[Global State-Historical Converted Quai|Historical Converted Quai]]
5. [[Global]].[[Global State-Historical Mined Ratio|Historical Mined Ratio]]
6. [[Global]].[[Global State-Historical Qi Hash|Historical Qi Hash]]
7. [[Global]].[[Global State-K Qi|K Qi]]
8. [[Global]].[[Global State-K Quai|K Quai]]
9. [[Global]].[[Global State-Locked Qi Supply|Locked Qi Supply]]
10. [[Global]].[[Global State-Locked Quai Supply|Locked Quai Supply]]
11. [[Global]].[[Global State-Mining Log|Mining Log]]
12. [[Global]].[[Global State-Qi Price|Qi Price]]
13. [[Global]].[[Global State-Qi Supply|Qi Supply]]
14. [[Global]].[[Global State-Qi Unlock Schedule|Qi Unlock Schedule]]
15. [[Global]].[[Global State-Quai Price|Quai Price]]
16. [[Global]].[[Global State-Quai Supply|Quai Supply]]
17. [[Global]].[[Global State-Quai Unlock Schedule|Quai Unlock Schedule]]
18. [[Global]].[[Global State-Simulation History Log|Simulation History Log]]
19. [[Global]].[[Global State-Time|Time]]

