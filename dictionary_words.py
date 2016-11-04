import random
import sys

text = sys.argv[1:][0]

# word_count = int(sys.argv[1:][0])

with open('words', 'r') as word_file:
    word_list = word_file.read().split('\n')

def generateRandomSentance(word_count, word_list):
    sentance_to_return = ''
    for num in range(0, word_count - 1):
        random_index = random.randint(0, len(word_list) - 1)
        sentance_to_return += word_list[random_index] + ' '
    return sentance_to_return

def autocomplete(text):
    suggestions = []
    for word in word_list:
        if text in word:
            suggestions.append(word)
    return suggestions

print(autocomplete(text))

# print(generateRandomSentance(word_count, word_list))
