from .Dummy import dummy_wiring
from .Simulation import simulation_wiring
from .Block import block_wiring
from .Controller import controller_wiring

wiring = []
wiring.extend(dummy_wiring)
wiring.extend(simulation_wiring)
wiring.extend(block_wiring)
wiring.extend(controller_wiring)
