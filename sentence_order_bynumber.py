def order(sentence):
    import re
    try:
        #split string to list and compile re pattern
        lst = sentence.split()
        pattern = re.compile(r'[1-9]')
        #find numbers in list
        for item in sentence:
            match = pattern.findall(sentence)
        #make dictionary from matches and original list
        dic = dict(zip(match, lst))
        #make dictionary to list of tuples and sort by first items (the numbers)
        list_new = sorted(list(dic.items()))
        result = []
        #append second items of tuple to list then join list to string to get result
        for item in list_new:
            result.append(item[1])
        result2 = ' '.join(result)
        return result2
    except:
        return ""

print(order("4of Fo1r pe6ople g3ood th5e the2"))
print(order(""))
