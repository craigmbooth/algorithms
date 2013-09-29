import random

NSAMPLE = 3

def reservoir_sample(filename):
    """ Get a completely random sample of NSAMPLE lines from
    a stream of unknown length with only one loop through the
    file.  The algorithm is the following:
       1. The first NSAMPLE items make up the initial sample
       2. Then for items of index n, generate a random number
          [0,n] and if n < NSAMPLE replace that element of the
          sample.
    """

    sample = []
    with open(filename,'r') as f:
        for i,line in enumerate(f):
            if i < NSAMPLE:
                sample.append(line)
            else:
                k = random.randint(0,i)
                if k < NSAMPLE:
                    sample[k] = line
    return sample

print reservoir_sample("workfile")


