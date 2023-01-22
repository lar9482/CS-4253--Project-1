from utils.ga_util import bitstr2float
from binary_fractions import Binary

def main():
    one = -100.9535434465465455
    
    #float to binary
    two = Binary(one)
    three = two.to_twoscomplement()
    
    test = two.split('.')
    print(test[1])
    print(bitstr2float(test[1]))



if __name__ == "__main__":
    main()