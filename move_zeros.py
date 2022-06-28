def move_zeros(array):
    lst_zeros = [i for i in array if i == 0]
    lst_rest = [i for i in array if not i == 0]
    for zero in lst_zeros:
        lst_rest.append(zero)
    return lst_rest

print(move_zeros([1, 2, 0, 4, 0, 5, 10]))