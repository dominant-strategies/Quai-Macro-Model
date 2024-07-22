from .Block import block_policies
from .Market import market_policies
from .Controller import controller_policies

policies = []
policies.extend(block_policies)
policies.extend(market_policies)
policies.extend(controller_policies)
