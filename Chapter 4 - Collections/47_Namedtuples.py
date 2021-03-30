from collections import namedtuple
'''
namedtuple:

* method returns a tuple-like object that has fields accessible with named indexes as well as the integer indexes of normal tuples. This allows for code that is,
 to a certain extent self-documentating and more readable. 

* sounds useful if you have an application with a shitload of tuples and you need to keep track of them.

* probably could be useful if you are using a lot of database shit 

'''


space = namedtuple('space','x y z')
s1 = space(x=2.0,y=3,z=20)
volume = s1.x * s1.y * s1.z
print(volume)


'''
You can convert a named Tuple to a dict
'''

#recall that s1 is a named tuple
ordered_dict = s1._asdict()


'''
You can create a new instance of a named tuple with updated values... see example below

_namedtuple._replace()
'''

financial_data = namedtuple('financial','cash inventory ar' )
f1 = financial_data(cash=5000,inventory=500,ar=2000)
f2 = f1._replace(cash=1000)
