

'''demonstrating variables and expressions

Basically:

* Variables are just pointers to specific objects

'''


#Variable example
list_a = list(range(10))

def def_dynamic_type_example_with_Variables(var_a):
    '''
    This function is supposed to illustrate that different variables point to the same underlying object
    :param var_a:
    :return:
    '''
    var_b = var_a
    print('this is var_a:{}\n'.format(var_a),'this is var_b:{}\n'.format(var_b))
    var_a.append(10)
    print('this is var_a (after append):{}\n'.format(var_a),'this is var_b (after append):{}\n'.format(var_b))
    print('I think both variables will be {}'.format('[1,2,3,4,5,6,7,8,9,10]'))

def_dynamic_type_example_with_Variables(list_a)


#This is a little unexpected to me. ---> This was solved by someone on reddit. It is because
def show_mutating_types(val:int):
    '''
    This is supposed to illustrate that types can mutate when changing a variable.
    :param val:
    :return:
    '''
    print('this is the initial type of val: {}'.format(type(val)))
    var_val2 = val
    val=val+.01
    print('this is the type of val after the addition operation: {}'.format(type(val)))
    print('this is the type of var_val2 after the addition operation: {}'.format(type(var_val2))) #------> this was inititally unexpexted it's because


val = 1
show_mutating_types(val)