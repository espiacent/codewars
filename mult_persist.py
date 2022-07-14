def persistence(n):
    x = str(n)
    c = 0
    while len(x) > 1:
        r = 1
        for i in x:
            f = int(i)
            r *= f
        c += 1
        x = str(r)

    print("Multiplicative Persistence of " + str(n) + ":")
    return c


print(persistence(39))
print()
print(persistence(99))
print()
print(persistence(4))
print()
print(persistence(3279))
print()
print(persistence(77777733332222222222222222222))
