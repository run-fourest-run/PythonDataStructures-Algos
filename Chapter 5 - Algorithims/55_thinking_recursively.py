from math import log10, ceil
'''
Python implementation of Karatsuba algo -

Demoing Recursion. 

I really am totally lost here. 

'''


def karasuba(x,y):
    # the base case for recursion
    if x < 10 or y < 10:
        return x*y

    # sets n, the number of digits of the highest input
    n = max(int(log10(x) + 1 ), int(log10(y) + 1))

    #routs up n/2
    n_2 = int(ceil(n / 2.0))

    #adds 1 if n is uneven
    n = n if n % 2 == 0 else n + 1

    a, b = divmod(x, 10**n_2)
    c, d = divmod(y, 10**n_2)

    #applies the three recursive steps
    ac = karasuba(a,c)
    bd = karasuba(b,d)
    ad_bc = karasuba((a+b),(c+d)) - ac - bd

    #performs the multiplication

    return (((10**n) *ac) + bd + ((10**n_2)*(ad_bc)))

