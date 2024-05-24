n = input("Введите строку: ")

words = n.split()
abbreviation = ""
for word in words:
    abbreviation += word[0].upper()

print("Аббревиатура:", abbreviation)
