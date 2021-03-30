from collections import defaultdict,OrderedDict

'''
defaultdict

* subclass of dict --> So it will share the same operations
* Acts as a convient way to intialize dictionaries
* default dictionary overrides one method, __missing__(key), and creates a new instance variable, default_factory.
* With default dict rather than throw an error, it will run the function, supplied as default_factory arguement, which will generate the value

'''


'''
simple use of default dicts is to set default_factory to int to get a quick count of dicts
'''


def isprimary(color):
    if (color=='red') or (color=='blue') or (color=='green'):
        return True
    else:
        return False

demo_defaultdict = defaultdict(bool)
words = ['red','orange','mango','brown']
for word in words:
    demo_defaultdict[word] = isprimary(word)

print(demo_defaultdict)