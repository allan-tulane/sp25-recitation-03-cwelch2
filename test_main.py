from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3 * 3

    #Additional Test Cases
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(8)) == 4 * 8
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(19)) == 5 * 19
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(1)) == 2 * 1
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(0)) == 3 * 0

