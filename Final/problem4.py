# Problem 1 and Problem 2 were objective type questions and therefore not listed
###############################################################################
# Problem 4
def primes_list(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    # Your code here
    L = [2]
    for n in range(3,N+1):
        for i in L:
            if n%i == 0:
                break
        if i == L[-1]:
            L.append(n)
    return L

# Test
print( primes_list(39))