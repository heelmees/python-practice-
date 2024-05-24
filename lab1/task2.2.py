'''
n = int(input("Введите натуральное число n: "))
for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end="")
        
    for j in range(i, 1, -1):
        print(j, end="")
        
    for j in range(1, i+1):
        print(j, end="")
        
    print()

'''

n = int(input("Введите натуральное число n: "))
number_width = len(str(n * n))

for i in range(1, n + 1):
    print(' ' * (number_width + 1) * (n - i), end='')
    for j in range(1, i + 1):
        print(f"{j:{number_width}d}", end=' ')
    for j in range(i - 1, 0, -1):
        print(f"{j:{number_width}d}", end=' ')
    print()

