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

### Spec Notebooks

## MSML Spec Creation Features

## MSML Wiring Features

## MSML Simulation Features

## cadCAD Simulation Features