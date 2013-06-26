"""
Simple recursive algorithm for multiplying two numbers, x and y.
Split x and y into halves (a,b) and (b,c).

Rewrite x and y as:
x = 10^(n/2)*a + b
y = 10^(n/2)*c + d

Then:
x*y = 10^n * ac + 10^(n/2) * (ad+bc) + bd  --(Eq. 1)

Note that this algorithm scales O(n^2). A simple improvement is
provided by Karatsuba's fast multiply algorithm, which relies on:

(b+a)(c+d) - ac - bd = bc + ad

Substituting this into equation 1 allows us to calculate the
multiplication using only three sub-problems in place of four:
a*c, b*d and (a+b)*(c+d)
"""
from math import ceil

#Lookup table for multiplying two single-digit numbers
single_multiply = [[0,0,0,0,0,0,0,0,0,0],[0,1,2,3,4,5,6,7,8,9],[0,2,4,6,8,10,12,14,16,18],[0,3,6,9,12,15,18,21,24,27],[0,4,8,12,16,20,24,28,32,36],[0,5,10,15,20,25,30,35,40,45],[0,6,12,18,24,30,36,42,48,54],[0,7,14,21,28,35,42,49,56,63],[0,8,16,24,32,40,48,56,64,72],[0,9,18,27,36,45,54,63,72,81]]

def list_to_int(a):
    """Convert an a list where each element is one digit to a single integer"""
    return int(''.join(map(str,a)))

def int_to_list(a):
    """Convert an integer to a list where each element is one digit"""
    return map(int,list(str(a)))

def multiply_karatsuba(x,y):
    """Wrapper routine multiplies two integers with Karatsuba's fast multiplication
    algorithm"""

    #Convert the integers into strings, and make a list
    #from each element of the string:
    str_x = int_to_list(x)
    str_y = int_to_list(y)

    return multiply_karatsuba_list(str_x,str_y)

def multiply_karatsuba_list(x,y):

    n = max(len(x),len(y))
    deg = ceil(float(n)/2)

    if len(x) < n:
        pad = [0]*(n-len(x))
        x = pad + x
    if len(y) < n:
        pad = [0]*(n-len(y))
        y = pad + y

    if len(x) == 1 and len(y) == 1:
        #Base case for recursion.  Return from lookup table.
        return single_multiply[x[0]][y[0]]
    else:
        a,b = x[:n/2], x[n/2:]
        c,d = y[:n/2], y[n/2:]

        ac = multiply_karatsuba_list(a,c)
        bd = multiply_karatsuba_list(b,d)

        #We now need to multiply (a+b)(c+d) so convert back from
        #a list to a number to add them, then back to a list.
        a_plus_b = int_to_list(list_to_int(a) + list_to_int(b))
        c_plus_d = int_to_list(list_to_int(c) + list_to_int(d))

        f  = multiply_karatsuba_list(a_plus_b,c_plus_d)

        #Note that although I do use some multiplications here
        #that multiplying by a power of 10 is the same as adding
        #zeroes to the end of a number.
        return int(10**(2*deg)*ac + 10**deg*(f-ac-bd) + bd)

def test_karatsuba():
    assert multiply_karatsuba(1234,4321) == 5332114
    assert multiply_karatsuba(111,111) == 12321
    assert multiply_karatsuba(1,0) == 0
    assert multiply_karatsuba(500,1) == 500
    assert multiply_karatsuba(2844592,101990) == 2844592*101990

    #Exhaustively verify that single-digit multiplications are correct:
    for i in range(10):
        for j in range(10):
            assert multiply_karatsuba(i,j) == i*j

    print '   --multiply_karatsuba passed tests'

if __name__ == "__main__":

    #If the module is called directly do some testing:
    test_karatsuba()
