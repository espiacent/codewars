import time


def disemvowel0(string):
    start_time = time.time()
    vowels = ["a", "u", "e", "i", "o"]
    new_string = []
    for char in string:
        if char.lower() not in vowels:
            new_string.append(char)
    string = "".join(new_string)
    print(time.time() - start_time)
    print("time using for, creating and joining a list")


def disemvowel(string):
    start_time = time.time()
    read = 0
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    while read < len(string):
        if not string[read] in vowels:
            read += 1
        else:
            string = string.replace(string[read], "")
    print(time.time() - start_time)
    print("time using while and replacing vowels with '' at string")


def disemvowel1(string):
    start_time = time.time()
    "".join(c for c in string if c.lower() not in "aeiou")
    print(time.time() - start_time)
    print("time using c.lower")


def disemvowel2(string):
    start_time = time.time()
    "".join(c for c in string if c not in 'aeiouAEIOU')
    print(time.time() - start_time)
    print("time using 'aeiouAEIOU'")


def disemvowel3(string_):
    start_time = time.time()
    transt = dict.fromkeys(map(ord, 'aeiouAEIOU'), None)
    string_t = string_.translate(transt)
    print(time.time() - start_time)
    print("time using translation table with aeiouAEIOU")


sentence = "a"*(10**8) + "b"*(10**8) + "e"*(10**8)

disemvowel0(sentence)
disemvowel(sentence)
disemvowel1(sentence)
disemvowel2(sentence)
disemvowel3(sentence)
