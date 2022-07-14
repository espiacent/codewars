import time


def tribonacci(signature, n):
    start_time = time.time()
    if n == 0:
        signature.clear()
        print(signature)
        return(signature)
    elif n == 1:
        del signature[1:]
        print(signature)
        return(signature)
    elif n == 2:
        print(signature[0:2])
        return(signature[0:2])
    elif n == 3:
        print(signature)
        return(signature)
    else:
        n = n - 3
        counter_all = 1
        first = sum(signature)
        signature.append(first)
        counter_sub = 0
        while counter_all < n:
            counter_all = counter_all + 1
            counter_sub = counter_sub + 1
            list_cache = signature[counter_sub:]
            sum_cache = sum(list_cache)
            signature.append(sum_cache)
        # print(signature)
        print(time.time() - start_time)
        return(signature)


tribonacci([1, 2, 3], 250000)
