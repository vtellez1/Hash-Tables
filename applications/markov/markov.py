import random

wordbank = {}
#wordbank.setdefault(key, []).append(value)

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
list_of_words = words.split()

for i in range(0, len(list_of_words) - 1):
    #print(list_of_words[i])
    if list_of_words[i] not in wordbank:
        wordbank.setdefault([list_of_words[i]], []).append(list_of_words[i+1])

print(wordbank)
#print(wordbank)
# TODO: construct 5 random sentences
