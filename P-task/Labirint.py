def found(pathArr, finPoint):
    weight = 1
    for i in range(len(pathArr) * len(pathArr[0])):
        for y in range(len(pathArr)):
            for x in range(len(pathArr[y])):
                if pathArr[y][x] == weight:
                    # Вниз
                    if y > 0 and pathArr[y - 1][x] == 0:
                        pathArr[y - 1][x] = weight + 1

                        # Вверх
                    if y < (len(pathArr) - 1) and pathArr[y + 1][x] == 0:
                        pathArr[y + 1][x] = weight + 1

                    # Вправо
                    if x > 0 and pathArr[y][x - 1] == 0:
                        pathArr[y][x - 1] = weight + 1

                    # Влево
                    if x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == 0:
                        pathArr[y][x + 1] = weight + 1

                    # Конечная точка
                    if (abs(y - finPoint[0]) + abs(x - finPoint[1])) == 1:
                        pathArr[finPoint[0]][finPoint[1]] = weight + 1
                        return True
        weight += 1
    return False


def printPath(pathArr, finPoint):
    y = finPoint[0]
    x = finPoint[1]
    weight = pathArr[y][x]
    result = list(range(weight))
    while (weight):
        weight -= 1
        if y > 0 and pathArr[y - 1][x] == weight:
            result[weight] = 'Вниз'
            y -= 1
        elif y < (len(pathArr) - 1) and pathArr[y + 1][x] == weight:
            result[weight] = 'Вверх'
            y += 1
        elif x > 0 and pathArr[y][x - 1] == weight:
            result[weight] = 'Вправо'
            x -= 1
        elif x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == weight:
            result[weight] = 'Влево'
            x += 1

    return result[1:]


labirint = []
with open("file.txt") as myFile:
    for line in myFile:
        labirint.append(line.replace('\n', '').split(' '))

ii = 0
for i in labirint:
    jj = 0
    for j in i:
        if j == 'A':
            labirint[ii][jj] = 1
            pozIn = (ii, jj)
        elif j == 'B':
            labirint[ii][jj] = 0
            pozOut = (ii, jj)
        elif j == '1':
            labirint[ii][jj] = -1
        else:
            labirint[ii][jj] = 0
        jj += 1
    ii += 1

if not found(labirint, pozOut):
    print("Путь не найден!")
else:
    result = printPath(labirint, pozOut)

    for i in labirint:
        for line in i:
            print("{:^3}".format(line), end=" ")
        print()
    print(result)