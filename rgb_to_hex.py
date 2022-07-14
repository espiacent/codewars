def rgb_test(r, g, b):
    # edge case = min or max rgb values
    if r <= 0:
        r = 0
    elif r >= 255:
        r = 255

    if g <= 0:
        g = 0
    elif g >= 255:
        g = 255

    if b <= 0:
        b = 0
    elif b >= 255:
        b = 255

    # getting hex code from numbers
    num_1 = int(r / 16)
    num_2 = (r % 16)

    hex_1 = hex(num_1)
    hex_2 = hex(num_2)

    num_3 = int(g / 16)
    num_4 = (g % 16)

    hex_3 = hex(num_3)
    hex_4 = hex(num_4)

    num_5 = int(b / 16)
    num_6 = (b % 16)

    hex_5 = hex(num_5)
    hex_6 = hex(num_6)

    return (hex_1[2:] + hex_2[2:] + hex_3[2:] + hex_4[2:] + hex_5[2:] + hex_6[2:]).upper()


print(rgb_test(255, 255, 255))
print(rgb_test(-20, 255, 255))
print(rgb_test(500, 200, 10))
