'''
Backtracking:

* A Form of recursion that is particularly useful for types of problems such as traversing tree structures, where we are presented
with a number of options at each node. From which we need to choose one. Subsequently presented with a new set of problems.
* Important to note that backtracking prunes branches that cannot give a result
'''


#all possible permutations of a string, s , of a given length n:
def bitStr(n,s):

        if n == 1: return s
        return [ digit + bits for digit in bitStr(1,s ) for bits in bitStr( n- 1,s) ]



