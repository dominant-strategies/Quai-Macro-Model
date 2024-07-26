# Mathematical Specification V0 Presentation

## Executive Summary

- The mathematical specification presented here serves as the foundation for the following:
    - Documentation of simulation model architecture
    - An engine that allows for binding code to the blocks to test wirings in pieces before full model deployment
    - The precursor to a full simulation model
- Implementation of these wirings in code can be done in very little time now as the inputs/outputs/logics are all defined out nicely
- The boundary actions, control actions, and policies all have an attribute for their "options" which are specific implementations; the component defines the abstract block while the options describe specific implementations
    - What this means is that we have modularity here to both overwrite different implementations and conduct A/B testing (for example, the legacy model controllers are present as a benchmarking tool)

## Introduction to the Mathematical Specification Mapping Library

- The mathematical specification mapping library is documented [here](https://github.com/BlockScience/MSML/blob/main/README.md). This specification is completely built using its technology.

## Worked Example: Conversions Wiring

- Opened in Obsidian, the conversions wiring is one example of a wiring in the model that can be interactively probed
- We can see how the boundary action sets up the user behaviors, the policy maps the logic of a conversion, and the mechanisms illustrate what state variables are updated as an outcome of the policy

## High Level Wiring Overview

- The architecture of the simulation will be for the following wirings to be run sequentially N times to simulate a given time period:
    - **Price Movements Wiring**: The actions which shift the prices of both Qi and Quai, in dollar terms, on secondary markets
    - **Conversions Wiring**: Any conversions that might take place given the current pricing
    - **Mine Block Wiring**: All logics about one single prime block being mined and the effects of it
    - **Controller Update Wiring**: The updates that the controller initiates based on the both the recent wirings and historical state variables
    - **Log Simulation Data Mechanism**: A meta block which is only related to the simulation apparatus/saves the simulation data that is relevant, allowing for computational efficiency
- Now, let's view them in Obsidian...

## Outstanding Questions

- Are there any recommendations for how to model the block difficulty and mining time?
    - Current idea would be, for model parsimony, to derive a simple heuristic of the relationship between the two and model mining time as a stochastic process.
        - Implementing the full logic of difficulty adjustment is possible, but given the focus on the controller and exchanges this seems more prudent (but would allow for modularity to upgrade this component later in the model)
    - Are there any empirical datasets for Quai which has if we wanted to run back of the envelope statistics?
    - Are any other proof-of-work models good representations?
        - Is constant block time the goal also?
- For the conversions wiring, do we expect there to be any sort of fee, slippage, etc. charged on it?

## Discussion

- Time held to explore any other pieces of the spec or talk through any questions from the Quai team