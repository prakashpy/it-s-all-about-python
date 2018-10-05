## Are you a Python Developer? Something you should always remember ##


        '==' is an equality test and is is an identity test.


#### List vs Tuple vs Dictionary ####
###### Find the index of an item given a list or dict ######
        mylist.index('my_item')

###### shuffle(list_name) can be used to randomizing the items of a list in python

[using generator expression](https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search )
[How to Remove index list from another list](https://stackoverflow.com/questions/40199689/how-to-remove-index-list-from-another-list-in-python?noredirect=1&lq=1)


#### Try Except Finally ####


#### Logging vs Logger


## Still wandering of "with" keyword?
###### In python the with keyword is used when working with unmanaged resources (like file streams). 
###### It allows you to ensure that a resource is "cleaned up" when the code that uses it finishes running, even if exceptions are thrown. 
###### It provides 'syntactic sugar' for try/finally blocks.
[With Keyword](https://www.python.org/dev/peps/pep-0343/)



#### Find difference between sort() and sorted()


### List comprehensions is a concise way to create lists.

###### syntax: *result*  = [*transform*    *iteration*         *filter*     ]
###### Example: 

        my_new_list = [i for i in range(10) if i%2==0]    >>> output: [0, 2, 4, 6, 8]

###### List comprehension is an elegant way to define and create list in Python.
###### List comprehension is a complete substitute for the lambda function as well as the functions map(), filter() and reduce().
###### List comprehensions are a tool for transforming one list (any iterable actually) into another list. 
###### During this transformation, elements can be conditionally included in the new list and each element can be transformed as needed.
        Output Expression      var       Input Sequence   Optional Predicate
        [ e ** 2            for e   in    a_list           if type(e) == types.IntType]

#### range vs xrange
###### range returns a list; xrange returns an object that acts like iterator for generating numbers on demand.

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

### Static Method / Class Method
###### @classmethod decorator, is a builtin function decorator that is an expression that gets evaluated after your function is defined.
###### @classmethod receives class as first argument. @classmethod is bound to the class not to the object of class.
###### @classmethod can modify a class state that would apply across all the instances of the class.

###### @classmethod -> use classmethod to create factory methods. Factory methods return class object for different use cases.

###### @staticmethod. -> we use staticmethod to create utility functions. // thanks to geeksforgeeks. :)



###  Early Binding vs Late Binding ###
###### Python takes a late binding approach to lambda expressions and has no precedent for automatic, early binding. FIXME


###  Pickling vs Unpickling ###
#### Pickling in python refers to the process of serializing objects into binary streams. Unpickling is the inverse of that. 
#### Pickling is useful when you want to save state of your objects and reuse them at another time without losing any instace specific data.
### pickle.dumps(obj) & pickle.loads(obj)

        import pickle
        data = {'a':1, 'b':2}
        with open('my_data.pickle', 'wb') as f:
            pickle.dump(data, f)
        with open('my_data.pickle', 'rb') as f:
            data_temp = pickle.load(f)

###  Monkey Patching
#### Dynamic replacement of attributes at runtime
#### common to use in unit testing to replace some variables to use some fixed data or replace some methods dynamically.


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



### Python 2.7
###### breakpoint() -- A Default Function
###### Order of Dictionaries is guaranteed in python 3.6+
###### async & await keywords added from 3.5+
###### context variables; values changes based on context

### metaclass
###### A metaclass is the class of a class. 
###### Like a class defines how an instance of the class behaves, a metaclass defines how a class behaves. A class is an instance of a metaclass.
