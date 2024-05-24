text = "Скажи-ка, дядя, ведь недаром Москва, спаленная пожаром, Французу отдана? Ведь были ж схватки боевые, Да, говорят, еще какие!"

text = text.lower()
for char in '.,;:-?!()[]{}"\'':
    text = text.replace(char, ' ')

words = text.split()

word_count = {}
for word in words:
    if word:  # проверяем, что слово не пустое
        word_count[word] = word_count.get(word, 0) + 1

sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

for word, frequency in sorted_words:
    print(word)
