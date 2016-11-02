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

def reverse_word(word):
    reversed_word = ""
    for i in range(len(word), 0, -1):
        reversed_word += word[i - 1]
    return reversed_word


if __name__ == '__main__':
    reversed_word = reverse_word("abcdefg")
    print reversed_word

    # randomized_words = rearrange_words(data)
    # print randomized_words
