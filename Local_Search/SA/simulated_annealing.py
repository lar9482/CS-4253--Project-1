import random
import math
import numpy as np
from operator import itemgetter

class simulated_annealing:
    def __init__(self, value_function, constraint_function, min_value = 0, max_value = 10, dim = 2, maxProblem = True):
        self.value_function = value_function
        self.constraints = constraint_function
        self.min_value = min_value
        self.max_value = max_value
        self.dim = dim
        self.maxProblem = maxProblem

    def run_algorithm(self, schedule, T_0 = 1000, T_Final = 0.1, alpha = 0.8):
        current_time = 1
        current_state = self.get_first_state()
        while True:
            current_temperature = schedule(current_time, T_0, alpha)
            if (current_temperature <= T_Final):
                print('done')
                return current_state

            next_state = self.get_random_successor_state(current_state)
            delta_E = self.value_function(current_state) - self.value_function(next_state)
                
            if (delta_E > 0):
                current_state = next_state
            else:
                random_num = random.uniform(0, 1)
                probability = math.exp((delta_E/current_temperature))
                # print(probability)
                if random_num < probability:
                    current_state = next_state

            current_time += 1
            print(current_temperature)


    def get_first_state(self):
        first_state = np.empty((self.dim))
        for i in range(0, self.dim):
            random_num = random.uniform(self.min_value, self.max_value)
            first_state[i] = random_num

        return first_state

    def get_random_successor_state(self, current):
        successor = np.empty((self.dim))
        
        for i in range(0, self.dim):
            successor[i] = random.gauss(0, 1) + current[i]
            while (not self.constraints(np.array([successor[i]]))):
                successor[i] = random.gauss(0, 1) + current[i]

        return successor