'''
Important to understand the internal mechanism that python
uses to copy them.

* Python creates real copies only if it has too
* When we assign the value of a variable to another variable, both of these variables
point to the same memory location. A new slot in memory will only be allocated if one
of those variables changes.
* This has important consequences for mutable compound objects



'''

x = 5; y = 10; z = 15
list_a = [x,y,z]
list_b  = list_a
list_b[1] = -10


'''
An important feature of lists is that they contain nested data structures:
'''

def demonstrate_nested_lists():
    items = [["rice",2.4,8],['flour',1.8,5],['Corn',4.7,6]]
    for item in items:
        print('Product:%s Price:%.2f,Quality:%i'% (item[0],item[1],item[2]))




def demonstrate_updating_nestedLists():
    items = [["rice", 2.4, 8], ['flour', 1.8, 5], ['Corn', 4.7, 6]]
    items[1][1] = items[1][1] * 2
    for item in items:
        print('Product:%s,Price:%.2f,Quantity:%i' % (item[0],item[1],item[2]))


demonstrate_updating_nestedLists()
