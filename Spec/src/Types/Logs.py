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

simulation_types = [ConversionsArrayType]

"Mined Ratio Array Type"  # Ratio, Block Number
"Hash Array Type"  # Hash amount, block number