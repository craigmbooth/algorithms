
def mergesort(A):

    if len(A) == 1:
        return A
    else:
        left = mergesort(A[:len(A)/2])
        right = mergesort(A[len(A)/2:])
        return combine_arrays(left,right)


print mergesort([5,8,4,7,3,6,2,5,1])
