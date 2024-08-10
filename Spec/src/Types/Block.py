EntityType = {
    "name": "Entity Type",
    "type": "EntityType",
    "notes": "",
}

BlockNumberType = {
    "name": "Block Number Type",
    "type": "BlockNumberType",
    "notes": "",
}

BlockDifficultyType = {
    "name": "Block Difficulty Type",
    "type": "BlockDifficultyType",
    "notes": "Difficulty in has",
}

HashType = {
    "name": "Hash Type",
    "type": "HashType",
    "notes": "",
}

BlockArrayType = {
    "name": "Block Array Type",
    "type": "BlockArrayType",
    "notes": "An array of blocks where each block has its difficulty and its level",
}

HashpowerPerSecond = {
    "name": "Hashpower per Second",
    "type": "HashpowerPerSecond",
    "notes": "The amount of hashpower per second",
}

HashCumulativeSumArrayType = {
    "name": "Hash Cumulative Sum Array Type",
    "type": "HashCumulativeSumArrayType",
    "notes": "A cumulative sum array for total hash (for computation effeciency in simulation)",
}

BlockDifficultyMultiplesType = {
    "name": "Block Difficulty Multiples Type",
    "type": "BlockDifficultyMultiplesType",
    "notes": "A dictionary mapping each block level to a multiple of difficulty",
}

NumberOfRegionsType = {
    "name": "Number of Regions Type",
    "type": "NumberOfRegionsType",
    "notes": "",
}

ZonesPerRegionType = {
    "name": "Zones per Region Type",
    "type": "ZonesPerRegionType",
    "notes": "",
}

MiningEpochArrayType = {
    "name": "Mining Epoch Array Type",
    "type": "MiningEpochArrayType",
    "notes": "An array of mining epochs where each mining epoch has the mined blocks of type BlockArrayType and mining time in seconds",
}


block_types = [
    EntityType,
    BlockNumberType,
    BlockDifficultyType,
    HashType,
    BlockArrayType,
    HashpowerPerSecond,
    HashCumulativeSumArrayType,
    BlockDifficultyMultiplesType,
    NumberOfRegionsType,
    ZonesPerRegionType,
    MiningEpochArrayType,
]
