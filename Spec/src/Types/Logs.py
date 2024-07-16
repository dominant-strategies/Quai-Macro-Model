ConversionsArrayType = {
    "name": "Conversions Array Type",
    "type": "ConversionsArrayType",
    "notes": r"""An array of the form:

List[{"Qi Value": "Qi Type",
"Quai Value": "Quai Type",
"Time": "Datetime Type"}]

The negaive values on Qi or Quai value denote amounts that were sent in by a user and burned to get out the converted other asset.
""",
}

MinedRatioArrayType = {
    "name": "Mined Ratio Array Type",
    "type": "MinedRatioArrayType",
    "notes": r"""An array of the form:

List[{"Ratio": "Mined Ratio Type",
"Block Number": "Block Number Type"}]

0 corresponds to 100% Qi, 1 corresponds to 100% Quai, number in between are the increments between those balances.""",
}

HashArrayType = {
    "name": "Hash Array Type",
    "type": "HashArrayType",
    "notes": r"""An array of the form:

List[{"Hash Value": "Hash Type",
"Block Number": "Block Number Type"}]

""",
}

MinedRatioType = {
    "name": "Mined Ratio Type",
    "type": "MinedRatioType",
    "notes": "0 corresponds to 100% Qi, 1 corresponds to 100% Quai, number in between are the increments between those balances.",
}


log_types = [ConversionsArrayType, MinedRatioArrayType, HashArrayType, MinedRatioType]
