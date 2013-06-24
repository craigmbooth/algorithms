"""
Simple recursive algorithm for multiplying two numbers, x and y.
Split x and y into halves (a,b) and (b,c).

Rewrite x and y as:
x = 10^(n/2)*a + b
y = 10^(n/2)*c + d

Then:
x*y = 10^n * ac + 10^(n/2) * (ad+bc) + bd

Note that this algorithm scales O(n^2). A simple improvement is
provided by Karatsuba's fast multiply algorithm in
multiply_karatsuba.py
"""

from math import ceil

#Lookup table for multiplying two single-digit numbers
single_multiply = [[0,0,0,0,0,0,0,0,0,0],[0,1,2,3,4,5,6,7,8,9],[0,2,4,6,8,10,12,14,16,18],[0,3,6,9,12,15,18,21,24,27],[0,4,8,12,16,20,24,28,32,36],[0,5,10,15,20,25,30,35,40,45],[0,6,12,18,24,30,36,42,48,54],[0,7,14,21,28,35,42,49,56,63],[0,8,16,24,32,40,48,56,64,72],[0,9,18,27,36,45,54,63,72,81]]

def multiply_recursive(x,y):

    str_x = str(x)
    str_y = str(y)
    n = max(len(str_x),len(str_y))

    str_x = str_x.zfill(n)
    str_y = str_y.zfill(n)

    if len(str_x) == 1 and len(str_y) == 1:
        #Base case for recursion.  Return from lookup table.
        return single_multiply[x][y]
    else:
        a_out,b_out = str_x[:n/2], str_x[n/2:]
        c_out,d_out = str_y[:n/2], str_y[n/2:]

        ac = multiply_recursive(int(a_out),int(c_out))
        ad = multiply_recursive(int(a_out),int(d_out))
        bc = multiply_recursive(int(b_out),int(c_out))
        bd = multiply_recursive(int(b_out),int(d_out))

        deg = ceil(float(n)/2)

        #Note that although I do use some multiplications here
        #that multiplying by a power of 10 is the same as adding
        #zeroes to the end of a number.
        return pow(10,2*deg)*ac + pow(10,deg)*(ad+bc) + bd

if __name__ == "__main__":

    #If the module is called directly do some testing:
    assert multiply_recursive(1234,4321) == 5332114
    assert multiply_recursive(111,111) == 12321
    assert multiply_recursive(1,0) == 0
    assert multiply_recursive(500,1) == 500
    assert multiply_recursive(2844592,101990) == 2844592*101990

    #Exhaustively verify that single-digit multiplications are correct:
    for i in range(10):
        for j in range(10):
            assert multiply_recursive(i,j) == i*j

    print '   --multiply_recursive_naive passed tests'
