import struct
from binary_fractions import Binary

realBitLength = 7
fractionBitLength = 51

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


def real_to_binary(num):
    #Splitting the number into binary with its real part and fractional part separated
    [realBits, fractionBits] = Binary(num).string.split('.')

    #Removing the negative sign, if it exists
    realBits = realBits.replace('-', '')
    
    while (len(realBits) < realBitLength):
        realBits = '0' + realBits
    
    while (len(fractionBits) < fractionBitLength):
        fractionBits = fractionBits + '0'

    if (num > 0):
        realBits = '0' + realBits
    else:
        realBits = '1' + realBits
    
    return realBits + '.' + fractionBits