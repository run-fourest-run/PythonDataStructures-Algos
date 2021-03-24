'''
Variable Scope:


Important to understand scoping rules of a variable inside functions. Each time a function executes new local namespace is created.
Python first searches the local namespace and if no match is found it will search the global namespace.



INTERESTING FIND
#############################################
so this was kind of an interesting find when I was doing this scoping excercise. But essentailly it looks like if you try to use a variable
defined outside the scope of a function it will be ok. However if you later define the variable in a statement inside the function it will result in an error.

var_a = 100
def scoping_example():
    var_b = var_a + 100
    var_a = 200
    print(var_b)

############################################


Keep an eye on the global keyword


'''


a = 'alex'
b = 'spencer'

def namespace_example():
    global a
    print('this is the value assigned to global a (before it is modified in the function): {}'.format(a))
    a = 'fournier' ; b = 'stall'
namespace_example()

print('this is the current value assigned to a: {}'.format(a))
print('this is the current value assigned to b: {}'.format(b))
