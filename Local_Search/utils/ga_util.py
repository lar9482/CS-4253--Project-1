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
    realBits = ''
    fractionBits = ''

    # If the inputted num is an integer, all of the bits are allocated to 'realBits'
    if (Binary(num).string.find('.') == -1):
        realBits = Binary(num).string
    #Else, the bits are allocated to 'realBits' and 'fractionBits' by spliited the string at the decimal point
    else:
        [realBits, fractionBits] = Binary(num).string.split('.')

    #Removing the negative sign, if it exists
    realBits = realBits.replace('-', '')
    
    #Adding placeholder zeros to the 7th place of 'realBits', if possible
    while (len(realBits) < realBitLength):
        realBits = '0' + realBits
    
    #Adding placeholder zeros to the 51th place of 'fractionBits', if possible
    while (len(fractionBits) < fractionBitLength):
        fractionBits = fractionBits + '0'

    #If num is posistive, add a zero in front to indicate the string as a positive number
    if (num > 0):
        realBits = '0' + realBits
    #Else, add a one in front to indicate the string as a negative number
    else:
        realBits = '1' + realBits
    
    return realBits + '.' + fractionBits