import struct
from binary_fractions import Binary

realBitLength = 7
fractionBitLength = 52

def bitstr2float(s):
    """Transforms a bit representation of a number between 0 and 1 to a
    floating point number. This is less error-prone (I believe) than
    something like float division.

    Additionally, if len(s) < 52, this method will choose the midpoint
    between two decimal values to guaratee that each value is equally
    displaced.

    :param str s: A string formatted as a bitstring
    """
    if len(s) < 52:
        s = s + ("1" + "0" * (51 - len(s)))
    elif len(s) > 52:
        raise ValueError("Bitstring cannot be longer than 52 bits (floating point number limit).")
    # https://stackoverflow.com/a/8751666
    b = '0b001111111111{}'.format(s)
    return struct.unpack('d', struct.pack('Q', int(b, 0)))[0] - 1


def real_to_binary(num, min_value, max_value):

    #Normalizing the input number
    normal_num = (num - min_value) / (max_value - min_value)

    #Getting the initial bitstring conversion of normal_num
    fractionBits = Binary(normal_num).string.split('.')[1]
    
    #Adding placeholder zeros to the 51th place of 'fractionBits', if possible
    while (len(fractionBits) < fractionBitLength):
        fractionBits = fractionBits + '0'

    #In cases where the fractional bits are greater than 52 bits
    if (len(fractionBits) > fractionBitLength):
        fractionBits = fractionBits[0:fractionBitLength:1]

    
    return fractionBits

def binary_to_real(bitstring, min_value, max_value):

    #Converting the inputted bitstring into a number between 0 and 1.
    normal_num = bitstr2float(bitstring)

    #Transforming normal_num back into a scaled number
    num = (normal_num*(max_value - min_value)) + min_value

    return num
        
    