def unlock_tokens_policy_v1(state, params, spaces):
    current_time = state["Time"]
    unlocked_qi = 0
    unlocked_quai = 0
    unlock_schedule_quai = state["Quai Unlock Schedule"]
    unlock_schedule_qi = state["Qi Unlock Schedule"]

    while len(unlock_schedule_quai) > 0:
        if unlock_schedule_quai[0]["time"] <= current_time:
            unlocked_quai += unlock_schedule_quai.pop(0)["amount"]
        else:
            break

    while len(unlock_schedule_qi) > 0:
        if unlock_schedule_qi[0]["time"] <= current_time:
            unlocked_qi += unlock_schedule_qi.pop(0)["amount"]
        else:
            break

    space = {
        "Qi Tokens": unlocked_qi,
        "Quai Tokens": unlock_schedule_quai,
        "Quai Unlock Schedule": unlock_schedule_quai,
        "Qi Unlock Schedule": unlock_schedule_qi,
    }

    return [space]
