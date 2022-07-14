def validate_pin(pin):

    import re
    pin = str(pin).strip()
    pattern1 = re.compile(r'^\d{4}$')
    pattern2 = re.compile(r'^\d{6}$')
    return bool(pattern1.fullmatch(pin)) or bool(pattern2.fullmatch(pin))


print(validate_pin('1234'))

# shorter:

# def validate_pin2(pin):
#   import re
#   return bool(re.fullmatch("\d{4}|\d{6}", pin))

# print(validate_pin('0918'))
