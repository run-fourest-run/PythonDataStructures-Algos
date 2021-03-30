from collections import deque
from itertools import islice
'''
Deques:

Double ended queues or deques (usually pronounced decks), are list-like objects
* support thread safe, memory efficient appends
* mutable
* support some list operations - like indexing


** major advantage of deques is inserting something at the beginning is much faster than using a list. 
* inserting at the end is fractionally less performant than with lists.



Best way to think about them: populating and consuming Items!

'''

test_deque = deque(range(10)) #Instantiating deque
test_deque.append(11) #adding element to the right
test_deque.appendleft(0) #adding element to the left
test_deque.extend('eff') #adds multiple items to right
test_deque.extendleft('aaa') #adds multiple items to the beginning of the list
print(test_deque)


'''
we can use pop() & popleft() to consume elements on either side of the deque
'''
print(test_deque)
pop = test_deque.pop()
pop_left = test_deque.popleft()
print(test_deque)



'''
an easy way to slice deques

itertools.islice()

'''


deque_sliced = list(islice(test_deque,3,4))



'''
Another useful feature of deques is the optional maxlen parameter that restricts the size of the deque.

This makes it ideally suited to a data structure known as a circular buff


circular buff:
Fixed sized structure that is effectively connected end to end and they are typically used for buffering data streams. The following is a basic example:


typically used for buffering data strueams:
'''


def circular_buff():
    circular_buff = deque([],maxlen=10)
    for i in range(20):
        circular_buff.append(i)
        print(circular_buff)

circular_buff()