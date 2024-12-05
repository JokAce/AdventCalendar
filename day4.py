import numpy as np


# turn a file into an array of arrays of charac
def fileToTab(filepath):
    rows = []

    with open(filepath, "r") as f:
        for line in f:
            stripped_line = line.strip().replace(" ", "")
            if stripped_line:
                rows.append(list(stripped_line))

    return np.array(rows)


# from a position, find every way to write XMAS
def findXmas(tab, i, j):
    nbLetters = 4
    sum = 0
    lineLen = len(tab)
    colLen = len(tab[i])

    if i + nbLetters <= lineLen:
        word = ""
        for index in range(nbLetters):
            word += tab[i + index][j]

        if word == "XMAS" or word == "SAMX":
            sum += 1

    if j + nbLetters <= colLen:
        word = ""
        for index in range(nbLetters):
            word += tab[i][j + index]

        if word == "XMAS" or word == "SAMX":
            sum += 1

    if j + nbLetters <= colLen and i + nbLetters <= lineLen:
        word = ""
        for index in range(nbLetters):
            if i + index < lineLen and j + index < colLen:
                word += tab[i + index][j + index]

        if word == "XMAS" or word == "SAMX":
            sum += 1

    if j + nbLetters <= colLen and i - nbLetters + 1 >= 0:
        word = ""
        for index in range(nbLetters):
            if i - index >= 0 and j + index < colLen:
                word += tab[i - index][j + index]

        if word == "XMAS" or word == "SAMX":
            sum += 1

    return sum


# Calculate total of XMAS in a grid
def findTotalXMAS(tab):
    sum = 0

    for i in range(len(tab)):
        for j in range(len(tab[i])):
            sum += findXmas(tab, i, j)

    return sum


# From a position, find the word MAS written in X
def findX_Mas(tab, i, j):
    if (i - 1 >= 0) and i + 1 < len(tab) and (j - 1 >= 0) and (j + 1 < len(tab[i])):
        oneMAS = False
        twoMAS = False

        if tab[i - 1][j - 1] == 'M':
            if tab[i + 1][j + 1] == 'S':
                oneMAS = True

        elif tab[i - 1][j - 1] == 'S':
            if tab[i + 1][j + 1] == 'M':
                oneMAS = True
        else:
            return 0

        if oneMAS:
            if tab[i + 1][j - 1] == 'M':
                if tab[i - 1][j + 1] == 'S':
                    twoMAS = True
            elif tab[i + 1][j - 1] == 'S':
                if tab[i - 1][j + 1] == 'M':
                    twoMAS = True
            else:
                return 0

        if oneMAS and twoMAS:
            return 1

    return 0


# Calculate total of X-MAS in a grid
def findTotalX_Mas(tab):
    sum = 0

    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == 'A':
                sum += findX_Mas(tab, i, j)

    return sum


def day4():
    tab = fileToTab("inputs/day4_input.txt")
    test = fileToTab("inputs/day4_test.txt")

    sum = findTotalX_Mas(tab)
    return sum
