import itertools
import string

alphabet = string.ascii_lowercase

result = list(itertools.product(alphabet, alphabet))

for x,y in result:
    if x != y:
        print(x+y)