from random import randint
import sys

text = sys.argv[1:][0]

word_count = int(sys.argv[1])

with open('words', 'r') as word_file:
    word_list = word_file.read().split('\n')

def generateRandomSentence(word_count, word_list):
    sentance_to_return = []
    word_list_count = len(word_list) - 1
    for num in range(0, word_count - 1):
        random_index = random.randint(0, word_list_count)
        sentance_to_return.append(word_list[random_index])
    return (' '.join(sentance_to_return) + '.')

def autocomplete(text):
    suggestions = []
    for word in word_list:
        if len(word) > len(text):
            if word.startswith(text):
                suggestions.append(word)
    return suggestions

print(autocomplete(text))

# print(generateRandomSentence(word_count, word_list))
