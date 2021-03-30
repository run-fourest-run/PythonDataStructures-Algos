from collections import Counter

'''
Counter Objects:


* Counter is a subclass of Dictionary where each dictionary key is a hashable object and the associated value is an integer count of that object.
* There are three ways to intialize a counter. 
1). We can pass it any sequence object
2). a dictionary of key:value pairs
3). or a tuple of the format (object=value,)

'''

#sequence intialization
c1 = Counter('alexfournier')



#dictionary intiailization
c2 = Counter({"key":"value"})



#tuple --(object=value)
c3 = Counter(a=1,b=1,c=3)


'''
* You can also create an emtpy CounterObject and pass it a sequence via Counter.update()


'''

def demo_counter_update_method():
    counter = Counter('yeayeayea')
    print(counter)
    counter.update('yeayea')
    print(counter)
    print('Notice how Counter.update() will add to the value and not replace it')




def accessing_stored_values():
    '''
    Showing how to access Counter values and it's similarities to Dictionaries
    :return:
    '''
    counter = Counter('yeayeayeayea')
    for element in counter:
        print('%s %d' %(element,counter[element]))

'''
Noticeable difference with counter objects and dictionaries is that counter objects return a zero count for missing items rather than raising a key error.
For example:

'''


def demo_zero_return_if_no_key():
    print(c1['x']) # ---> This will return 0
    print(c1['r']) # --->? This will return 0
    print(c1['l']) # --> This will return 12


'''
We can create an iterator out of a Counter objec by using it's elements() method

'''

def create_counter_iterator():
    '''
    demonstrating how you can get an iterator. Having a hard time thinking of an applicable situation for this.
    :return:
    '''
    counter = Counter('yeayeayea')
    sorted_iterator  = sorted(counter.elements())
    print(sorted_iterator)



def counter_subtract():
    '''
    Demonstrating how counter.subtract works
    :return:
    '''
    counter = Counter('yeayeayea')
    print('this is counter: %s'% (counter))
    counter.subtract('yeayea')
    print('this is counter after subtract: %s'% (counter))


