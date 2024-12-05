def sortReports(file):
    reports = []
    index = 0

    with open(file, "r") as file:
        for line in file:
            reports.append([])
            for word in line.split():
                reports[index].append(int(word))

            index += 1

    return reports


def totalSafeReports(reports):
    sum = 0
    index = 0
    index_level = 0
    prev_nb = -1
    is_increasing = True

    for report in reports:
        is_safe = True
        for level in report:

            if index_level == 0:
                prev_nb = level
            elif index_level == 1:
                if not (1 <= abs(prev_nb - level) <= 3):
                    is_safe = False
                    break
                if level - prev_nb > 0:
                    is_increasing = True
                else:
                    is_increasing = False
                prev_nb = level
            else:
                if not ((level - prev_nb > 0) == is_increasing):
                    is_safe = False
                    break

                if not (1 <= abs(prev_nb - level) <= 3):
                    is_safe = False
                    break
                prev_nb = level
            index_level += 1

        index += 1
        index_level = 0
        if is_safe:
            sum += 1

    return sum

#totalSafeReports but with one unsafe level tolerance
def totalSafeReports2(reports):
    sum = 0
    index = 0
    index_level = 0
    prev_nb = -1
    is_increasing = True

    for report in reports:
        is_safe = True
        error = False
        for level in report:
            print(level)

            if index_level == 0:
                prev_nb = level
            elif index_level == 1:
                if not (1 <= abs(prev_nb - level) <= 3 ):

                    if error:
                        print("test2")
                        is_safe = False
                        break
                    else:
                        error = True
                        index_level = 0
                    print(error)

                if level - prev_nb > 0:
                    is_increasing = True
                else:
                    is_increasing = False
                prev_nb = level
            else:
                if not ((level - prev_nb > 0) == is_increasing) and not (level - prev_nb == 0):
                    print(error)
                    if error:
                        print("test3")
                        is_safe = False
                        break
                    else:
                        error = True
                    print(error)

                if not (1 <= abs(prev_nb - level) <= 3):
                    if error:
                        is_safe = False
                        break
                    else:
                        error = True

                prev_nb = level
            index_level += 1

        index += 1
        index_level = 0
        if is_safe:
            sum += 1

    return sum




def day2():
    test = [[1, 3, 7, 6, 8]]
    reports = sortReports("inputs/day2_input.txt")
    sum = totalSafeReports2(reports)
    return sum
