from datetime import date



se_hire_dates = []
hire_date_anthony = date(year=2019,month=7,day=1)
hire_date_joe = date(year=2020,month=6,day=1)
hire_date_alexander = date(year=2020,month=8,day=23)
hire_date_brandon = date(year=2019,month=7,day=20)
se_hire_dates.append(hire_date_anthony);se_hire_dates.append(hire_date_alexander);se_hire_dates.append(hire_date_joe);se_hire_dates.append(hire_date_brandon)
string_hire_dates = [x.strftime('%m%d%Y') for x in se_hire_dates]
sales_engineers = ['Alexander','Anthony','Joeseph','Brandon']

sales_engineers_dict = {k:v for k,v in zip(sales_engineers,string_hire_dates)}
print(sales_engineers_dict)
second_dict = sales_engineers_dict.copy()


'''
Sorting Dictionaries:

If we want to do a simple sort on either keys or values of a dictionary we can use the following:


*  The key argument has nothing to do with the dictionary keys, but rather is a way of passing a function to the sort algorithm to determine the sort order


'''

#Returns ['Alexander', 'Anthony', 'Brandon', 'Joeseph']
sorted_names = sorted(list(sales_engineers_dict))

#Returns ['06012020', '07012019', '07202019', '08232020']
sorted_hire_dates = sorted(list(sales_engineers_dict.values()))

#This uses a list comprehension
sorting_example = [(key,value) for (key,value) in sorted(sales_engineers_dict.items(),reverse=True)]
print(sorting_example)


#new dictionary
'''
task is to print these in the correct order. Beacause all keys and values are strings, we have no context for numerical ordering.To place these
items in correct order, we need to use the first dictionary we created, mapping words to numerals as a way to order our English to French Dict
'''



d ={'one': 1 , 'two': 2, 'three': 3 ,'four':4,'five':5,'six':6}
d2 ={'one':'uno' , 'two':'deux', 'three':'trois', 'four': 'quatre', 'five': 'cinq', 'six':'six'}
sorted_d2 = sorted(d2,key=d.__getitem__)