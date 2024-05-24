cities_set = set()

while True:
    city = input("Напишите город: ")
    if city in cities_set:
        print("REPEAT")
    else:
        cities_set.add(city)
        print("OK")