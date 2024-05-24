def count_unique_numbers(n):
    unique_numbers = set(numbers)
    return len(unique_numbers)

inputs = [[1, 5, 3, 6, 4, 7, 2, 5, 6, 7, 3, 3, 5, 6, 3, 2, 2, 5]]

for numbers in inputs:
    unique_count = count_unique_numbers(numbers)
    print(f"Входные данные: {inputs}.")
    print(f"Выходные значения: {unique_count}.")