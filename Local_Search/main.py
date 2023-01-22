from utils.ga_util import bitstr2float
from binary_fractions import Binary
from utils.ga_util import real_to_binary, binary_to_real
import random

def main():
    one = -99.9535434465465455
    two = 5.0
    three = 100.555
    four = -100
    five = 0

    test1 = real_to_binary(one)
    test2 = real_to_binary(two)
    test3 = real_to_binary(three)
    test4 = real_to_binary(four)
    test5 = real_to_binary(five)
    
    # #float to binary
    # two = Binary(one)
    # three = two.to_twoscomplement()
    
    # test = two.split('.')
    # print(test[1])
    # print(bitstr2float(test[1]))
    print(test1)
    print(test2)
    print(test3)
    print(test4)
    print(test5)

    print(binary_to_real(test1))
    print(binary_to_real(test2))
    print(binary_to_real(test3))
    print(binary_to_real(test4))
    print(binary_to_real(test5))


    six = random.uniform(-100, 100)
    print(six)
    test6 = real_to_binary(six)
    print(test6)
    print(binary_to_real(test6))


if __name__ == "__main__":
    main()