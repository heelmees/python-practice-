digit = int(input("Введите число от 1 до 1000: "))

units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
second_tens = ['одиннадцать', 'двенадцать', 'тренадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
              'семнадцать', 'восемнадцать', 'девятнадцать']
tens = ['', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']

if digit == 1000:
    print('Тысяча')

if 0 < digit < 11:
    print(units[digit])
elif 10 < digit < 20:
    print(second_tens[digit % 10 - 1])
elif 19 < digit < 1000:
    hundred = digit % 1000 // 100
    ten = digit % 100 // 10
    unit = digit % 10
    second_ten = digit % 100

    if 10 < second_ten < 20:
        print(hundreds[hundred] + ' ' + second_tens[second_ten % 10 - 1])

    elif ten == 0 and unit != 0:
        print(hundreds[hundred] + ' ' + units[unit])

    elif ten == 0 and unit == 0:
        print(hundreds[hundred])

    elif unit != 0:
        print(hundreds[hundred] + ' ' + tens[ten - 1] + ' ' + units[unit])

    else:
        print(hundreds[hundred] + ' ' + tens[ten - 1])