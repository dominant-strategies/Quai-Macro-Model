## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Block Number"])
EES0 --- EE0
EES1(["Estimated Mining Beta Vector"])
EES1 --- EE0
EES2(["Historical Mined Ratio"])
EES2 --- EE0
EES3(["Historical Qi Hash"])
EES3 --- EE0
EES4(["K Qi"])
EES4 --- EE0
EES5(["K Quai"])
EES5 --- EE0
EES6(["Locked Qi Supply"])
EES6 --- EE0
EES7(["Mining Log"])
EES7 --- EE0
EES8(["Qi Supply"])
EES8 --- EE0
EES9(["Qi Unlock Schedule"])
EES9 --- EE0
EES10(["Quai Supply"])
EES10 --- EE0
EES11(["Quai Unlock Schedule"])
EES11 --- EE0
EES12(["Time"])
EES12 --- EE0
end

subgraph X31["Mine Block Wiring"]
direction TB
X1["Mine Block Boundary Action"]
X2["Mining Policy"]
X3["Block Reward Policy"]
X4["Mining Payment Policy"]
subgraph X16["Mezzanine Mining Wiring"]
direction TB
subgraph X12["Controller Update Wiring"]
direction TB
X5["Beta Estimation Policy"]
X6["Controller Update Policy"]
subgraph X11["Controller Mechanisms"]
direction TB
X7["Set K Mechanism"]
X7 --> EES5
X7 --> EES4
X8["Set Estimated Beta Vector Mechanism"]
X8 --> EES1
X9[Domain]

direction LR
direction TB
X9 --"K Space"--> X7
X9 --"Beta Vector Space"--> X8
end
X5--"Mined Blocks Space 2
Beta Vector Space"---->X6
X6--"K Space
Beta Vector Space"---->X11
end
X13["Mezzanine Wiring Passthrough"]
X14[Domain]
X15[Codomain]
direction LR
direction TB
X14 --"Mined Blocks Space 2"--> X12
X14 --"Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space
Qi Space
Quai Space
Unlock Schedule Entry Space
Mined Blocks Space 2
Mined Blocks Space 2"-----------> X13
X13 --"Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space
Qi Space
Quai Space
Unlock Schedule Entry Space
Mined Blocks Space 2
Mined Blocks Space 2"--> X15
end
subgraph X30["Mining Mechanisms"]
direction TB
X17["Increment Block Number Mechanism"]
X17 --> EES0
X18["Mint Qi Tokens Mechanism"]
X18 --> EES8
X19["Mint Quai Tokens Mechanism"]
X19 --> EES10
X20["Update Historical Mined Ratio Mechanism"]
X20 --> EES2
X21["Update Historical Qi Hash Mechanism"]
X21 --> EES3
X22["Update Historical Quai Hash Mechanism"]
X22 --> EES3
X23["Update Locked Qi Mechanism"]
X23 --> EES6
X24["Update Locked Quai Mechanism"]
X24 --> EES6
X25["Append to Unlock Schedule Mechanism"]
X25 --> EES11
X25 --> EES9
X26["Increment Time Mechanism"]
X26 --> EES12
X27["Log Mined Blocks Mechanism"]
X27 --> EES7
X28[Domain]

