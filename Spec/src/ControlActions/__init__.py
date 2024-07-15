from .Dummy import dummy_control_actions
from .Simulation import simulation_control_actions

control_actions = []
control_actions.extend(dummy_control_actions)
control_actions.extend(simulation_control_actions)
