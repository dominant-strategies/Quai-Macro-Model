# Quai Macro Model

The repository presented here is all the source code for the mathematical specification as well as model used to model the macroeconomics of the Quai ecosystem.

## MSML Background

Writing mathematical specifications can be a difficult process, especially when variable names are changed or new mechanisms are introduced. MSML seeks to streamline the process with automations as well as enhance the abilities of static math specs to deliver deeper insights. Because it is automated, one can write specifications at different levels of details or for different purposes.

More information on how the library works can be found [here](https://github.com/BlockScience/MSML).

## cadCAD Background

cadCAD is a Python package that assists in the processes of designing, testing and validating complex systems through simulation, with support for Monte Carlo methods, A/B testing and parameter sweeping. More information on it can be found [here](https://github.com/cadCAD-org/cadCAD).

## Folder Structure

1. Exploratory: Assorted notebooks that were used for working through ideas before integrating them into the mathematical specification. These can be ignored, but are left within the repository if similar questions ever arise again.
2. Model: The folder containing the code for running a cadCAD model with MSML as the wiring orchestration engine. Currently the preference is to use the native MSML engine but this is set up for when/if large scale models and parameter selection under uncertainty workflows are run.
3. Research: An Obsidian vault filled with annotated documents and meeting notes. This can also be safely ignored unless one wants to see some of the underlying documents that went into creating the specification.
4. Spec: The folder containing the majority of the code and all the components used for the spec creation process.

### Spec Folders

1. src: The specification of all components of the system. The folder of Implementations/Python specifically is the code that is bound to all components for actually running the simulation.
2. obsidian: This folder contains the outputted spec which can be opened up as an Obsidian vault to easily understand every component in the system. It is auto-generated every time the "Build Obsidian.ipynb" notebook is run.
3. simulation: Special functions for running the simulations. The folders are analytics for any analytical functions of results, config for defining out default starting states and parameters, preprocessing for functions that are used before the simulation runs and postprocessing for functions and metrics run after the simulation has run.
4. Wiring Examples: A folder of examples of running individual wirings. These examples are mostly meant for development purposes when zooming in on a specific aspect of the spec.

### Spec Notebooks

1. Build Obsidian: This notebook allows for building out the Obsidian spec.
2. Single Simulation: Notebook for experimenting with running one single simulation.
3. Controller Basic Scenarios: Notebook for the basic scenarios in testing the controller.
4. Controller Basic Scenarios - Variable Difficulty: Notebook for the basic scenarios with a varying aggregate hashpower array.

## Running Simulations

The following are the components for running a simulation (which can be seen in "Spec/Controller Basic Scenarios.ipynb"):
- load_from_json() loads the math spec object
- Under global inputs, the wirings run, the number of timesteps, and some the aggregate hashpower series can be set for use across all simulations
- An experiment is initialized with a name, a dictionary for updates to base parameters, a dictionary for updates to base state, and the blocks to run (passed from the global inputs)
- ms.run_experiment() runs the experiment and returns the final state, parameters used, a dataframe of the simulation log and metrics imputed
- The parameters of this function define out the things that happen before and after including preprocessing, postprocessing and any metrics to compute for a simulation