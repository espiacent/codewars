def odd_triangle(n):
    # edge case
    if n == 1:
        return 1
    # get length of list
    lst = []
    counter_a = 0
    base = 0
    while counter_a < n:
        base = base + 1
        lst.append(base)
        counter_a = counter_a + 1
    length_triangle = sum(lst)

# generate list of odd numbers of this length
    counter_b = 0
    next = 1
    odd_numbers = []
    while counter_b < length_triangle:
        next = next + 2
        odd_numbers.append(next)
        counter_b = counter_b + 1
    final_list = odd_numbers[-n-1:-1]
    return sum(final_list)


print("My Solution:")
print(odd_triangle(1))
print(odd_triangle(2))
print(odd_triangle(3))
print(odd_triangle(4))
print(odd_triangle(5))
print(odd_triangle(7))
print(odd_triangle(12))
print()


def odd_triangle2(n):
    # your code here
    return n ** 3


print("Easy/short solution:")
print(odd_triangle2(1))
print(odd_triangle2(2))
print(odd_triangle2(3))
print(odd_triangle2(4))
print(odd_triangle2(5))
print(odd_triangle2(7))
print(odd_triangle2(12))
