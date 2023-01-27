import random
import numpy as np
from operator import itemgetter

class simulated_annealing:
    def __init__(self, schedule, value_function, min_value, max_value):
        self.schedule = schedule
        self.value_function = value_function
        self.min_value = min_value
        self.max_value = max_value

    def run_algorithm(self, T_0, schedule_weight):
        
        print()