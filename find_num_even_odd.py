number = input("Enter number:")
try:
    number = int(number)
except:
    print("Not a number.")
    raise SystemExit
if number % 2 == 0:
    print("Number is even.")
else:
    print("Number is uneven.")