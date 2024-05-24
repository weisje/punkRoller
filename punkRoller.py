import csv


def main():
    testFile = csvReader("Documents\\cashAndGearColumn1.csv")
    print(testFile)


def cashAndGearRoller():
    pass


def attributeRoller(preferredStat=False):
    pass


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
    csvContentList = [] # Final list that will be returned to caller
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
