# Problem 1 and Problem 2 were objective type questions and therefore not listed here
###############################################################################
# Write a Python function that returns a list of keys in aDict with the value 
# target. The list of keys you return should be sorted in increasing order. 
# The keys and values in aDict are both integers. 

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    d = []
    for k in sorted(aDict.keys()):
        if aDict[k] == target:
            d.append(k)
    return d

# Test
print(keysWithValue({3:3,2:22,1:1},2))
