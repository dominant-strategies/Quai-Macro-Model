from .Block import block_policies
from .Market import market_policies
from .Controller import controller_policies
from .Vesting import vesting_policies
from .User import user_policies

policies = []
policies.extend(block_policies)
policies.extend(market_policies)
policies.extend(controller_policies)
policies.extend(vesting_policies)
policies.extend(user_policies)
