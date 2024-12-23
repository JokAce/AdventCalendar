import numpy as np

def load_map(file):
    map = []

    with open(file, "r") as file:
        index = 0
        content = file.read(1)
        map.append([])
        while content:
            if content == '\n':
                map.append([])
                index += 1
            else:
                map[index].append(content)

            content = file.read(1)

    return np.array(map)

def graph(tab):
    graph = {}

    for i in range(len(tab)):
        for j in range(len(tab[i])):
            current = (i, j)
            graph[current] = []

            if i != len(tab)-1 and tab[i+1][j] == tab[i][j]:
                graph[current].append((i+1,j))
            if i != 0 and tab[i-1][j] == tab[i][j]:
                graph[current].append((i-1,j))
            if j != len(tab[i])-1 and tab[i][j+1] == tab[i][j]:
                graph[current].append((i,j+1))
            if j != 0 and tab[i][j-1] == tab[i][j]:
                graph[current].append((i,j-1))

    return graph


visited = set()

def dfs(visited, graph, node, stack=None):
    if stack is None :
        stack = []
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour, stack)
        stack.append(node)
    return stack[::-1]

def perimeter(stack):
    sum = 0

    for s in stack:
        if not ((s[0] + 1, s[1]) in stack):
            sum +=1
        if not ((s[0] - 1, s[1]) in stack):
            sum += 1
        if not ((s[0], s[1] + 1) in stack):
            sum += 1
        if not ((s[0], s[1] - 1) in stack):
            sum += 1

    return sum


def mapCost(map):
    gr = graph(map)
    cost = 0

    for key in gr:
        if key not in visited:
            component = dfs(visited, gr, key)
            cost += len(component) * perimeter(component)

    return cost


def day12():
    map = load_map("inputs/day12_input.txt")
    return mapCost(map)


