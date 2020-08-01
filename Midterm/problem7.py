# Problem 1 and Problem 2 were objective type questions and therefore not listed here
###############################################################################
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    L_c = L[:]
    for e in L_c:
        if not f(e):
            L.remove(e) 
    return len(L)

def f(s):
    return 'a' in s

# Test      
L = ['a', 'b', 'b', 'a']
print(satisfiesF(L))
print(L)
