from utils.ga_util import bitstr2float
from binary_fractions import Binary
from utils.ga_util import real_to_binary, binary_to_real

def main():
    one = -100.9535434465465455
    two = 5.0
    three = 100.555

    test1 = real_to_binary(one)
    test2 = real_to_binary(two)
    test3 = real_to_binary(three)
    
    # #float to binary
    # two = Binary(one)
    # three = two.to_twoscomplement()
    
    # test = two.split('.')
    # print(test[1])
    # print(bitstr2float(test[1]))
    print(test1)
    print(test2)
    print(test3)

    print(binary_to_real(test1))
    print(binary_to_real(test2))
    print(binary_to_real(test3))


if __name__ == "__main__":
    main()