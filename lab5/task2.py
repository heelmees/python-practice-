with open('C:\\Users\\richa\\dev\\bfu_python\\lab5\\src\\numbers.txt', 'r') as file:
    numbers = file.readlines()

numbers = [int(num.strip()) for num in numbers]

numbers.sort()

with open('C:\\Users\\richa\\dev\\bfu_python\\lab5\\src\\sorted_numbers.txt', 'w') as file:
    for num in numbers:
        file.write(f"{num}\n")
