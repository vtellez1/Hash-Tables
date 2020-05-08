import random

wordbank = {}

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
list_of_words = words.split()

for i in range(len(list_of_words) - 1):
    if list_of_words[i] not in wordbank:
        wordbank[list_of_words[i]].append(list_of_words[i+1])


print(wordbank)
# TODO: construct 5 random sentences
