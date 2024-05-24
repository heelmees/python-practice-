input_strings = ['abc', 'bcd', 'abc', 'abc', 'dcd', 'aaa']
occurrences = {}

for string in input_strings:
    if string in occurrences:
        occurrences[string] += 1
    else:
        occurrences[string] = 1

for string, count in occurrences.items():
    print(f'{string}: {count}')