"""
Strassen's sub-cubic matrix multiplication algorithm.  Scales as
O(n^2.808).  Beging by considering 2x2 matrix multiplication:

[a b].[e f] = [ae+bg  af+bh]
[c d] [g h]   [ce+dg  cf+dh]

Now it is the case that if you break a matrix into blocks and operate
on the blocks that each of the blocks behaves the same way as the full
matrix.  We can therefore treat this problem recursively by breaking
the matrix down in factors of two.  Now, doing this the naive way
results in O(n^3) behaviour as it requires 8 n/2 matrix
multiplications per step.  Strassen's insight was that this can be
performed with 7 multiplications (variables M1-M7 calculated below),
and that these 7 quantities can be combined in different ways to
reproduce the four quantities on the right-hand side of the equation
above.
"""


import numpy as np
from math import ceil,log

def strassen(A,B):
   """
   Pad arrays up to a power of two and call strassen_step to multiply
   the arrays.

   INPUT:  Two square 2d numpy arrays, A and B
   OUTPUT: A single array containing A.B
   """
   #Pad up to a power of two:
   n = A.shape[0]
   next_power_of_2 = int(pow(2, ceil(log(n, 2))))
   
   Apad = np.zeros((next_power_of_2,next_power_of_2))
   Bpad = np.zeros((next_power_of_2,next_power_of_2))
   
   Apad[0:n,0:n] = A
   Bpad[0:n,0:n] = B
   
   Cpad = strassen_step(Apad,Bpad)

   #Strip out the padding and return:
   return Cpad[0:n,0:n]

def strassen_step(A,B):
   """Strassen's sub-cubic algorithm for matrix multiplication.
   Perform one recursive step."""

   n = A.shape[0]
   if n == 1:
       return A*B
   else:
       #Extract sub-matrices:
       Anw = A[:n/2,:n/2]
       Ane = A[:n/2,n/2:]
       Asw = A[n/2:,:n/2]
       Ase = A[n/2:,n/2:]
       Bnw = B[:n/2,:n/2]
       Bne = B[:n/2,n/2:]
       Bsw = B[n/2:,:n/2]
       Bse = B[n/2:,n/2:]

       M1 = strassen(Anw+Ase,Bnw+Bse)
       M2 = strassen(Asw+Ase,Bnw)
       M3 = strassen(Anw,Bne-Bse)
       M4 = strassen(Ase,Bsw-Bnw)
       M5 = strassen(Anw+Ane,Bse)
       M6 = strassen(Asw-Anw,Bnw+Bne)
       M7 = strassen(Ane-Ase,Bsw+Bse)

       Cnw = M1 + M4 - M5 + M7
       Cne = M3 + M5
       Csw = M2 + M4
       Cse = M1 - M2 + M3 + M6

       #Copy partial results back into C:
       C = np.zeros((n,n))
       C[:n/2,:n/2] = Cnw
       C[:n/2,n/2:] = Cne
       C[n/2:,:n/2] = Csw
       C[n/2:,n/2:] = Cse

       return C.astype(int)

def test_strassen():
    n_tests = 10
    print "   --Testing strassen() with "+str(n_tests)+" tests"
    for i in range(n_tests):
       this_n = 1+np.random.randint(10) #size of matrix for this test
       max_val = np.random.randint(5000)
       A = np.random.randint(max_val,size=(this_n,this_n))
       B = np.random.randint(max_val,size=(this_n,this_n))
       np.testing.assert_array_equal(strassen(A,B), np.dot(A,B)) 
    print "   --test_strassen() tests passed"

if __name__ == "__main__":

    test_strassen()
