import sys

def choosePivot(A):
    return 2

def partitionArray(A,p):
    print "Pivoting on : ",p

    i = 0
    i_pivot = 0

    j = 0
    while j < len(A):
        print "-----------------"
        print "Before : ",A
        print "Considering element ",j," = ",A[j]
        print i,j,A[j]
        if A[j] < p:
            print "lt"
            if j != 0:
               temp = A[i]
               A[i] = A[j]
               A[j] = temp
            i += 1

        elif A[j] > p:
            pass
            #Easy case, this
        else:
            print "pivot"
            #Move the pivot to the start of the array.
            #Shift the first element of the lt section to the end
            #of the lt section
            temp = A[i_pivot]
            A[i_pivot] = A[j]
            A[j] = temp
            i_pivot += 1
            j -= 1
        j += 1
        print "After : ",A
    print "Final result = ",A
    print "i_pivot = ",i_pivot
    print i
    Pivot = A[0:i_pivot]
    Left  = A[i_pivot:i]
    Right = A[i:]

    return Left, Pivot, Right

def quickSort(A):

    if len(A) == 1:
        return A
    else:
        p = choosePivot(A)
        Left,Pivot,Right = partitionArray(A,p)
        print Left,Pivot,Right
        #Left = quickSort(Left)
        #Right = quickSort(Right)
        return 1
        #return Left+Pivot+Right

if __name__ == "__main__":

    A = [2,4,6,8,1,3,5,7]

    print quickSort(A)
