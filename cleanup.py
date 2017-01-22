import sys
import re
import tokenize
import markov

with open('shakespear.txt', 'r') as corpus:
    corpus = corpus.read()

# print(clean_corpus(corpus))
# print(get_sentences(clean_corpus(corpus)))

def clean_corpus(corpus):
# clean_corpus = re.findall("\n *[A-Z][A-z]+\. (.+)", corpus)
    cleaner_corpus = re.findall(" *[A-Z][A-z]+\. (.+)", corpus)
    clean_string = ' '.join(cleaner_corpus)
    clean_string = re.sub("ELECTRONIC AND MACHINE READABLE COPIES MAY BE  PROHIBITED COMMERCIAL DISTRIBUTION INCLUDES BY ANY", "", clean_string)
    clean_string = re.sub("\[(.*?)\]", "", clean_string)
    return clean_string

# Takes in corpus, returnes list of sentences
def get_sentences(corpus):
    sentenceRegex = re.compile("[^.](.*?)[!.;?]")
    matches = sentenceRegex.findall(corpus)
    sentences = []
    for match in matches:
        sentences.append(match)
    return sentences

sentence_list = get_sentences(clean_corpus(corpus))
tokenized_sentence_list = tokenize.tokenize(sentence_list)

# print(markov.markov(tokenized_sentence_list))

fake_sentence = [["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]]
print(markov.generate_sentence(markov.markov(tokenized_sentence_list), 3))

# markov.markov(fake_sentence)
