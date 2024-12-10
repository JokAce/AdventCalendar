import re
from itertools import product

def evaluate_left_to_right(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def calibration(filepath):
    with open(filepath, "r") as f:
        calcul = re.findall(r"(\d+):\s([^\n]+)", f.read())
        total = 0

        for cal in calcul:
            res = int(cal[0])
            numbers = list(map(int, cal[1].split()))
            operator_combinations = list(product(["+", "*", "||"], repeat=len(numbers) - 1))

            valid = False
            for op in operator_combinations:
                if evaluate_left_to_right(numbers, op) == res:
                    valid = True
                    break

            if valid:
                total += res

        return total

def day7():
    total = calibration("inputs/day7_input.txt")

    return total
