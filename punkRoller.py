import csv
import random
import sys


def main():
    print(cyberTechRoller())


def cashAndGearRoller() -> list:
    """
    Function for picking the initial, banal equipment for characters
    :return: list
    """
    startingGear = []
    gearColumn1 = csvReader("documents\\cashAndGearColumn1.csv")
    gearColumn2 = csvReader("documents\\cashAndGearColumn2.csv")
    gearColumn3 = csvReader("documents\\cashAndGearColumn3.csv")

    startingGear.append(random.choice(gearColumn1))
    startingGear.append(random.choice(gearColumn2))
    startingGear.append(random.choice(gearColumn3))

    return startingGear


def attributeRoller(preferredStat=False, defaultDie=6, defaultRollPool=3) -> int:
    """
    Function for providing stats for each roll garnered based on whether the stat is preferred or not.
    :param preferredStat: Tells if the stat being generated should be rolled with 3d6 (False) or 4d6 drop the lowest (True).
    :type preferredStat: bool
    :param defaultDie: The number of faces the die that is rolling for attributes should have
    :type defaultDie: int
    :param defaultRollPool: The baseline number of times the default die for attributes should be rolled.
    :type defaultRollPool: int
    :return: int
    """
    dicePool = [] # Place to store the values that have been rolled.

    for roll in range(defaultRollPool):
        dicePool.append(random.randint(1, defaultDie))

    if preferredStat: # If the stat is preferred, then add one more die & remove the lowest die from the current pool
        dicePool.append(random.randint(1, defaultDie))
        dicePool.remove(min(dicePool))

    match sum(dicePool): # Add all values of the dice pool & then return a stat based on the values from the core rulebook pg 40.
        case 1 | 2 | 3 | 4:
            return -3
        case 5 | 6:
            return -2
        case 7 | 8:
            return -1
        case 9 | 10 | 11 | 12:
            return 0
        case 13 | 14:
            return 1
        case 15 | 16:
            return 2
        case 17 | 18 | 19 | 20:
            return 3
        case _:
            sys.exit(f"\'{sum(dicePool)}\' is not a valid amount for the attributeRoller().")


def statsRoller() -> dict:
    """
    Function for rolling all of a character's stats & returning them to the caller.
    :return: dict
    """
    stats = {"Agility": -4, "Knowledge": -4, "Presence": -4, "Strength": -4, "Toughness": -4,} # Stats as per core rulebook pg 40.  Default is set to -4, a value that is not valid via the rulebook, for error catching.
    preferredStats = []
    while len(preferredStats) < 2: # Randomly choose two stats to be listed as preferred.
        currentChoice = (random.choice(list(stats)))
        if currentChoice not in preferredStats:
            preferredStats.append(currentChoice)

    for stat in stats: # Roll the character stats with the preferred ones getting an extra die for their pool
        if stat in preferredStats:
            stats[stat] = attributeRoller(True)
        else:
            stats[stat] = attributeRoller()

    for stat in stats: # Check to confirm all stats are within an acceptable range before returning them.
        if stats[stat] < -3 or stats[stat] > 3:
            sys.exit(f"\'{stat}\' with a value of {stats[stat]} is outside range of acceptable stats.")

    return stats


def weaponRoller() -> dict:
    """
    Function to roll out a weapon for characters & return the variables for the weapon
    :return: dict
    """
    weaponList = csvReader("Documents\\weapons.csv")
    weaponChoice = random.choice(weaponList)
    if weaponChoice[3] == "True":
        magCount = random.randint(1,4)
    else:
        magCount = 0
    weaponChoice[3] = magCount

    return {"Weapon Name":weaponChoice[0],"Damage":weaponChoice[1], "Autofire": weaponChoice[2], "Magazine Count": weaponChoice[3], "Notes": weaponChoice[4]}


def armorRoller(defaultDie=3) -> dict:
    """
    Function for randomly selecting armor from a csv file of armor types and stats.
    :param defaultDie: sets the upper limit of die to be rolled when selecting armor
    :type defaultDie: int
    :return: dict
    """
    armorList = csvReader("Documents\\armor.csv")
    armorNumber = random.randint(1, defaultDie)
    armorChoice = armorList[armorNumber - 1]
    return {"Armor Name": armorChoice[0], "Tier": armorChoice[1], "Damage Reduction": armorChoice[2], "Notes": armorChoice[3]}


def debtRoller(dieCount=3, dieFace=6, debtMultiplier=1000) -> dict:
    """
    Function for generating an amount of debt owed as well as who that debt is owed to
    :param dieCount: How many die should be rolled for calculating debt
    :type dieCount: int
    :param dieFace: What type of die should be used for the upper limit of debt on each die rolled
    :type dieFace: int
    :param debtMultiplier: How much the debt roll should be multiplied by to gather debt amount.
    :return: dict
    """
    debt = 0
    debtor = ""
    debtors = csvReader("Documents/debtors.csv")
    rollPool = []
    while len(rollPool) < dieCount:
        rollPool.append(random.randint(1, dieFace))

    debt = sum(rollPool) * debtMultiplier
    debtor = random.choice(debtors)
    debtor = debtor[0]
    return {"debtor": debtor, "debt": debt}


def cyberTechRoller() -> dict:
    """
    Function to randomly select from available cybertech & return the results to caller.
    :return: dict
    """
    cyberTech = csvReader("Documents/cybertech.csv")
    cyberTechChoice = random.choice(cyberTech)

    return {"Name": cyberTechChoice[0], "Description": cyberTechChoice[1], "Price": cyberTechChoice[2]}


def appRoller():
    pass


def nanoPowerRoller():
    pass


def infestationRoller():
    pass


def csvReader(documentFilePath, hasHeader="True", delimiterChar = "|", ) -> list:
    """
      Function for reading in designated CSV files, populating contents of rows to a list, then returning a list of lists for said contents
      :param documentFilePath: Document filepath where the csv file is located, including the csv file itself(i.e. "\\documents\\cashAndGearColumn1.csv"
      :type documentFilePath: str
      :param delimiterChar: Character defined as the seperator between columns within the csv file
      :type: char
      :param hasHeader: Specifies if the csv file has a header included for the information or not.
      :type hasHeader: bool
      :return: list
      """
    csvContentList = []  # Final list that will be returned to caller
    with open(documentFilePath, 'r') as csvContentFile:
        csvReadEngine = csv.reader(csvContentFile, delimiter=delimiterChar)
        if hasHeader:
            next(csvReadEngine)
        for row in csvReadEngine:
            csvContentList.append(row)
    csvContentFile.close()

    return csvContentList


if __name__ == '__main__':
    main()