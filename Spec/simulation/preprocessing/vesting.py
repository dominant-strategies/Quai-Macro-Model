import numpy as np


def vesting_schedule_translate(state, params):
    unlock_schedule = []
    for x in params["Initial Vesting Schedule"]:
        if x["vesting_frequency"] == "Immediate":
            unlock_schedule.append(
                {
                    "time": x["time"] * 365,
                    "amount": x["vesting_amount"],
                    "recipient": x["recipient"],
                }
            )
        elif x["vesting_frequency"] == "Monthly":
            months = x["duration"] * 12
            times = np.linspace(x["time"], x["time"] + x["duration"], months + 1)[1:]
            amount = x["vesting_amount"] / months
            for t in times:
                unlock_schedule.append(
                    {"time": t * 365, "amount": amount, "recipient": x["recipient"]}
                )
        else:
            assert False, "Not a recognized vesting frequency"
    unlock_schedule = sorted(unlock_schedule, key=lambda x: x["time"])
    quai_supply = sum([x["amount"] for x in unlock_schedule])
    unlock_schedule = [x for x in unlock_schedule if x["time"] > 0]
    locked_quai = sum([x["amount"] for x in unlock_schedule])

    state["Quai Unlock Schedule"] = unlock_schedule
    state["Qi Unlock Schedule"] = []
    state["Locked Qi Supply"] = 0
    state["Quai Supply"] = quai_supply
    state["Circulating Quai Supply"] = [quai_supply]
    state["Locked Quai Supply"] = locked_quai
    state["Mining Log"] = []

    return state
