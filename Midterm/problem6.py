# Problem 1 and Problem 2 were objective type questions and therefore not listed here
###############################################################################
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    l = []
    for e in aList:
        if type(e) == list:
            l += flatten(e)
        else:
            l.append(e)
    return l

# Test
print(flatten( [ [1,'a',['cat'],2], [[[3]], 'dog'], 4, 5 ] ))

