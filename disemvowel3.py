def disemvowel(string):
    for char in "aeiouAEIOU":
        string = string.replace(char, '')
    return string


print(disemvowel("This website is for losers, LOL!"))
