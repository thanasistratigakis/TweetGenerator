import random
import sys

word_count = int(sys.argv[1:][0])

with open('words', 'r') as word_file:
    word_list = word_file.read().split('\n')

def generateRandomSentance(word_count, word_list):
    sentance_to_return = ''
    for num in range(0, word_count - 1):
        random_index = random.randint(0, len(word_list) - 1)
        sentance_to_return += word_list[random_index] + ' '
    return sentance_to_return

print(generateRandomSentance(word_count, word_list))
