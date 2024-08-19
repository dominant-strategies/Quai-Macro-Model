from .Block import block_mechanisms
from .Log import log_mechanisms
from .MonetaryPolicy import monetary_policy_mechanisms
from .Controller import controller_mechanisms
from .Vesting import vesting_mechanisms

mechanisms = []
mechanisms.extend(block_mechanisms)
mechanisms.extend(log_mechanisms)
mechanisms.extend(monetary_policy_mechanisms)
mechanisms.extend(controller_mechanisms)
mechanisms.extend(vesting_mechanisms)
