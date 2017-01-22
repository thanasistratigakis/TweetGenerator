import histograms

# Generates markov model for a tokenized list of sentences
def markov(tokenized_sentence_list):
    model = histograms.Dictogram()
    order = 3

    initial_key = []
    for i in range(0, order - 1):
        initial_key.append(None)
    initial_key.append("--start--")

    for sentence in tokenized_sentence_list:
        history = []
        for i in range(0, order - 1):
            history.append(None)
        history.append("--start--")

        for index in range(0, len(sentence)):
            key = tuple(history)
            if key in model:
                model[key].add(sentence[index])
            else:
                model[key] = histograms.Dictogram()
                model[key].add(sentence[index])

            # Shift array
            del history[0]
            history.append(sentence[index])
        key = tuple(history)
        if model.get(key) is None:
            model[key] = histograms.Dictogram()
            model[key].add("--end--")

    # print(model)
    return model






    # for plain_sentence in tokenized_sentence_list:
    #     # plain_sentence.append(""--start--"")
    #     sentence = ["--start--"]
    #     sentence.extend(plain_sentence)
    #     # sentence.insert(0, "--start--")
    #     sentence.append("--end--")
    #     # print(sentence)
    #     histogram = histograms.Dictogram()
    #
    #     first_key = []
    #     for n in range(0, order):
    #         first_key.append("--start--")
    #     first_key = tuple(first_key)
    #     model[first_key] = histograms.Dictogram()
    #     model[first_key].add(sentence[order - 1])
    #
    #     for index in range(0, len(sentence) - order):
    #
    #         history_list = []
    #
    #         for i in range(0, order):
    #             history_list.append(sentence[index + i])
    #         history_tuple = tuple(history_list)
    #
    #         if history_tuple in model:
    #             model[history_tuple].update([sentence[index + order]])
    #         else:
    #             model[history_tuple] = histograms.Dictogram()
    #             model[history_tuple].add(sentence[index + order])
    #
    # # print(model)
    # sentence = generate_sentence(model, order)
    # print(sentence)
    # return model


# Pass in markov model and sentence as list of strings
def generate_sentence(model, order):
    sentence = []
    key = []

    for i in range(0, order - 1):
        key.append(None)
    key.append("--start--")
    key = tuple(key)

    word = "--start--"

    while True:
        word = model[key].random_word()
        print(word)
        if word == "--end--":
            break
        sentence.append(word)

        key = list(key)
        del key[0]
        key.append(word)

        key = tuple(key)
        print(key)
    return sentence








    #
