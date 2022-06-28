
def duplicate_encode2(word):
    l = word.lower()
    freq = [l.count(ele) for ele in l]
    d = dict(zip(l, freq))
    generic = dict((k, v) for k, v in d.items() if v == 1)
    for k in generic: generic[k] = "("  
    unique = dict((k, v) for k, v in d.items() if v > 1)
    for k in unique: unique[k] = ")"
    generic.update(unique)
    table = l.maketrans(generic)
    return (l.translate(table))

print(duplicate_encode2('din'))
print(duplicate_encode2('recede'))