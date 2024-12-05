import re

# sum of multiplications in a corrupted file
def getMultFromCorruptedFile(file):
    sum = 0
    with open(file) as file:
        muls = re.findall(r"mul\(-?\d+,-?\d+\)", file.read())
    file.close()

    for mul in muls:
        n,m = re.findall(r"-?\d+", mul)
        sum += int(n)*int(m)

    return sum

# same but don't for disable next mult and do for enable
def getMultFromCorruptedFile2(file):
    enable = True
    sum = 0

    with open(file) as file:
        muls = re.findall(r"(mul\(-?\d+,-?\d+\)|do\(\)|don't\(\))", file.read())
    file.close()

    for mul in muls:
        if mul == "do()":
            enable = True
        elif mul == "don't()":
            enable = False
        else:
            if enable:
                n,m = re.findall(r"-?\d+", mul)
                sum += int(n)*int(m)

    return sum


def day3():
    mul = getMultFromCorruptedFile2("inputs/day3_input.txt")
    return mul