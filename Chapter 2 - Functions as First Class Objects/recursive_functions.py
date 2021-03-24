'''
Recursion is one of the most fundamental concepts in CS!

* We implement a recursive function in python simply by calling it within it's own function
body.

* To stop the recursive function from turning into an infinate loop,
we need at least one arguement that tests for a terminating case to the end of recursive
function.

* This is sometimes called the base case.

* Recursion is different from iteration. Although both involve repetition...

* Difference is iteration loops through a sequence

* Recursion repeadely calls a function

* Both need a selection statement to end

* Technical recursion is a special kind of iteration known as tail iteration

* Interesting thing about recursive functions is that they are able to describe an infinite
object within a finite statement

* General note: Iteration is more efficient but Recrusive function are easier to write and understand

* Recursive functions are also useful in manipulating recursive data structures
like linked lists or trees









'''



def iterTest(low,high):
    while low <= high:
        print(low)
        low = low+1

def recurTest(low,high):
    if low<=high:
        print(low)
        recurTest(low+1,high)


high=5
low=1

iterTest(low,high)
recurTest(low,high)