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

# calculate the distance between paired values and add all of them
def calculateTotalDistance(rightNbList, leftNbList):

    sum = 0

    rightNbList.sort()
    leftNbList.sort()

    for i in range(len(rightNbList)):
        sum += abs(rightNbList[i] - leftNbList[i])

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

def day1(): #('Total Distance: ', 1941353, 'Similarity Score: ', 22539317)
    rCol, lCol = separateColumns("inputs/day1_input.txt")
    totalDistance = calculateTotalDistance(rCol,lCol)
    score = similarityScore(rCol, lCol)

    return "Total Distance: ", totalDistance, "Similarity Score: ", score
