def is_prime(n):
    import math
    flag = False
    div = math.floor(math.sqrt(n))
    if n > 1:
        for i in range(2, 1 + div):
            if (n % i) == 0:
                flag = True
                break
    else:
        print("False")
            
    if flag:
        print("False")
    else:
        print("True")
    
is_prime(1)    
is_prime(2)
is_prime(3)
is_prime(4)
is_prime(6)
is_prime(7)
is_prime(9)
is_prime(13)
is_prime(37)