'''
n = int(input("Введите натуральное число n: "))

if n > 0:
    for i in range(n, 0, -1):
        print(''.join(str(j) for j in range(1, i + 1)))
else:
    print("Число должно быть натуральным")
'''
n = int(input("Введите натуральное число n: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end='')
    print()
