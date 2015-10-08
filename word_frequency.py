import re


def word_frequency(words, used):
    """takes in (key, value) and spits out a dictionary"""
    return dict(zip((words_used),(times_used)))

def space_remover(phrase):
    """ Removes the punctuation from the string"""
    return re.sub(r'[^A-Za-z ]', "", phrase)

with open("sample.txt") as file:
    text = file.read()
    text = space_remover(text)
    text = text.split()

words_used = []
# putting each word into a list
for words in text:
    words_used.append(words)

times_used = []
# make a list of times each word was used
for words in words_used:
    times_used.append(words_used.count(words))
word_frequency_dict = word_frequency(words_used, times_used)
order = sorted(word_frequency_dict.items(), key=lambda x: x[1], reverse = True)
print(order[:20])
