VestingScheduleType = {
    "name": "Vesting Schedule Type",
    "type": "VestingScheduleType",
    "notes": "A list of objects with the following attributes: vesting_amount, vesting_frequency, recipient, time (in years) for when it is active, and optionally duration if the vesting_frequency is not immediate",
}

UnlockScheduleType = {
    "name": "Unlock Schedule Type",
    "type": "UnlockScheduleType",
    "notes": "A sorted list (by earliest time) where each list object has the time for unlocking (in years), the amount, and the recipient",
}

LockupTableType = {
    "name": "Lockup Table Type",
    "type": "LockupTableType",
    "notes": "A table of lockups that exist in terms of time frame as the index, year of the system as columns, and mutliple of locked up amount returned as the values. Data structure will be a nested dictionary where outside key is the year of the system and inside keys are options offered.",
}


vesting_types = [VestingScheduleType, UnlockScheduleType, LockupTableType]
