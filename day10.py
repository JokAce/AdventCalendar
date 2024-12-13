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
                map[index].append(int(content))

            content = file.read(1)

    return np.array(map)


def total_trailheads(map):
    sum = 0

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                visited = set()
                sum += trailheads(map, i, j, visited)
    return sum


def trailheads(map, i, j, visited):
    if map[i][j] == 9 and (i, j) not in visited:
        visited.add((i, j))
        return 1

    count = 0

    if i != len(map) - 1 and map[i + 1][j] == map[i][j] + 1:
        count += trailheads(map, i + 1, j, visited)
    if i != 0 and map[i - 1][j] == map[i][j] + 1:
        count += trailheads(map, i - 1, j, visited)
    if j != 0 and map[i][j - 1] == map[i][j] + 1:
        count += trailheads(map, i, j - 1, visited)
    if j != len(map[i]) - 1 and map[i][j + 1] == map[i][j] + 1:
        count += trailheads(map, i, j + 1, visited)

    return count

def total_trailheads2(map):
    sum = 0

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                sum += trailheads2(map, i, j)
    return sum


def trailheads2(map, i, j):
    if map[i][j] == 9:
        return 1

    count = 0

    if i != len(map) - 1 and map[i + 1][j] == map[i][j] + 1:
        count += trailheads2(map, i + 1, j)
    if i != 0 and map[i - 1][j] == map[i][j] + 1:
        count += trailheads2(map, i - 1, j)
    if j != 0 and map[i][j - 1] == map[i][j] + 1:
        count += trailheads2(map, i, j - 1)
    if j != len(map[i]) - 1 and map[i][j + 1] == map[i][j] + 1:
        count += trailheads2(map, i, j + 1)

    return count

def day10():
    map = load_map("inputs/day10_input.txt")
    print(total_trailheads2(map))
