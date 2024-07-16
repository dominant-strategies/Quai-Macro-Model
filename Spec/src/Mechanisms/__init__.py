from .Dummy import dummy_mechanisms
from .Block import block_mechanisms
from .Log import log_mechanisms
from .MonetaryPolicy import monetary_policy_mechanisms

mechanisms = []
mechanisms.extend(dummy_mechanisms)
mechanisms.extend(block_mechanisms)
mechanisms.extend(log_mechanisms)
mechanisms.extend(monetary_policy_mechanisms)
