from datetime import date
'''
Dictionaries:

Are arbitrary collections indexed by numbers, strings or immutable objects. Dictionaries themselves are mutable. However their index key is immutable.
The following are all of the dictionary methods:


* only built in mapping type and they are similar to hash tables or associative arrays in other languages
* They can be thought of as a mapping from a set of a keys to a set of values. 
* They are created using the {key:value} syntax. 

'''



first_example_dict = {0:'zero',1:'one',2:"two"}

#We can add keys and values as follows
first_example_dict[3] = 'three'

#or updating multiple values using the following syntax:
first_example_dict.update({4:'four',5:'five'})




def test_occurence(var,dict):
    return var in dict

#we can test for this occurence of a value in a dict --> it returns True if key matches
is_it_in_question = 5 in dict
#print(test_occurence(5,first_example_dict))











'''
Instantiating some dummy dictionaries to demonstrate methods below
'''



se_hire_dates = []
hire_date_anthony = date(year=2019,month=7,day=1)
hire_date_joe = date(year=2020,month=6,day=1)
hire_date_alexander = date(year=2020,month=8,day=23)
hire_date_brandon = date(year=2019,month=7,day=20)
se_hire_dates.append(hire_date_anthony);se_hire_dates.append(hire_date_alexander);se_hire_dates.append(hire_date_joe);se_hire_dates.append(hire_date_brandon)
sales_engineers = ['Alexander','Anthony','Joeseph','Brandon']

hire_date = []
index_on_hire_date_engineers = {x:'sales_engineer_%s'%(v) for x,v in zip(se_hire_dates,sales_engineers)}
indexed_engineers = {x:v for x,v in enumerate(sales_engineers)}
other_indexed_engineer = {'sandy':'Alan'}






















'''
Dictionary Methods!!!


See below:
* Length
* Copy
* Clear
* FromKeys
* Keys 
* Values
* Pop
* PopItem
* Update
* SetDefault



'''
#len(d)
#Returns the Length
length_of_engineers = len(indexed_engineers)

#d.copy()
#shallow copy
copy_of_engineers = indexed_engineers.copy()

#d.clear()
#Removes all items
remove_all_engineers = copy_of_engineers.clear()


#d.fromkeys()
#Returns a new dictionary with keys from sequence s and values set to value --? I don't really understand what is happening here
newly_indexed_engineers = indexed_engineers.fromkeys(index_on_hire_date_engineers)

#d.items()
#Returns a sequence of keys and values
items = indexed_engineers.items()

#d.keys()
# returns a sequence of keys
keys = indexed_engineers.keys()

#d.pop()
# returns d[k]] and removes it from d. If k is not found it returns default of returns KeyError
#print(indexed_engineers)
remove_brandon = indexed_engineers.pop(3)
#print(indexed_engineers)

#d.popitem()
#removes a random key:value pair
remove_random = indexed_engineers.popitem()


#d.setdefault() --> I don't understand this one
# returns d[k]. if d[k] is not found it returns v and sets d[k] to value

#d.update()
#updates all objects from dictionary a to d --> keys apparently don't need to confom whatsoever
adding_dicts = indexed_engineers.update(other_indexed_engineer)
#print(indexed_engineers)



#d.values()
#Returns a sequence of values (a list of values)
values = indexed_engineers.values()
#print(values)