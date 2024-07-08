## Gameplan

- Sean to take [[Source Processing List]] and begin to build out the MSML scaffold / do due diligence
- Michael to write in markdown files, lucidchart, etc. thoughts that can be added either as links or artifacts to the repository
- Focus on economic instead of technical elements
- It may be worth it to touch up the lucidchart of the modeling flow

## Considerations
- We will need to define out the metrics used, i.e. how we measure volatility
- We need to figure out priorities are between:
	- Having the exchange between [[Quai Type|Quai]] and [[Qi Type|Qi]] be stable / close to the theoretical "no arbitrage price"
	- Have stability in price movements, i.e. low standard deviation in either price returns or log price returns
	- Have stability against energy as a benchmark (likely difficult because it requires an assumption on appropriate benchmarking of electricity prices)
- [[Controller Observability Stateful Metric|Controller Observability]] is going to be crucial to accurately define
- What is the appropriate time scale for the simulation?
- The timescale of the simulation likely will depend on the actuation frequency of the [[controller]]