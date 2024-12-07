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

def correctWrongUpdates(rules, updates):

    sum = 0

    for update in updates:
        if rightUpdates(rules, update) == 0:
            gr = dfs(update[0], graph(update, rules))
            sum += gr[len(gr) // 2]
            print(gr)

    return sum

def graph(update, rules):
    gr = {page: [] for page in update}

    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[i] in rules and update[j] in rules[update[i]]:
                gr[update[i]].append(update[j])

    print(gr)

    return gr

def dfs(node, graph, visited=None, stack=None):
    if visited is None:
        visited = set()
    if stack is None:
        stack = []

    def visit(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                visit(neighbor)
            stack.append(node)

    for node in graph:
        visit(node)

    return stack[::-1]

def day5():

    rules = extractRules("inputs/day5_input.txt")
    updates = extractUpdates("inputs/day5_input.txt")

    return correctWrongUpdates(rules, updates)



    #test = correctWrongUpdates(rules,updates)
