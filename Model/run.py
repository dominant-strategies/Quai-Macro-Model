from psub import psub_blocks
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
from cadCAD import configs
from cadCAD.configuration.utils import config_sim
from cadCAD.configuration import Experiment
from copy import deepcopy
import pandas as pd


def load_config(monte_carlo_runs: int, t: int, params, initial_state):
    sim_config = config_sim(
        {
            "N": monte_carlo_runs,  # number of monte carlo runs
            "T": range(t),  # number of timesteps
            "M": params,  # simulation parameters
        }
    )

    exp = Experiment()
    exp.append_configs(
        sim_configs=sim_config,
        initial_state=initial_state,
        partial_state_update_blocks=psub_blocks,
    )
    return exp


def add_config(exp: Experiment, monte_carlo_runs: int, t: int, params, initial_state):
    sim_config = config_sim(
        {
            "N": monte_carlo_runs,  # number of monte carlo runs
            "T": range(t),  # number of timesteps
            "M": params,  # simulation parameters
        }
    )

    exp.append_configs(
        sim_configs=sim_config,
        initial_state=initial_state,
        partial_state_update_blocks=psub_blocks,
    )


def run(exp, context=None, disable_deepcopy=False) -> pd.DataFrame:
    """
    Run simulation
    """
    # execute in local mode
    if context is None:
        exec_mode = ExecutionMode()
        _context = exec_mode.local_mode
    else:
        _context = context

    if disable_deepcopy:
        ctx = ExecutionContext(
            context=_context, additional_objs={"deepcopy_off": disable_deepcopy}
        )
    else:
        ctx = ExecutionContext(context=_context)

    sim = Executor(exec_context=ctx, configs=exp.configs)
    raw_system_events, _, _ = sim.execute()
    df = pd.DataFrame(raw_system_events)
    return df
