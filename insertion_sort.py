def insertion_sort(A):

    #At each point the array up to element i-1 is alreadysorted.
    #We grab element i, and store it in currentVal.  This leaves
    #a 'hole' in the array, so slide the hole backwards until we
    #find a value smaller than currentVal.
    for i in range(1,len(A)):
        #At this point, the array up to i is sorted.
        currentVal = A[i]
        holePos = i
        #keep moving the hole down until the valueToInsert is larger than 
        #what's just below the hole or the hole has reached the
        #beginning of the array
        while holePos > 0 and currentVal < A[holePos - 1]:
            A[holePos] = A[holePos - 1] #shift the larger value up
            holePos -= 1 #move the hole position down

        #hole is in the right position, so put currentVal into the hole
        A[holePos] = currentVal

    return A

if __name__ == "__main__":
    assert insertion_sort([4,8,3,7,2,6,1,5,0]) == sorted([4,8,3,7,2,6,1,5,0])
