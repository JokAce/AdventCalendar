def mapToBlocks(filepath):
    blocks = []
    is_free_space = False
    index = -1
    with open(filepath, "r") as f:
        while True:
            content = f.read(1)
            if content == '':
                break
            if is_free_space:
                for i in range(int(content)):
                    blocks.append('.')
                is_free_space = False
            else:
                index += 1
                for i in range(int(content)):
                    blocks.append(index)
                is_free_space = True
    return blocks


def moveBlocks(tab):
    compacted = tab.copy()
    last_modified = len(compacted)
    stop = False

    for i in range(len(compacted) - 1, -1, -1):
        if stop:
            break
        if compacted[i] != '.':
            for j in range(len(compacted)):
                if j >= last_modified:
                    stop = True
                    break
                if compacted[j] == '.':
                    compacted[j] = compacted[i]
                    compacted[i] = '.'
                    last_modified = i
                    break

    return compacted


def moveBlocks2(tab):
    compacted = tab.copy()
    index = len(compacted) - 1
    last_modified = len(compacted)

    while index >= 0:

        blocks = []
        free_spaces = []
        index_space = 0

        # find blocks
        while compacted[index] == '.':
            index -= 1
        blocks_id = compacted[index]
        while compacted[index] == blocks_id:
            blocks.append(index)
            index -= 1

        # find free spaces
        while index_space < len(compacted) and len(blocks) > len(free_spaces):
            if index_space >= last_modified:
                break
            while index_space < len(compacted) and compacted[index_space] != '.':
                index_space += 1

            tmp = []
            while index_space < len(compacted) and compacted[index_space] == '.':
                tmp.append(index_space)
                index_space += 1

            if index_space < last_modified:
                free_spaces = tmp.copy()

            if len(blocks) > len(free_spaces):
                free_spaces.clear()

        last_modified = blocks[len(blocks)-1]

        # move blocks
        if len(blocks) <= len(free_spaces):
            for i in range(len(free_spaces) - (len(free_spaces) - len(blocks))):
                compacted[free_spaces[i]] = compacted[blocks[i]]
                compacted[blocks[i]] = '.'

    return compacted


def checkSum(tab):
    sum = 0
    for i in range(len(tab) - 1):
        if tab[i] != '.':
            sum += i * int(tab[i])

    return sum


def day9():
    blocks = mapToBlocks("inputs/day9_input.txt")
    compacted = moveBlocks2(blocks)
    return checkSum(compacted)
