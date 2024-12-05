# Read file and separate left and right values into two different lists
def separateColumns(file):
    rightNbList = []
    leftNbList = []
    ct = 0

    with open(file, "r") as file:
        for line in file :
            for word in line.split():
                ct += 1
                if ct % 2 == 0:
                    rightNbList.append(int(word))
                else:
                    leftNbList.append(int(word))

    return rightNbList, leftNbList

# Pair smallest number from right list with left list then second smallest number, etc
def pairSmallestNb(rightNbList, leftNbList):

    rList = rightNbList.copy()
    lList = leftNbList.copy()

    pairedList = []

    while rList or lList:

        smallestNbR = rList[0]
        smallestNbL = lList[0]

        for nb in rList:
            if nb < smallestNbR:
                smallestNbR = nb

        rList.remove(smallestNbR)

        for nb in lList:
            if nb < smallestNbL:
                smallestNbL = nb

        lList.remove(smallestNbL)

        pairedList.append((smallestNbL, smallestNbR))

    return pairedList

# calculate the distance between paired values and add all of them
def calculateTotalDistance(pairedList):
    sum = 0

    for nbL, nbR in pairedList:
        sum += abs(nbL-nbR)

    return sum

# Count nb of occurrence of the left number in the right list then multiply. And add to total
def similarityScore(rightNbList, leftNbList):
    occ = 0
    sum = 0

    for nbL in leftNbList:
        for nbR in rightNbList:
            if nbL == nbR:
                occ += 1
            sum += nbL * occ
            occ = 0

    return sum

def day1():
    rCol, lCol = separateColumns("inputs/day1_input.txt")
    pairedList = pairSmallestNb(rCol, lCol)
    totalDistance = calculateTotalDistance(pairedList)
    score = similarityScore(rCol, lCol)

    return "Total Distance: ", totalDistance, "Similarity Score: ", score
