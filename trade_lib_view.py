def Header(headerText):
    textLength = len(headerText)

    maxHifens = 49
    maxHifensLessTextLenght = maxHifens - textLength
    maxEachSide = round(maxHifensLessTextLenght / 2)

    hif = 0

    while(hif < maxEachSide):
        print("*", end="")
        hif += 1
    
    print("*", end="")
    print(" ", headerText, " ", end="")
    print("*", end="")

    if maxHifensLessTextLenght %2 != 0:
        hif -= 1

    while(hif < maxEachSide * 2):
        print("*", end="")
        hif += 1
    print("")


def DrawLine():
    hif = 0

    while hif < 55:
        print("*", end="")
        hif += 1
    print("")

   
def GetInteger(text):
    option = input(text)
    option = int(option)
    return option


def GetFloat(text):
    option = input(text)
    option = float(option)
    return option


def GetText(text):
    option = input(text)
    option = option.upper()
    return option
