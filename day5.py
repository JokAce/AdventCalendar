import re

def extractRules(file):
    rules_dict = {}

    with open(file) as file:
        content = file.read()
        rules = re.findall(r"-?\d+\|-?\d+", content)

    for rule in rules:
        key, val = re.findall(r"-?\d+", rule)
        key, val = int(key), int(val)

        if key not in rules_dict:
            rules_dict[key] = []
        rules_dict[key].append(val)

    return rules_dict


def extractUpdates(file):
    result = []

    with open(file, "r") as f:
        for line in f:
            if re.match(r"^\d+(,\d+)*$", line.strip()):
                numbers = map(int, line.strip().split(","))
                result.append(list(numbers))

    return result



def rightUpdates(rules, updates):
    for i in range(len(updates)):
        if updates[i] in rules:
            for j in range(i+1, len(updates)):
                if updates[j] in rules:
                    if not updates[j] in rules[updates[i]]:
                        return 0

    return updates[len(updates) // 2]


def totalRightUpdates(rules, updates):
    sum = 0

    for update in updates:
         sum += rightUpdates(rules, update)

    return sum

def correctWrongUpdates():
    pass

def totalCorrectedWrongUpdates():
    pass


def day5():

    rules = extractRules("inputs/day5_input.txt")
    updates = extractUpdates("inputs/day5_input.txt")

    test = totalRightUpdates(rules,updates)
    return test
