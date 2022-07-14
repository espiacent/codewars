string_input = input("Enter strings:")


def xo(chars):
    count_x = 0
    count_o = 0
    search_x = 'x'
    search_o = 'o'

    chars = chars.lower()
    list(chars)

    for x in chars:
        if search_x in x:
            count_x = count_x + 1
    for o in chars:
        if search_o in o:
            count_o = count_o + 1

    if count_x == count_o:
        return True
    if count_x != count_o:
        return False


print(xo(string_input))
