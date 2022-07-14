def sum_primes(n):
    lst = []
    if n > 1:
        for i in range(3, n):
            if (n % i) == 0:
                lst.append(i)
                print(lst)
    print(sum(lst))


sum_primes(2)
sum_primes(5)
sum_primes(39)

# hackinscience
