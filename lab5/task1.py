with open("C:\\Users\\richa\dev\\bfu_python\\lab5\src\\input.txt", 'r') as file:
    numbers = [int(number) for number in file.readline().split()]

product = 1
for number in numbers[:10]:
    product *= number

# Открываем файл для записи и записываем результат
with open('C:\\Users\\richa\dev\\bfu_python\\lab5\\src\\output.txt', 'w') as file:
    file.write(str(product))
