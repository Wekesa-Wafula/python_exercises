def maximum(a,b,c):
    """This function returns the largest of the three variables passed to it"""
    if (a > b) and (a > c):
        return a
    elif (b > a) and (b > c):
        return b
    elif (c > a) and (c > b):
        return c

max_value = maximum(7200,450000000,300000)
print('The maximum value of the three is: ' + str(max_value) )
     
