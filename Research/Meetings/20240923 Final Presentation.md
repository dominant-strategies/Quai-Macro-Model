# V1 Quai Macro Model Final Presentation

## Recent Additions

- Documentation, README, general cleanup of the repository
- Previous asks on capping the conversion rate (note it does not cap the changes in KQi/KQuai but instead caps it when requesting a conversion)
- Updated all starting parameters and initial starting state with the working version of initial values
- Variable difficulty notebook for testing across a ramp up in the aggregate hashpower
- cadCAD implementation for when/if large scale simulations are wanted

## High Level Walk Through

- The high level information for the model is contained in the [README](https://github.com/BlockScience/Quai-Macro-Model/blob/main/README.md)

## Model Calibration through Feature Vectors

- The model can be enriched further by expanding the feature vector for mining probabilities as well as the beta estimator
- There are already two other working models of a feature vector in the behavioral side where one has the reward ratio as an additional feature and the other has the log of the reward ratio
- The two places that modifications might happen are:
    - On the behavioral aspects (or population beta model)
    - On the beta estimation side (which computes estimated betas)

## Variable Difficulty Notebook

## Potential Future Work Arcs

### Parameter Selection under Uncertainty

- The PSuU workflow takes a massive amount of monte carlo runs and draws both insights and recommendations of parameters through machine learning workflows
- There are two related concepts that can be tested: failure conditions and parameter optimization

#### Failure Conditions

- By defining success criteria, PSuU can be leveraged to determine under what conditions a system might fail
- By sweeping through a variety of edge cases in parameterizations and behaviors, the stability and robustness of economic systems can be tested

#### Parameter Optimization

- Leveraging the same or expanded success criteria, parameter optimization can be done to find the constellations of parameters that provide the highest likelihood of fulfilling success criteria
- Parameterizations are tested as constellations rather than individual components to ensure that any correlations or impacts that one might have on the other are captured 

### Unit & Integration Testing

- Because of how the wirings and components are set up, it can very easily be enhanced with tests to ensure the validity of the model after any iterations and updates
- Unit tests can be built up into integration tests by testing entire wirings against different conditions

### A/B Testing of Mechanism

- Given MSML's support of multiple policy/boundary action/etc. options, one can write out different potential implementations to talk through
- As well, each can be bound with code and by just switching the functional parameterizations (parameters with FP before them), the simulation will run with different implementations
- Multiple simulations can be set up to probe the effects of different policies and behavioral assumptions

### Digital Twin

- When a production system is launched, a digital twin model can be used to backtest the realized outcomes versus backtested outcomes as well as make future extrapolations
- Analytic dashboards and potentially even early warning systems can also be potentially designed


### Cloud Enabled Simulations

- For scaling of simulations, a custom cloud solution for running parallelized simulations can be built
- This allows for a massive number of simulations to be run in a short time