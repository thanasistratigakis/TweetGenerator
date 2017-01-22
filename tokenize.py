import re

# Splits up Strings into tokens
def tokenize(text):
    if not isinstance(text, basestring):
        tokens = []
        for sentence in text:
            tokens.append(tokenize(sentence))
        return tokens
    else:
        no_punc_text = remove_punctuation(text)
        tokens = split_on_whitespace(no_punc_text)
        return tokens

# Separates words
def split_on_whitespace(text):
    return re.split('\s+', text)

# Removes punctuation
def remove_punctuation(text):
    no_punc_text = re.sub('[,.()]', '', text)
    no_punc_text = re.sub('--', ' ', no_punc_text)
    return no_punc_text
