from collections import OrderedDict

'''
The important thing about ordered dictionaries is that they remember the insertion order, so when we iterate over them,
they return values in the order they were inserted

* This is in contrast to a normal dictionary, where the order is arbitrary. 
* When we test to see whether two dictionaries are equal, this equality is only based on their keys and values.
* But this equality test extends in Ordered Dicts. So if I compared two ordered dicts then the order needs to also be the same, else Returning False, Bitch!

'''

ordered_dict = OrderedDict()
ordered_dict['one'] = 1
ordered_dict['two'] = 2
ordered_dict['three'] = 3
ordered_dict2 = OrderedDict()
ordered_dict2['one'] = 1
ordered_dict2['three'] = 3
ordered_dict2['two'] = 2

def test_equality(ordered_dict,ordered_dict2):
    print(ordered_dict == ordered_dict2)
    print('It will print False - Since the dicts are not in the same order')



'''
When we add values from a list using .update(), The ordered dict will retain the same order
as the list
'''

kvs = [('four',4),('five',5),('six',6)]
ordered_dict.update(kvs)


'''
Ordered Dict is often used in conjunction with the sorted method to create a sorted dictionary


'''

#Numerical expressions to sort integer values
#The lambda takes a type of list as it's anonymous arguement: It performs a numerical
#expression against the second index of the list
ordered_dict_sorted = OrderedDict(sorted(ordered_dict.items(),key=lambda t:  (4* t[1]) - t[1] ** 2))




def print_numerical_expression_in_lambda():

    '''trying to understand the OrderedDict above'''

    for v in ordered_dict.values():
        print(f'4 * {v} == {4 * v}')

    for v in ordered_dict.values():
        print(f'2**{v} == {2 ** v}')