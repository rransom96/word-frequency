def word_frequency(words, used):
    """takes in (key, value) and spits out a dictionary"""
    return dict(zip((words_used),(times_used)))

with open("sample.txt") as file:
    text = file.read().split()

re.sub(r'[^A-Za-z]',)

words_used = []
for words in text:
    words_used.append(words)

times_used = []
for words in words_used:
    times_used.append(words_used.count(words))
word_frequency_dict = word_frequency(words_used, times_used)


print(word_frequency_dict)
