chars = input("Input x's and o's:").lower()

if len(chars) < 1:
    chars = ['x', 'x', 'x', 'o', 'o', 'o']

else:
    def split(chars):
        return list(chars)
     
print(chars)

count_x = 0
count_o = 0

search_x = 'x'
search_o = 'o'

for x in chars:
    if search_x in x:
        count_x = count_x + 1
for x in chars:
    if search_o in x:
        count_o = count_o + 1

if count_x == count_o:
    y = True
    print(bool(y))
if count_x != count_o:
    y = False
    print(bool(y))