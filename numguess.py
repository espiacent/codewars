import time

fname = input('What ist your first name?')
lname = input('What ist your last name?')

name =f'{fname} {lname}'
print(f'Hello, {name.title()}!')
print("Let's play a number guessing game!")

solution = 42

while True:
    try:
        number = int(input('Guess the number:'))
    except:
        print('Not a number.')
        print()
        time.sleep(2)
        continue

    if number < 42:
        time.sleep(1)
        print('Too low. Guess again.')
        time.sleep(1)
        continue
    elif number > 42:
        time.sleep(1)
        print('Too high. Guess again.')
        time.sleep(1)
        continue
    else:
        time.sleep(1)
        print('Correct!')
        break