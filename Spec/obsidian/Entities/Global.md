## Notes

## State
### Notes

### Variable Table
| Name | Description | Type | Symbol | Domain |
| --- | --- | --- | --- | --- |
|[[Global State-Dummy\|Dummy]]|The dummy entity|[[Entity Type]]|||
|[[Global State-Qi Supply\|Qi Supply]]|The total supply of Qi|[[Qi Type]]|||
|[[Global State-Quai Supply\|Quai Supply]]|The total supply of Quai|[[Quai Type]]|||
|[[Global State-Locked Qi Supply\|Locked Qi Supply]]|The total supply of Qi that is locked|[[Qi Type]]|||
|[[Global State-Locked Quai Supply\|Locked Quai Supply]]|The total supply of Quai that is locked|[[Quai Type]]|||
|[[Global State-Block Number\|Block Number]]|The current block that the system is on|[[Block Number Type]]|||
|[[Global State-Block Difficulty\|Block Difficulty]]|The latest difficulty for blocks|[[Block Difficulty Type]]|||
|[[Global State-Historical Converted Qi\|Historical Converted Qi]]|An array of the conversions from Qi to Quai. The Qi Values will be negative in each entry and Quai values will be positive. Time is also logged in the entries of the array.|[[Conversions Array Type]]|||
|[[Global State-Historical Converted Quai\|Historical Converted Quai]]|An array of the conversions from Quai to Qi. The Quai Values will be negative in each entry and Qi values will be positive. Time is also logged in the entries of the array.|[[Conversions Array Type]]|||
|[[Global State-Historical Mined Ratio\|Historical Mined Ratio]]|An array of the historical ratios of mining between Qi and Quai which the miners had chosen at given times.|[[Mined Ratio Array Type]]|||
|[[Global State-Historical Qi Hash\|Historical Qi Hash]]|An array of the historical amount of hash attributed to Qi in block rewards with block numbers attatched to each entry.|[[Hash Array Type]]|||
|[[Global State-Historical Quai Hash\|Historical Quai Hash]]|An array of the historical amount of hash attributed to Quai in block rewards with block numbers attatched to each entry.|[[Hash Array Type]]|||
|[[Global State-K Qi\|K Qi]]|The controller coeffecient for Qi.|[[Gain Type]]|||
|[[Global State-K Quai\|K Quai]]|The controller coeffecient for Quai.|[[Gain Type]]|||
|[[Global State-Quai Price\|Quai Price]]|The current price of Quai.|[[USD Type]]|||
|[[Global State-Qi Price\|Qi Price]]|The current price of Qi.|[[USD Type]]|||
|[[Global State-Simulation History Log\|Simulation History Log]]|The logged data from simulation history.|[[Simulation History Log Type]]|||
|[[Global State-Number of Regions\|Number of Regions]]|The current number of regions.|[[Number of Regions Type]]|||
|[[Global State-Zones per Region\|Zones per Region]]|The current number of zones in each region.|[[Zones per Region Type]]|||
|[[Global State-Time\|Time]]|The current time in the system.|[[Datetime Type]]|||
|[[Global State-Delta Time\|Delta Time]]|The amount of time covered in the current simulation epoch.|[[Delta Time Type]]|||


## Boundary Actions
## Mechanisms Impacting the Entity
### [[Increment Block Number Mechanism]]
### [[Update Historical Mined Ratio Mechanism]]
### [[Update Historical Qi Hash Mechanism]]
### [[Update Historical Quai Hash Mechanism]]
### [[Update Historical Converted Qi Mechanism]]
### [[Update Historical Converted Quai Mechanism]]
### [[Log Simulation Data Mechanism]]
### [[Mint Qi Tokens Mechanism]]
### [[Mint Quai Tokens Mechanism]]
### [[Burn Qi Tokens Mechanism]]
### [[Burn Quai Tokens Mechanism]]
### [[Update Prices Mechanism]]
### [[Update Prices Mechanism]]
### [[Set K Mechanism]]
### [[Set K Mechanism]]
## Actions Impacting the Entity
### [[Mine Block Boundary Action]]
### [[Conversions Boundary Action]]
### [[Price Movements Boundary Action]]
### [[Controller Update Control Action]]
