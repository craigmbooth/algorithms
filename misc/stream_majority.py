def stream_majority(filename):
    """ Return the element that represents the majority
    of an unknown length stream, provided that there is
    a majority.  e.g. the majority of a,a,a,b,b,c,a is a
    """
    majority = None
    count = 0
    with open(filename,'r') as f:
        for line in f:
            if count == 0:
                majority = line.rstrip()
                count = 1
            elif line.rstrip() == majority:
                count += 1
            else:
                count -= 1

    return majority.rstrip() if count else None

print stream_majority("workfile")
