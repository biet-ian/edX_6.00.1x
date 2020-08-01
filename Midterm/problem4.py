# Problem 1 and Problem 2 were objective type questions and therefore not listed here
###############################################################################
def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # solution 1
    # l = len(L)
    # for i in range(len(L)):
    #     L[i] = L[i][::-1]
    # for i in range(l//2):
    #     L[l - i - 1],L[i] = L[i],L[l - i - 1]

    # soultion 2
    l = len(L)
    if l == 1:
        L[0] = L[0][::-1]
    else:
        for i in range(l//2):
            L[l - i - 1],L[i] = L[i][::-1],L[l - i - 1][::-1]
        if l%2 == 1:
            # odd , reverse mid element
            L[l//2] = L[l//2][::-1]


# Test
L = [[0, 1, 2], [1, 2, 3], [3, 2, 1]]
deep_reverse(L) 
print(L)