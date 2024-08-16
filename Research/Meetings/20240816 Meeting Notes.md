# 8/16/2024 Meeting Notes

## Notes

- With locking we need to figure out what the preferred rates are, the users converting/mining will be offered all of them as options
- There will be a certain amount of supply in the system that is speculative, and we should understand how that changes with more supply
- Effects of lockup vs. reward
    - Certain risk, FEVs, volatility risk between $ and Quai
- Control Surfaces:
    - Setting K Quai/K Qi
    - Lockup table options
    - Predicting price outcomes in the future and using that in the controller (but noted that it is very complex/behavioral based and would not make sense for a first model likely)
- Initial Allocation:
    - Unforced and forced functions can be useful
    - Shocks in vesting
- Quai views hash in the same way that there is a dollar valuation
- For mining, there should be samples that overall converge to similar difficulties
- The conversions would happen with prices from prior epoch but be included in current epoch
- Quickly scribbled notes that might be incorrect or incorrectly written, disregard grammar issues:
    - A prime block is also zone and region block
    - We can try to only think about prime blocks
    - The important thing is knowing the sub-samples and having that correct number
    - Time value ->
        - 2 shards -> Time delay of 2 for region, 2 for regions to prime
    - In the time to take 4 zone blocks you would find prime
    - Time scales:
        - 3x3 -> 81 subsamples
        - 2x2 -> 16 subsamples
    - Target time should scale with network size
    - Meant to avoid too much block contention
    - Target time is a linear DAA, 2 hours, continious distribution with no dead zones over 100 blocks


## Simulation Model Take-aways & Next Steps

### Initial Allocation

- Quai does have a strong preference towards having them in
- Likely best I just do some linear vesting module with the other unlocking pieces
- Plan on initial allocations is to just add the linear vesting and wrap it into the meta block, just want to confirm before I head down that path its fine, I know Z talked about forced vs. unforced functions and shocks but I think implementation of the vesting schedule for initial allocations like this should be pretty cut and dry.

### Fees

- We are good to go on either constant or distributional returns
- Plan would be to lock in simple constant fees for now

### Reward Metrics

- Put them both as multiplied in as linearly instead of dividing

### Unlocking/Locking

- Integrate in with the locking schedule options as a parameter

### USD Pricing

- Simple distributional model for changes in price over time
- Sean to come up with some baseline distribution parameter that is similar to capital asset pricing model where there is the 'market' factor that both Quai/Qi are correlated to and the idiosyncratic factors of their own distributions of return

### Mining

- It sounds like hash can be scaled as a distribution * a scaling factor for network size
- Subsample table we are going to need to dig in more, might be getting something from them?
- Need to define out how target time scales with network (linear to number of subsamples most likely?)
- Need to get the linear DAA and modify some of block to be over a 100 block timeframe for difficulty adjustment
- Tentative gameplan:
    - Sean write out sample model
    - Quickly get eyes on it from Jamsheed/Z?
    - Dr. K offered to check out/help so maybe send over to him after we feel confident to get a final sign off on validity of our abstraction?
    - Integrate into model