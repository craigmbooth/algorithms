def permute_string(A):
    """ Generate all permutations of string, A
    Algorithm is to remove each element in turn
    and recursively generate all the permutations
    of the remaining length n-1 array
    """
    if len(A) == 1:
        yield A

    for i in range(len(A)):
        this_element = A[i]
        other_elements = A[:i] + A[i+1:]
        for other_perm in permute_string(other_elements):
           yield this_element + other_perm

if __name__ == "__main__":
    thestr = "abcd"
    for p in permute_string(thestr):
        print p

    
