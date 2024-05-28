import csv
import random


def main():
    attributeRoller(True)


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

    if preferredStat:
        dicePool.append(random.randint(1, defaultDie))
        dicePool.remove(min(dicePool))


def statsRoller():
    pass


def weaponRoller():
    pass


def armorRoller():
    pass


def debtRoller():
    pass


def cyberTechRoller():
    pass


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