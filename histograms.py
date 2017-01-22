#!python
from __future__ import division, print_function
import random


class Dictogram(dict):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Dictogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        self.histogram = {}
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            if item in self:
                self[item] += 1
            else:
                self[item] = 1
            pass

    def add(self, item):
        """Insert a single item to this histogram"""
        if item in self.keys():
            self[item] += 1
        else:
            self[item] = 1
            self.types += 1
        self.tokens += 1

    # def random_word(self):
    #     """Retuns a random word"""
    #     start_value = 0
    #     tuple_list = []
    #     # assign space on numberline for each element (add weight)
    #     for key, value in self.items():
    #         new_tuple = (key, start_value, start_value + value - 1)
    #         tuple_list.append(new_tuple)
    #         start_value += value
    #
    #     # get random int between 0 and token count
    #     random_int = random.randint(0, self.tokens - 1)
    #     for tup in tuple_list:
    #         # if random number falls between range, return that key
    #         if random_int >= tup[1] and random_int <= tup[2]:
    #             return tup[0]


    def random_word(self):
        """Return a 'random' word weighted based on occurance"""
        temp_value = 0
        tuple_list = []
        for key, value in self.items():
            # print(value)
            new_tuple = (key, temp_value, temp_value + value - 1)
            tuple_list.append(new_tuple)
            temp_value += value
        print(self.tokens)
        random_int = random.randint(0, self.tokens - 1)
        for i in tuple_list:
            if random_int >= i[1] and random_int <= i[2]:
                return i[0]




    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        return self[item]
        pass


class Listogram(list):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new list; update with given items"""
        super(Listogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            if self.__contains__(item):
                print("update")
                index = self._index(item)
                self[index][1] += 1
            else:
                new_word = [item, 1]
                self.append(new_word)
                self.types += 1
                print("append")
            self.tokens += 1
        pass

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        index = self._index(item)
        if index > -1:
            return self[index][1]
        else:
            return 0
        pass

    def __contains__(self, item):
        """Return True if the given item is in this histogram, or False"""
        for thing in self:
            if thing[0] == item:
                return True

        return False
        pass

    def _index(self, target):
        """Return the index of the (target, count) entry if found, or None"""
        # linear search to find an item's index
        for index, item in enumerate(self):
            if item[0] == target:
                return index
                print("found")
        return -1
        pass


def test_histogram(text_list):
    print('text list:', text_list)

    hist_dict = Dictogram(text_list)
    print('dictogram:', hist_dict)

    hist_list = Listogram(text_list)
    print('listogram:', hist_list)


def read_from_file(filename):
    """Parse the given file into a list of strings, separated by seperator."""
    return file(filename).read().strip().split()


if __name__ == '__main__':
    import sys
    arguments = sys.argv[1:]  # exclude script name in first argument
    if len(arguments) == 0:
        # test hisogram on letters in a word
        word = 'abracadabra'
        test_histogram(word)
        print()
        # test hisogram on words in a sentence
        sentence = 'one fish two fish red fish blue fish'
        word_list = sentence.split()
        test_histogram(word_list)
    elif len(arguments) == 1:
        # test hisogram on text from a file
        filename = arguments[0]
        text_list = read_from_file(filename)
        test_histogram(text_list)
    else:
        # test hisogram on given arguments
        test_histogram(arguments)
