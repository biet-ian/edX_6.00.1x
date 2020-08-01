# Problem 1 and Problem 2 were objective type questions and therefore not listed
###############################################################################
# Problem 3
def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    if n < 0:
        return False
    a_lim = n // 6
    b_lim = n // 9
    c_lim = n // 20
    for a in range(a_lim+1):
        if n == 6*a:
            return True
        else:
            for b in range(b_lim+1):
                if n == 6*a+9*b:
                    return True
                else:
                    for c in range(c_lim+1):
                        if n == 6*a + 9*b + 20*c:
                            return True
    return False

#Test
print(McNuggets(29))
