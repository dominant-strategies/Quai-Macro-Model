from .Block import block_spaces
from .MonetaryPolicy import monetary_policy_spaces
from .Controller import controller_spaces
from .Market import market_spaces
from .Vesting import vesting_spaces

spaces = []

spaces.extend(block_spaces)
spaces.extend(monetary_policy_spaces)
spaces.extend(controller_spaces)
spaces.extend(market_spaces)
spaces.extend(vesting_spaces)
