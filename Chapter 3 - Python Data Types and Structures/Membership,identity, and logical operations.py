'''
Membership operators (in, not in) test for variables in sequences, suchas lists or strings
* x in y returns True if a variable x is found in y.
* The is operator compares identity

'''


#Same elments in two different lists
x = [1,2,3,4]; y =[1,2,3,4]

print('equivilance:{}'.format(x == y))
print('identity:{}'.format(x is y))
x = y #assignment
print('after assignment:{}'.format(x is y))