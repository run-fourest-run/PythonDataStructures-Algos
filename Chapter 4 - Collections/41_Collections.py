from collections import namedtuple,deque,ChainMap,Counter,OrderedDict,defaultdict


'''
High level:

The collections module provides more specialized, high performance alternatives for the built-in data types as well as a utility
function to create named tuples. 

'''



#namedtuple()
#Creats a tuple subclass with named fields
#basically easy to create lightweight object types
Point = namedtuple('Point','x y')
pt1 = Point(1.0,2)
pt2 = Point(2.0,3)
print(pt2)


#deque
#lists with fast appends and pops either end





#ChainMap
#Dictionary like class to create a single view of multiple mappings




#Counter
#Dictionary subclass for counting hashable objects


#OrderedDict
#Dictionary subclass that remembers the entry order



#defaultdict
#dictionary subclass that calls a function to supply missing values

