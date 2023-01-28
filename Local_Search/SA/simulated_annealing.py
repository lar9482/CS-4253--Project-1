import random
import numpy as np
from operator import itemgetter

class simulated_annealing:
    def __init__(self, value_function, min_value = 0, max_value = 10, dim = 2):
        self.value_function = value_function
        self.min_value = min_value
        self.max_value = max_value
        self.dim = dim

    def run_algorithm(self, schedule, T_0, alpha):
        
        print()