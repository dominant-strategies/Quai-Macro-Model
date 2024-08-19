from .Dummy import v1_dummy_control, v2_dummy_control
from .Vesting import v1_unlock_tokens_control_action

control_action_options = {
    "V1 Dummy Control": v1_dummy_control,
    "V2 Dummy Control": v2_dummy_control,
    "Unlock Tokens Control Action V1": v1_unlock_tokens_control_action,
}