direction LR
direction TB
X28 --> X17
X28 --"Qi Space"--> X18
X28 --"Quai Space"--> X19
X28 --"Mined Ratio Space"--> X20
X28 --"Qi Hash Space"--> X21
X28 --"Quai Hash Space"--> X22
X28 --"Qi Space"--> X23
X28 --"Quai Space"--> X24
X28 --"Unlock Schedule Entry Space"--> X25
X28 --"Mined Blocks Space 2"--> X26
X28 --"Mined Blocks Space 2"--> X27
end
X1--"Pre-Mining Space"--->X2
X2--"Mined Blocks Space"--->X3
X3--"Block Reward Options Space"--->X4
X4--"Mined Blocks Space 2
Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space
Qi Space
Quai Space
Unlock Schedule Entry Space
Mined Blocks Space 2
Mined Blocks Space 2"------------->X16
X16--"Qi Space
Quai Space
Mined Ratio Space
Qi Hash Space
Quai Hash Space
Qi Space
Quai Space
Unlock Schedule Entry Space
Mined Blocks Space 2
Mined Blocks Space 2"------------>X30
end
```

## Description

Block Type: Stack Block
"The wiring for mining a block.

For the decision between Qi and Quai, the idea is that there should be a Schelling point, if the miner is mining and Qi is an option, they will only look at Qi as making sense if the market price is above their production price.

If the demand for Qi is greater than the supply, there should be a profitable opportunity until market price approaches at which point amount of Qi is at equilibrium because the market price matches the production price.
## Components
1. [[Mine Block Boundary Action]]
2. [[Mining Policy]]
3. [[Block Reward Policy]]
4. [[Mining Payment Policy]]
5. [[Mezzanine Mining Wiring]]
6. [[Mining Mechanisms]]

## All Blocks
1. [[Append to Unlock Schedule Mechanism]]
2. [[Beta Estimation Policy]]
3. [[Block Reward Policy]]
4. [[Controller Update Policy]]
5. [[Increment Block Number Mechanism]]
6. [[Increment Time Mechanism]]
7. [[Log Mined Blocks Mechanism]]
8. [[Mezzanine Wiring Passthrough]]
9. [[Mine Block Boundary Action]]
10. [[Mining Payment Policy]]
11. [[Mining Policy]]
12. [[Mint Qi Tokens Mechanism]]
13. [[Mint Quai Tokens Mechanism]]
14. [[Set Estimated Beta Vector Mechanism]]
15. [[Set K Mechanism]]
16. [[Update Historical Mined Ratio Mechanism]]
17. [[Update Historical Qi Hash Mechanism]]
18. [[Update Historical Quai Hash Mechanism]]
19. [[Update Locked Qi Mechanism]]
20. [[Update Locked Quai Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Beta Vector Space]]
2. [[Block Reward Options Space]]
3. [[Empty Space]]
4. [[K Space]]
5. [[Mined Blocks Space]]
6. [[Mined Blocks Space 2]]
7. [[Mined Ratio Space]]
8. [[Pre-Mining Space]]
9. [[Qi Hash Space]]
10. [[Qi Space]]
11. [[Quai Hash Space]]
12. [[Quai Space]]
13. [[Terminating Space]]
14. [[Unlock Schedule Entry Space]]

## Parameters Used
1. [[Aggregate Hashpower Series]]
2. [[Controller Alpha Parameter]]
3. [[Difficulty Randomness Mu]]
4. [[Difficulty Randomness Sigma]]
5. [[Initial Block Difficulty]]
6. [[PID Parameterization]]
7. [[Quai Reward Base Parameter]]

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Block Number|Block Number]]
2. [[Global]].[[Global State-Estimated Mining Beta Vector|Estimated Mining Beta Vector]]
3. [[Global]].[[Global State-Historical Mined Ratio|Historical Mined Ratio]]
4. [[Global]].[[Global State-Historical Qi Hash|Historical Qi Hash]]
5. [[Global]].[[Global State-K Qi|K Qi]]
6. [[Global]].[[Global State-K Quai|K Quai]]
7. [[Global]].[[Global State-Locked Qi Supply|Locked Qi Supply]]
8. [[Global]].[[Global State-Mining Log|Mining Log]]
9. [[Global]].[[Global State-Qi Supply|Qi Supply]]
10. [[Global]].[[Global State-Qi Unlock Schedule|Qi Unlock Schedule]]
11. [[Global]].[[Global State-Quai Supply|Quai Supply]]
12. [[Global]].[[Global State-Quai Unlock Schedule|Quai Unlock Schedule]]
13. [[Global]].[[Global State-Time|Time]]

