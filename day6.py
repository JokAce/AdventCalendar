import numpy as np


def fileToTab(filepath):
    rows = []

    index_y = -1
    index_x = -1

    with open(filepath, "r") as f:
        for line in f:
            stripped_line = line.strip().replace(" ", "")
            if stripped_line:
                if index_x == -1:
                    tmp = stripped_line.find('^')
                    index_y += 1
                    if tmp != -1:
                        index_x = tmp

                rows.append(list(stripped_line))

    guard_index = [index_y, index_x]

    width = len(rows[0])
    rows = [['X'] * (width + 2)] + [['X'] + row + ['X'] for row in rows] + [['X'] * (width + 2)]

    guard_index[0] += 1
    guard_index[1] += 1

    return np.array(rows), guard_index


def countDistinctPos(grid, guard_pos):
    direction = "up"
    guard_pos = list(guard_pos)
    visited = set()
    visited.add(tuple(guard_pos))

    while grid[guard_pos[0]][guard_pos[1]] != 'X':
        if direction == "up":
            while guard_pos[0] > 0 and grid[guard_pos[0] - 1][guard_pos[1]] != '#':
                guard_pos[0] -= 1
                visited.add(tuple(guard_pos))
            direction = "right"

        elif direction == "right":
            while guard_pos[1] < len(grid[0]) - 1 and grid[guard_pos[0]][guard_pos[1] + 1] != '#':
                guard_pos[1] += 1
                visited.add(tuple(guard_pos))
            direction = "down"

        elif direction == "down":
            while guard_pos[0] < len(grid) - 1 and grid[guard_pos[0] + 1][guard_pos[1]] != '#':
                guard_pos[0] += 1
                visited.add(tuple(guard_pos))
            direction = "left"

        elif direction == "left":
            while guard_pos[1] > 0 and grid[guard_pos[0]][guard_pos[1] - 1] != '#':
                guard_pos[1] -= 1
                visited.add(tuple(guard_pos))
            direction = "up"

    return len(visited)-1



def day6():
    grid, guard_pos = fileToTab("inputs/day6_input.txt")

    return countDistinctPos(grid, guard_pos)
