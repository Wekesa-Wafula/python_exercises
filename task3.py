def first_last(a):
    """Return a list with the first and last element """
    
    del a[1:-1]
    return a


numbers = [3,5,77,59,2,5,88,97,300,456,222,24]
print('\n')
print(first_last(numbers))
print('\n')