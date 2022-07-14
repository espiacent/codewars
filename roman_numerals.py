class RomanNumerals:

    def to_roman(val):
        # rule out edge cases
        if val == 0:
            return "0"
        elif val < 0:
            return "out of range --> low"
        elif val > 4000:
            return "out of range --> high"
        else:
            # get quotient and divider (divmod)
            thousand = divmod(val, 1000)
            hundred = divmod(thousand[1], 100)
            ten = divmod(hundred[1], 10)

            # get single digits
            one = thousand[0]
            print(one)
            two = hundred[0]
            print(two)
            three = ten[0]
            print(three)
            four = ten[1]
            print(four)

            # turn digits into numerals
            # thousand
            em = ("M" * one)

            # hundred
            if two == 0:
                ce = ""
            elif two < 5 and two != 4:
                ce = ("C" * two)
            elif two == 4:
                ce = ("CD")
            elif two == 5:
                ce = ("D")
            elif 5 < two < 9:
                ce = ("D" + ("C" * (two - 5)))
            elif two == 9:
                ce = ("CM")

            # ten
            if three == 0:
                ex = ""
            elif three < 5 and three != 4:
                ex = ("X" * three)
            elif three == 4:
                ex = ("XL")
            elif three == 5:
                ex = ("L")
            elif 5 < three < 9:
                ex = ("L" + ("X" * (three - 5)))
            elif three == 9:
                ex = ("XC")

            # one
            if four == 0:
                ei = ""
            elif four < 4:
                ei = ("I" * four)
            elif four == 4:
                ei = ("IV")
            elif four == 5:
                ei = ("V")
            elif 5 < four < 9:
                ei = ("V" + ("I" * (four - 5)))
            elif four == 9:
                ei = ("IX")

            # put together
            all = (em + ce + ex + ei)
            return all

    def from_roman(roman_num):
        substring = "MMMM"
        # rule out edge cases (not roman numeral and/or too long)
        roman_num_test = roman_num.upper()
        validRomanNumerals = ["M", "D", "C", "L", "X", "V", "I", "(", ")"]
        for letters in roman_num_test:
            if letters not in validRomanNumerals:
                return ("not a roman numeral")
            else:
                if roman_num == "":
                    return ""
                elif roman_num.startswith(substring) and (len(roman_num)) > 4:
                    return "out of range"
                else:
                    # calc start here
                    result = 0
                    if "CM" in roman_num:
                        result = 900
                        roman_num = roman_num.replace("CM", "")
                        print(result)
                        print(roman_num)
                    if "CD" in roman_num:
                        result += 400
                        roman_num = roman_num.replace("CD", "")
                        print(result)
                        print(roman_num)
                    if "XC" in roman_num:
                        result += 90
                        roman_num = roman_num.replace("XC", "")
                        print(result)
                        print(roman_num)
                    if "XL" in roman_num:
                        result += 40
                        roman_num = roman_num.replace("XL", "")
                        print(result)
                        print(roman_num)
                    if "IX" in roman_num:
                        result += 9
                        roman_num = roman_num.replace("IX", "")
                        print(result)
                        print(roman_num)
                    if "IV" in roman_num:
                        result += 4
                        roman_num = roman_num.replace("IV", "")
                        print(result)
                        print(roman_num)
                    if "D" in roman_num:
                        result += 500
                        roman_num = roman_num.replace("D", "")
                        print(result)
                        print(roman_num)
                    if "L" in roman_num:
                        result += 50
                        roman_num = roman_num.replace("L", "")
                        print(result)
                        print(roman_num)
                    if "V" in roman_num:
                        result += 5
                        roman_num = roman_num.replace("V", "")
                        print(result)
                        print(roman_num)

                times_m = roman_num.count("M")
                result += (1000 * times_m)
                print(result)

                times_c = roman_num.count("C")
                result += (100 * times_c)
                print(result)

                times_x = roman_num.count("X")
                result += (10 * times_x)
                print(result)

                times_i = roman_num.count("I")
                result += (1 * times_i)
                print(result)

                return(result)


print(RomanNumerals.to_roman(3847))
