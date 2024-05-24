n = int(input("Введите количество строк треугольника Паскаля: "))
pascal_triangle = [[1]]
for i in range(1, n):
    row = [1]
    for j in range(1, i):
        row.append(pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j])
    row.append(1)
    pascal_triangle.append(row)
for row in pascal_triangle:
    print(' '.join(map(str, row)).center(2*n))
