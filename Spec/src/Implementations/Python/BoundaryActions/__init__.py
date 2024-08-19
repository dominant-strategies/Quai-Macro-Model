from .Dummy import v1_dummy_boundary, v1_dummy_boundary2, v2_dummy_boundary2
from .Block import mine_block_boundary_action_v1
from .Conversions import test_quai_conversion, test_qi_conversion
from .Market import test_price_movements_boundary

boundary_action_options = {
    "V1 Dummy Boundary Action Option": v1_dummy_boundary,
    "V1 Dummy Boundary Action 2 Option": v1_dummy_boundary2,
    "V2 Dummy Boundary Action 2 Option": v2_dummy_boundary2,
    "Mine Block Boundary Action V1": mine_block_boundary_action_v1,
    "TEST Quai Conversion": test_quai_conversion,
    "TEST Qi Conversion": test_qi_conversion,
    "TEST Price Movements Boundary": test_price_movements_boundary,
}
