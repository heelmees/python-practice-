'''
n = int(input("Введите число: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end = '')
    print(" ")
'''

n = int(input("Введите натуральное число n: "))
number_width = len(str(n))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(f"{j:{number_width}}", end=' ')
    print()
