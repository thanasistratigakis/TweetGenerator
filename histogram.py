import sys

with open('book', 'r') as word_file:
    word_list = word_file.read().split(' ')

# returns histogram for a list of strings
def histogram(word_list):
    histogram = {}
    for word in word_list:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram

# returns list of strings with 1 as value for historam
def unique_words(histogram):
    unique_words = []
    for key, value in histogram.items():
        if value == 1:
            unique_words.append(key)
    return unique_words

# retunes value for string in histogram
def frequency(word, histogram):
    return histogram[word]

my_histogram = histogram(word_list)

print("######################################")
print("##########    histogram()   ##########")
print("######################################")
print(my_histogram)

print("######################################")
print("##########  unique_words()  ##########")
print("######################################")
print(unique_words(my_histogram))

print("######################################")
print("##########   frequency()    ##########")
print("######################################")
print(frequency('and', my_histogram))
