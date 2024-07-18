from .Dummy import dummy_policies
from .Block import block_policies
from .Market import market_policies

policies = []
policies.extend(dummy_policies)
policies.extend(block_policies)
policies.extend(market_policies)
