# Problem 1 and Problem 2 were objective type questions and therefore not listed
###############################################################################
# Problem 5
def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    # Your code here
    D = {}
    N = len(map_from)
    assert( N == len(map_to))

    for i in range(N):
        D[map_from[i]] = map_to[i]

    decoded = ''
    for c in code:
        decoded += D[c]
    return (D,decoded)

# Test
print(cipher("abcd", "dcba", "dab"))
