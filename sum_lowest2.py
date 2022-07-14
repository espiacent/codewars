def sum_two_smallest_numbers(numbers):
    numbers.sort()
    sum_numbers = numbers[0] + numbers[1]
    return(sum_numbers)


def sum_two_smallest_numbers2(numbers):
    return sum(sorted(numbers)[:2])


print(sum_two_smallest_numbers([33, 410, 3312, 300, 122, 325]))
print(sum_two_smallest_numbers2([3, 410, 3, 5, 2, 5]))
