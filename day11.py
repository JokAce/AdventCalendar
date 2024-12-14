from functools import cache
def getStones(filepath):
    with open(filepath, "r") as f:
        for line in f:
            words = line.strip().split()
    words = [int(x) for x in words]
    return words


def blink(stones, times):
    for _ in range(times):
        new_stones = []
        i = 0
        while i < len(stones):
            stone = stones[i]
            if stone == 0:
                new_stones.append(1)
            elif len(str(stones[i])) % 2 == 0:
                first_half = ((str(stone))[:len(str(stone)) // 2]).lstrip('0')
                if first_half == '':
                    first_half = 0
                second_half = ((str(stone))[len(str(stone)) // 2:]).lstrip('0')
                if second_half == '':
                    second_half = 0

                new_stones.append(int(first_half))
                new_stones.append(int(second_half))
            else:
                new_stones.append(stone * 2024)
            i += 1
        stones = new_stones
        print(stones)
    return len(stones)

@cache
def blink2(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return blink2(1, steps - 1)
    string = str(stone)
    length = len(string)
    if length % 2 == 0:
        return blink2(int(string[:length // 2]), steps - 1) + blink2(int(string[length // 2:]), steps - 1)
    return blink2(stone * 2024, steps - 1)
def total_blink(stones, times):
    return sum(blink2(stone, times) for stone in stones)

def day11():
    stones = getStones("inputs/day11_input.txt")
    return total_blink(stones, 75)
