def is_subset(set1, set2):
    for item in set1:
        if item not in set2:
            return False
    if set1 == set2:
        return False
    return True

inputs = [
    ({1, 2, 3}, {1, 4, 5}),
    ({1, 2, 3, 4, 5, 6, 7}, {10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0}),
    ({1, 10, 223, 413, 2}, {1, 10, 223, 413, 2})
]

for set1, set2 in inputs:
    print(f"Входные данные: {set1} и {set2}.")
    print(f"Выходные значения: {is_subset(set1, set2)}.")