from utils.ga_util import real_to_binary, binary_to_real

class chromosome:
    def __init__(self, bit_value):
        self.bit_value = bit_value
        self.real_value = binary_to_real(bit_value)

    def get_binary(self):
        return self.bit_value
    
    def get_real(self):
        return self.real_value