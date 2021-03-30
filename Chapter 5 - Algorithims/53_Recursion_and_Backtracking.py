'''
Recurssion and Backtracking


At the heart of a recursive function there are two cases:

* Base Case - tells the recursion to end
* Recursive Case - Recalls the function they are in
* Recursive calls are stored in memory, whereas intration are not. This creates a trade off between
processor cyclea and memory usage. 
'''


def factorial(n):
    # test for base case
    if n==0:
        return 1
    f = n*factorial(n-1)
    print(f)
    return(f)

print(factorial(4))