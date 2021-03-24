import time
'''
Generators and co-routines

Generators:
* Returns not just one result but rather entire sequence of results
* easy way to create iterators
* especialy useful as replacement for unworkably long lists. 
* yields items rather than building list
* you can use generator expressions (Similar syntax to list comprehensions)
* generators create data on demand. So they don't support sequence operations 
(like append)


'''



#Compare the running time of a list compared to a generator

#Generator function - creates an iterator of odd numbers between n,m

def oddGen(n,m):
    while n < m :
        yield n
        n += 2

#builds a list of odd numbers between n & m

def oddLst(n,m):
    lst = []
    while n < m:
        lst.append(n)
        n +=2
    return lst

# time it takes tob build generator
t = time.time()

sum(oddGen(1,10000000))

print('this is the sum of an iterator: %f' % (time.time() - t))

#time it takes to build list

t = time.time()

sum(oddLst(1,10000000))
print('this sum the sum of a list %f' % (time.time() - t))
