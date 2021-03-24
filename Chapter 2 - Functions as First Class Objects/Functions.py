'''
In Python, as we know, functions and classes are known as first class objects.
This means:

* Created at Runtime
* assigned as a variable or data structure
* Can be passed as an arguement to a function
* Returned as a result of a function
'''


def greeting(language):
    if language == 'eng':
        return 'hello world'
    if language == 'fr':
        return 'Bonjour'
    else:
        return 'language not supported'


example_list= [greeting('eng'), greeting('fr'),greeting('german')]
example_list_comprehension = [greeting(x) for x in ['eng','fr','ger']]
print(example_list)
print(example_list_comprehension)