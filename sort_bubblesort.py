def bubbleSort(A):
    did_swap = True

    while did_swap:
        did_swap = False
        for i in range(len(A)-1):
            if (A[i] > A[i+1]):
                A[i], A[i+1] = A[i+1], A[i]
                did_swap = True

    return A


if __name__ == "__main__":

    A = [2,4,6,8,1,3,5,7]

    print bubbleSort(A)

