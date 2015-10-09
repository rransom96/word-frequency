import re


def space_remover(phrase):
    """ Removes the punctuation from the string"""
    return re.sub(r'[^A-Za-z ]', "", phrase)

with open("sample.txt") as file:
    text = file.read().lower()
    text = space_remover(text)
    text = text.split()

word_frequency_dict = {}

for words in text:
    if words not in word_frequency_dict:
        word_frequency_dict[words] = 1
    else:
      word_frequency_dict[words] += 1

order = sorted(word_frequency_dict.items(), key=lambda x: x[1], reverse = True)
print(order[:20])
