"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    xvec = x.binary_vec             # store binary vector representation of x in xvec
    yvec = y.binary_vec             # store binary vector representation of y in yvec

    xvec, yvec = pad(xvec, yvec)    # pad xvec and yvec if length is not the same

    # base case: if both x and y are <= 1, return their product as a BinaryNumber
    if x.decimal_val <= 1 and y.decimal_val <= 1:
        return BinaryNumber(x.decimal_val * y.decimal_val)

    x_left, x_right = split_number(xvec)    # split xvec and store left and right halves into x_left and x_right
    y_left, y_right = split_number(yvec)    # split yvec and store left and right halves into y_left and y_right

    n = len(xvec)       # get the total number of bits after padding

    # compute the three parts of the sum
    first = _quadratic_multiply(x_left, y_left)                                             # x_left * y_left
    second = _quadratic_multiply(BinaryNumber(x_left.decimal_val + x_right.decimal_val),
                                 BinaryNumber(y_left.decimal_val + y_right.decimal_val))    # (x_left + x_right) * (y_left + y_right)
    third = _quadratic_multiply(x_right, y_right)                                           # x_right * y_right

    # apply bit_shift for powers of 2 in the formula
    shifted_first = bit_shift(first, n)  # 2^n * first
    shifted_second = bit_shift(BinaryNumber(second.decimal_val - first.decimal_val - third.decimal_val), n // 2) # 2^(n/2) * (second - first - third)

    # return sum of the three parts as a BinaryNumber
    return BinaryNumber(shifted_first.decimal_val + shifted_second.decimal_val + third.decimal_val)


    
    
def time_quadratic_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x, y)
    return (time.time() - start)*1000

