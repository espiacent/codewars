from collections import OrderedDict


class RomanNumerals:

    def to_roman(num):

        conversions = OrderedDict([('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
                                   ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)])
        out = ''
        for key, value in conversions.items():
            while num >= value:
                out += key
                num -= value
        return out

    def from_roman(roman):

        conversions = OrderedDict([('CM', 900), ('CD', 400), ('XC', 90), ('XL', 40), ('IX', 9), ('IV', 4), ('M', 1000), ('D', 500),
                                   ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1)])
        out = 0
        for key, value in conversions.items():
            out += value * roman.count(key)
            roman = str.replace(roman, key, "")
        return out


print(RomanNumerals.to_roman(1249))
print(RomanNumerals.from_roman("MCCXLIX"))
