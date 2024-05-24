a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

max_value = a
min_value = a

if b > max_value:
    max_value = b
elif b < min_value:
    min_value = b

if c > max_value:
    max_value = c
elif c < min_value:
    min_value = c

print(f"Максимальное число: {max_value}")
print(f"Минимальное число: {min_value}")
