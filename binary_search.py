def binary_search(key,A,imin=0,imax=None):
    """Given a sorted array, A, perform a binary search
    to determine if it contains key"""

    #First iteration through set imax = end of array
    if imax is None:
        imax = len(A)-1

    if abs(imax - imin) <= 1:
        if A[imax] == key:
            return imax
        elif A[imin] == key:
            return imin
        else:
            return None

    middle = int((imax+imin)/2)

    if A[middle] == key:
        #Found it!
        return middle
    elif A[middle] < key:
        #Key is in the right half
        return binary_search(key,A,imin=middle+1,imax=imax)
    else:
        #Key is in the left half
        return binary_search(key,A,imin=imin,imax=middle-1)
    
if __name__ == "__main__":
    """If deirectly imported do 1000 random tests of the code"""

    import random
    numtests = [0,0]

    for i in range(1000):
        A = [random.randint(0,50) for _ in range(random.randint(1,100))]
        A.sort()
        key = random.randint(0,30)

        result = binary_search(key,A)
        if result is not None:
            numtests[0] += 1
            assert A[result] == key
        else:
            numtests[1] += 1
            assert key not in A

    print "   ---binary_search passed 1000 tests"
    print "      --- ",numtests[0]," in which the key was found"
    print "      --- ",numtests[1]," in which the key was not found"
