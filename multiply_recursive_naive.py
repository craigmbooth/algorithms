from math import ceil
#
#Simple recursive algorithm for multiplying two numbers, x and y.
#Split x and y into halves (a,b) and (b,c).
#
# Rewrite x and y as:
# x = 10^(n/2)*a + b
# y = 10^(n/2)*c + d
#
# Then:
# x*y = 10^n * ac + 10^(n/2) * (ad+bc) + bd

def multiply_recursive(x,y):

    str_x = str(x)
    str_y = str(y)
    n = max(len(str_x),len(str_y))

    str_x = str_x.zfill(n)
    str_y = str_y.zfill(n)

    if len(str_x) == 1 and len(str_y) == 1:
        return x*y
    else:
        a_out,b_out = str_x[:n/2], str_x[n/2:]
        c_out,d_out = str_y[:n/2], str_y[n/2:]

        ac = multiply_recursive(int(a_out),int(c_out))
        ad = multiply_recursive(int(a_out),int(d_out))
        bc = multiply_recursive(int(b_out),int(c_out))
        bd = multiply_recursive(int(b_out),int(d_out))

        deg = ceil(float(n)/2)

        return pow(10,2*deg)*ac + pow(10,deg)*(ad+bc) + bd

if __name__ == "__main__":

    #If the module is called directly do some testing:
    assert multiply_recursive(1234,4321) == 5332114
    assert multiply_recursive(111,111) == 12321
    assert multiply_recursive(1,0) == 0
    assert multiply_recursive(500,1) == 500
    assert multiply_recursive(2844592,101990) == 2844592*101990
    print '   --multiply_recursive_naive passed tests'
