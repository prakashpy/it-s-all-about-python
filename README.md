## Are you a Python Developer? Something you should always remember ##


        '==' is an equality test and is is an identity test.


#### List vs Tuple vs Dictionary ####
###### Find the index of an item given a list or dict ######
        mylist.index('my_item')

[using generator expression](https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search )
[How to Remove index list from another list](https://stackoverflow.com/questions/40199689/how-to-remove-index-list-from-another-list-in-python?noredirect=1&lq=1)


#### Try Except Finally ####


#### Logging vs Logger


## Still wandering of "with" keyword?
[With Keyword](https://www.python.org/dev/peps/pep-0343/)


#### Find difference between sort() and sorted()


### List comprehensions is a concise way to create lists.

###### syntax: *result*  = [*transform*    *iteration*         *filter*     ]
###### Example: 

        my_new_list = [i for i in range(10) if i%2==0]    >>> output: [0, 2, 4, 6, 8]


###### range vs xrange


### Iterators ###
[Iterators](https://www.python.org/dev/peps/pep-0234/)


### Generators0 ###
###### Using of generator expression, we can conserve Memory. lazy loading kinda - confirm
###### You should <3 Yield keyword
[pep-8 article on Yield](https://www.python.org/dev/peps/pep-0255/)


### PEP 3129 -- Class Decorators ###
[pep-8 article on Class Decorators](https://www.python.org/dev/peps/pep-3129/)

#### In Python, functions are first-class objects. Means, functions can be passed around and used as argument. 
#### Functions can return function. use  without parethesis when you want to return function.
#### Inner Function, define functions inside other functions.

## Decorators wrap a function, modifying its behavior. (Decorator modifies a function can change dynamically)

#### Syntactic Sugar. use decorator in simpler way with @ symbol.

###  Generator Decorator (PEP 342) ###
###### it is possible to write a decorator that makes it possible to use a generator that yields exactly once to control a with-statement.


###  Early Binding vs Late Binding ###
###### Python takes a late binding approach to lambda expressions and has no precedent for automatic, early binding. FIXME


###  Pickling vs Unpickling ###
#### Pickling in python refers to the process of serializing objects into binary streams. Unpickling is the inverse of that. 
#### Pickling is useful when you want to save state of your objects and reuse them at another time without losing any instace specific data.



## python-patterns
[Python Patterns](https://github.com/faif/python-patterns/blob/master/README.md)

###### Python is duck typed, meaning that you won't need to plan out class hierarchies in as much detail as in Java, and has first class functions.
###### The strategy pattern, for example, becomes much simpler and more obvious when you can just pass a function in, rather than having to make interfaces, etc. just to simulate higher order functions.
###### More generally, Python has syntactic sugar for a lot of common design patterns, such as the iterator and the aforementioned strategy.
###### It might be useful to understand these patterns (I've read Head First and found it pretty useful),
###### but think about Pythonic ways to implement them rather than just doing things the same way you would in Java.


## python design idioms

###### By assigning the class-type to a callable object you can essentially remove any 'factory' types in your code. You are only left with callables that produce objects that should conform to some given conventions.
###### Furthermore, there are design patterns in Python that just can't be represented in other statically-typed languages efficiently. Metaclasses and function decorators are good examples of this


## Garbage Collection in Python.

###### when you open file using "with" keyword, always close the file. This is not mendatory but you do not want to slow down your program hence it may use space in back.
###### Garbage collection is automatic in Python and you do not know when Python will close it! Hence, never forget to close your file!
