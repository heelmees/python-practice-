n = int(input("Введите количество строк треугольника Серпинского: "))

if n < 0:
    print("Введите положительное число.")
else:
    triangle = [[1]]
    for _ in range(1, n):
        prev_row = triangle[-1]
        next_row = [1]
        for j in range(1, len(prev_row)):
            next_row.append(prev_row[j - 1] + prev_row[j])
        next_row.append(1)
        triangle.append(next_row)
    print("\nТреугольник Серпинского из", n, "строк:")
    width = len(' '.join(map(str, triangle[-1])))
    for row in triangle:
        serpin_row = []
        for num in row:
            if num % 2 == 0:
                serpin_row.append(' ')
            else:
                serpin_row.append('*')
        print(' '.join(serpin_row).center(width))