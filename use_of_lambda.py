"""
Lambda in Python with Map function.

Limitation of Lambda.
You can only use one expressions.
 
"""

def testfunc(input_list):
    """
    functions accepts a list and returns new list replacing all the periods with white spaces

    Args:
        input_list: input list that you want to modify.
        param2: The second parameter.

    Returns:
        List: returns updated list without periods replaced by white space.
    """

    #Note: instead of using for loop for this, we can ideally do this pythonic way.
    
    # map(func, seq) => returns new list with the elements changed by func.
    # map can be applied to more than one func. example: map(func, seq1, seq2, seq3)

    return map (lambda x: x.replace(".", " "), input_list)


if __name__ == "__main__":
    temp_list = ["abc.pqr", "This.is.dummy","xyz.l.l.p"]
    print testfunc(temp_list)  # Output: ['abc pqr', 'This is dummy', 'xyz l l p']



    # similarly 
    # we can use filter
    # filter(func, seq) => returns filtered output based on functions returns
    # use case: in a given list return list of only elements divisible by 3

    # we can use reduce
    # reduce(func, seq) => returns a single value. sum of all elements does sum of first two, givne to third element and so on.
