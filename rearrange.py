import random
import sys

data = sys.argv[1:]

def rearrange_words(words):
    new_word_list = []
    for i in range(0, len(data)):
        rand_index = random.randint(0, len(words) - 1)
        new_word_list.append(words[rand_index])
        del data[rand_index]
    return new_word_list

if __name__ == '__main__':
    randomized_words = rearrange_words(data)
    print randomized_words
