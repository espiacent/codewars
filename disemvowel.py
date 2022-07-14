def disemvowel(string_):
    transt = dict.fromkeys(map(ord, 'aeiouAEIOU'), None)
    string_t = string_.translate(transt)
    return string_t


print(disemvowel("This website is for losers LOL!"))
