import random

def mergesort_recursive(A):
    """Basic implementation of mergesort algorithm.  Given
    a list A, return the list sorted into ascending order
    """

    #Two base cases, return the correct answer if length
    #is either 1 or two:
    if len(A) == 1:
        return A
    else:
        A1 = mergesort_recursive(A[:len(A)/2])
        A2 = mergesort_recursive(A[len(A)/2:])
        return merge_arrays(A1,A2)

def merge_arrays(A1,A2):
    """Given two sorted lists of length n1 and n2, merge them
    together in ascending order into a single list of length n1+n2
    """

    result = [0]*(len(A1)+len(A2))
    i1 = 0; i2 = 0
    counter = 0

    #Main merging loop.  Look at first element of both arrays
    #and copy the smallest into the results array.  Repeat.
    #Be careful with edge cases.
    while counter < len(A1) + len(A2):
        #Case where i1 and i2 are still in range:
        if i1 < len(A1) and i2 < len(A2):
            if A1[i1] <= A2[i2]:
                result[counter] = A1[i1]
                i1 += 1
            else:
                result[counter] = A2[i2]
                i2 += 1
        #i1 is out of range, just copy in i2:
        elif i1 >= len(A1) and i2 < len(A2):
            result[counter] = A2[i2]
            i2 += 1
        #i1 is out of range, just copy in i2:
        elif i1 < len(A1) and i2 >= len(A2):
            result[counter] = A1[i1]
            i1 += 1
        else:
            print i1,i2
            print result
            raise RuntimeError("This statement should never be reached."
                                "  Bug in the code")
        counter += 1

    return result

def test_mergesort():
    """Test the code by generating a series of arrays (with size randomly
    chosen in range [0,1000]), populating them with random integers (
    in range chosen randomly for each array to be between 0 and [1,1000]
    and comparing the result to Python's builtin sorted() method.
    """

    for i in range(100):
        #Max value in this test array:
        ubound = random.randint(1,1000)

        #Generate test array of random size:
        test_list = [random.randint(0,ubound) 
                     for r in xrange(random.randint(1,1000))]

        #Check that mergesort gives the same result:
        assert mergesort_recursive(test_list) == sorted(test_list)
    print "   --test_mergesort() passed tests"

if __name__ == "__main__":

    test_mergesort()


