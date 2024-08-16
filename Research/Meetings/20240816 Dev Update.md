# 8/16/2024 Dev Update

## Summary

- Progress has been made on finalizing the simulation apparatus, albeit we still need to finish the controller submodule before we can have the full simulation architecture. 
- There are 62 issues open in the github repo and 95 issues closed, but most of the 62 have been talked through and have a gameplan so the progress is actually further than 95 / (62 + 95), and not all issues are created the same anyways
- There are a lot of work in progress pieces but these will all come together in the very near future
- I will walk through all the high level updates and then we can spend time on any of the following:
    - More detailed walk-throughs of the current progress
    - Working through outstanding questions
    - Any discussion topics that are brought up

## Simulation Architecture V2

- The high level simulation architecture is mostly finalized with a few open questions, left to be addressed in the oustanding questions section
- As a reminder, these pieces can all be viewed in the Obsidian vault for documentation purposes but also are having code written to be bound to them for testing
- I will now to pan over to the Obsidian canvas to go through the current planned blocks for the simulation


## High Level Status Update - Implementations and Spec

1. Metrics (MSML component meaning the modularized functions taking state, parameters, and some input and mapping out values to be used across components): Most of the metrics are complete in both the specification as well as implemented in code bound to the specification
    - Quai/Qi reward rates are complete in spec and implementation
        - One outsanding issue is to remove the parameter that allowed for modifying $log_n(Difficulty)$ with hard coding to 2 (unless there is any possibility of wanting to have this as modular)
    - Conversion rate is implemented in code and spec
    - Loss function and controller metrics to be implemented soon
2. Prices Wiring: Currently completely done in the spec, and waiting implementation (but it is a very easy implementation) pending open question on whether or not we want/need external market prices
3. Conversions: V1 of spec and implementations done
    - The boundary action have an outstanding issue to determine the behavioral model of conversions and conversion size, currently there are just two test implementations for testing Quai/Qi conversions
    - Unlocking/locking still needs to be taken into account
4. Mining: Boundary action and policies complete in spec and code, mechanisms need to be potentially updated with locking/unlocking additions and some of the mining logic may need to be re-wired to correct abstraction model of mined blocks
    - The difficulty adjustment / how blocks might get mined in the abstraction may need to be revised; trying to strike the balance between abstraction and having all represented elements
    - Miner decision has a second option that needs to be implemented that will not use USD pricing but be in line with the current conversion rate
    - Mechanisms to be updated once finalization of locking/unlocking is done
5. Controller: Convering on finalized model but the spec currently has the rough scaffold of all blocks and the prior controllers from previous model as options
6. Meta Block: Simulation log implemented in spec but not code (should be easy but should be the last implementation once all final tweaks complete), unlocking should be straight forward but confirming a few final pieces of information
7. A lot of the starting simulation specific stuff such as state, parameters, etc. is ~80% complete and set up

## Current Implementation Notebooks

These notebooks display some of the current progress on implementations for alignment across everyone

1. Metrics Examples: Notebook comparing the current metrics and graphing the relations
2. Conversions Examples: Full split out component wirings of the conversions and spaces they pass for a test example with both Quai and Qi
3. Mining Examples: Mining completed from boundary action through policies with broken out printing of all spaces passed

## Outstanding Questions + Considerations

### Initial Allocation Vesting

1. Prefer to not include in this version of the model, but if we do need it, what impacts would we expect from the unvesting over time besides the obvious accounting updates? Does it impact prices?

### USD Prices

1. Do we have any feelings on whether or not we think USD prices are necessary?
    - They could be used an input into the behavioral model of aggregate hashpower where higher USD valuation correlates to more hashpower
    - But there might also be a case to cut from current version of the model

### Fees

1. Fees for conversions can be modularized so as to extend in the future, but are we ok with either a constant value fee and/or pulling fees from a distribution right now?

### Unlocking/Locking

1. How important is locking/unlocking here on macroeconomics? Hypothetically could be a place to cut for first version of the model but it sounds like we want it represented.
2. In the following table, is the miner and converter in both cases offered these 4 options of locking and they choose whatever suits them?

![alt text](lockup.png)