import itertools
import string
import time


def guess_password(real):
    start = time.perf_counter()
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            if attempts % 100000000 == 0:
                print(f"{attempts:,}")
                print(guess)
            guess = ''.join(guess)
            if guess == real:
                end = round(time.perf_counter() - start)
                length = len(real)
                print('Time needed was roughly {:,} seconds for password with {} chars.'.format(
                    end, length))
                return 'Password is {} and was found in {:,} guesses.'.format(guess, attempts)


print(guess_password('auto123'))

# make this work with actual files like pdf?
# what about using generators?
