"""

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

    return map (lambda x: x.replace(".", " "), input_list)


if __name__ == "__main__":
    temp_list = ["abc.pqr", "This.is.dummy","xyz.l.l.p"]
    print testfunc(temp_list)  # Output: ['abc pqr', 'This is dummy', 'xyz l l p']
