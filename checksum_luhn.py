"""Provides method generate(prefix,length), which for a given prefix and
total length will return a valid credit card number.  generate returns
None for invalid inputs.

Credit card numbers have the following form: PPPPPP NNNNNNNNN C

Where P is a prefix that identifies the issuing authority, N is an
account number and C is a checksum digit, calculated with Luhn's
algorithm.

"For a card with an even number of digits, double every odd numbered
digit and subtract 9 if the product is greater than 9. Add up all
the even digits as well as the doubled-odd digits, and the result
must be a multiple of 10 or it's not a valid card. If the card has
an odd number of digits, perform the same addition doubling the even
numbered digits instead."
"""

import random

#Double and subtract 9 if > 9:
lookup_tab = [0,2,4,6,8,1,3,5,7,9]

def is_luhn_valid(n):
    """is_luhn_valid takes a credit card number as input and verifies 
    whether it is valid or not. If it is valid, it returns True, 
    otherwise it returns False."""
    return (luhn_checksum(str(n)) == 0)

def luhn_checksum(n):
    """Calculate the Luhn checksum for number 'n'"""
    thesum = 0
    n = str(n)
    for i,num in enumerate(n):
        if (len(n)%2==0 and i%2==0) or (len(n)%2!=0 and i%2!=0):
            thesum += lookup_tab[int(num)]
        else:
            thesum += int(num)            
    return thesum%10

def generate(pref,l):
    """ Generate a credit card number with prefix 'pref' and total length
    'l' (including the checksum digit)"""
        
    if not pref.isdigit(): return None
    if len(pref) >= l: return None

    cc = "".join(pref)
    for i in range(l - len(cc) - 1):
        cc += str(random.randrange(10))
    cc += "0"
    
    checksum = luhn_checksum(cc)    
    if checksum != 0:
        cc = cc[:-1] + str(10-int(checksum))
    return cc

def test_generate():
    
    assert generate("123N56",16) == None
    assert generate("1234",3) == None
    for i in range(10,20):
       n = generate("123456",i)
       assert is_luhn_valid(n)
    print "passed tests in test_generate()"

if __name__ == "__main__":
    test_generate()
