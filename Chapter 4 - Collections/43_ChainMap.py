from collections import ChainMap
from datetime import date
import os

'''
ChainMap class was added in Python 3.2 and provides a way to link a number of dictionaries or other mappings so they can be treated as one object.

* map attribute, new_child() method and parents property
* underlying mappings for ChainMap are stored in a list and are accessable through map[i] attribute to retrieve the nth dictionary
* Underlying Dictionaries are unordered - but ChainMAPs are an ordered list of dictionaries
* useful in applications where you are using dictionaries with related data
* typically used to simulate nested contexts such as when we have multiple overriding configuraion settings.e

'''
###probably not the best example


#Example 1
se_hire_dates = [date(year=2020,month=6,day=1),date(year=2019,month=8,day=22),date(year=2019,month=7,day=1)]
se_hire_string_dates = [x.strftime('%d%m%Y') for x in se_hire_dates]
se_names = ['Joe','Alexander','Anthony']


ae_hire_dates = [date(year=2019,month=7,day=20),date(year=2020,month=6,day=1),date(year=2021,month=4,day=3)]
ae_hire_string_dates = [x.strftime('%d%m%Y') for x in ae_hire_dates]
ae_names = ('Chris','Dan','Troy')

se_dict = {(k,v) for k,v in enumerate(zip(se_hire_string_dates,se_names))}
ae_dict = {(k,v) for k,v in zip(ae_hire_string_dates,se_names)}


def hires_on_date(*employee_dicts):
    chainmap = ChainMap(employee_dicts)
    return chainmap





#Example 2


def chainmap_environment_variables():
    vars = {k:v for k,v in os.environ.items()}
    cmap = ChainMap(vars)
    for k,v in cmap.items():
        if k == 'AWS_DEFAULT_REGION':
            cm2 = cmap.new_child({k:'us-east-1'})
    return cm2.maps


print(chainmap_environment_variables())

'''
Advantages of ChainMap

1). retain previously set values.
2). Adding a child context overrides values for the same key, but does not remove them from the data structure. 
* Useful for when we may need to keep a record of changes so that we can easily roll back on a previous setting


'''