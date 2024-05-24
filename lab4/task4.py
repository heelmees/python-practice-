def count(text):
    words = text.split()
    word_count = {}
    result = []
    for word in words:
        if word in word_count:
            result.append(word_count[word])
        else:
            result.append(0)
        word_count[word] = word_count.get(word, 0) + 1
    return result

string = "one two one two three"
output = count(string)
print("Входная строка:", string)
print("Вывод:", output)