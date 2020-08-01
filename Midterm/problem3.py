# Problem 1 and Problem 2 were objective type questions and therefore not listed here
###############################################################################
# Write a recursive Python function, given a non-negative integer N, to count 
# and return the number of occurrences of the digit 7 in N
def count7(N):
    '''
    N: a non-negative integer
    '''
    if N // 10 == 0:
        return int(N==7)
    else:
        return count7(N//10) + (N%10 == 7)

# Test
print(count7(1237123))