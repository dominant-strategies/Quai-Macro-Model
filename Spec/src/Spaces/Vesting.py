unlock_tokens_space = {
    "name": "Unlock Tokens Space",
    "schema": {
        "Qi Tokens": "Qi Type",
        "Quai Tokens": "Quai Type",
        "Quai Unlock Schedule": "Unlock Schedule Type",
        "Qi Unlock Schedule": "Unlock Schedule Type",
    },
}

unlock_schedule_entry_space = {
    "name": "Unlock Schedule Entry Space",
    "schema": {
        "Quai Schedule Entry": "Unlock Schedule Type",
        "Qi Schedule Entry": "Unlock Schedule Type",
    },
}


vesting_spaces = [unlock_tokens_space, unlock_schedule_entry_space]
