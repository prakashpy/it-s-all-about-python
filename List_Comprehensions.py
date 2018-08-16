### List comprehensions is a concise way to create lists.

# syntax: *result*  = [*transform*    *iteration*         *filter*     ]
# Example: my_new_list = [i for i in range(10) if i%2==0]    >>> output: [0, 2, 4, 6, 8]


### code below is for the use case where do not need to have a full list created in memory.
### Instead, they only need to iterate over the elements one at a time.
### using Generators without using yield keyword

g = (x**2 for x in range(10))
print g.next()  # output: 0
print g.next()  # output: 1
print g.next()  # output: 4


g1 = list(x**2 for x in range(10))
print g1  # output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# List Comprehension
y = list(x for x in "abc")
print y  # output: ['a', 'b', 'c']

# Early Binding vs Late Binding

# For instance, the following summation code will build a full list of squares in memory,
# iterate over those values, and, when the reference is no longer needed, delete the list:

print sum([x*x for x in range(10)])

