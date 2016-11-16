import random
import sys
import histogram

with open('words', 'r') as word_file:
    word_list = word_file.read().split('\n')

my_histogram = histogram.histogram(word_list)

# weighted words are tupples ('word', starting_range, ending_range)
def getWeightedWords(histogram):
    current_range_value = 0
    weighted_words = []
    for word, frequency in histogram.items():
        new_current_range_value = current_range_value + frequency
        weighted_word = (word, current_range_value, new_current_range_value)
        current_range_value = new_current_range_value
        weighted_words.append(weighted_word)
        # print(weighted_word)
    return weighted_words

def generateRandomSentence(histogram):
    sentence = []
    for i in range(0, 10):
        weighted_words = getWeightedWords(histogram)
        rand_index = random.randint(0, len(word_list))
        for value in weighted_words:
            if value[1] <= rand_index and value[2] >= rand_index:
                sentence.append(value[0])
                break
    sentence_as_string = " ".join(sentence)
    return sentence_as_string

def sentence():
    sentence = generateRandomSentence(my_histogram)
    return sentence

# print(generateRandomSentence(my_histogram))
