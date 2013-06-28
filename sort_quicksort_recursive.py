import sys

def choosePivot(A):
    return A[0]

def partitionArray(A,p):
    
    

def quickSort(A):

    if len(A) == 1:
        return A
    else:
        p = choosePivot(A)
        Left,Pivot,Right = partitionArray(A,p)

        Left = quickSort(Left)
        Right = quickSort(Right)

        return Left+Pivot+Right

if __name__ == "__main__":

    A = [5,4,3,2,1]

    print quickSort(A)
