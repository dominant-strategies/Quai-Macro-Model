from .Dummy import dummy_spaces
from .Block import block_spaces
from .MonetaryPolicy import monetary_policy_spaces

spaces = []
spaces.extend(dummy_spaces)
spaces.extend(block_spaces)
spaces.extend(monetary_policy_spaces)
