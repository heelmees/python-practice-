'''
n = int(input("Введите натуральное число n: "))

if n > 0:
    for i in range(n, 0, -1):
        print(' ' * (n - i), end='')
        for j in range(1, i + 1):
            print(j, end='')
        for j in range(i - 1, 0, -1):
            print(j, end='')
        print()
else:
    print("Число должно быть натуральным")
'''
n = int(input("Введите натуральное число n: "))

if n > 0:
    number_width = len(str(n))
    
    for i in range(n, 0, -1):
        print(' ' * ((n - i) * number_width), end='')
        for j in range(1, i + 1):
            print(f"{j:>{number_width}}", end='')
        for j in range(i - 1, 0, -1):
            print(f"{j:>{number_width}}", end='')
        print()
else:
    print("Число должно быть натуральным")
