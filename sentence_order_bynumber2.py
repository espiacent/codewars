def order(words):
    return ' '.join(sorted(words.split(), key=lambda w: sorted(w)))


def order2(sentence):
    if not sentence:
        return ""
    result = []  # the list that will eventually become our setence

    split_up = sentence.split()  # the original sentence turned into a list

    for i in range(1, 10):
        for item in split_up:
            if str(i) in item:
                # adds them in numerical order since it cycles through i first
                result.append(item)

    return " ".join(result)
