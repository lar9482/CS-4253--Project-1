import random
import math
import numpy as np
from operator import itemgetter
from utils.ga_eval import _plot_f
import matplotlib.pyplot as plt

class simulated_annealing:
    def __init__(self, value_function, constraint_function, min_value = 0, max_value = 10, dim = 2, maxProblem = True):
        self.value_function = value_function
        self.constraints = constraint_function
        self.min_value = min_value
        self.max_value = max_value
        self.dim = dim
        self.maxProblem = maxProblem

        self.times = []
        self.values = []
        self.temperatures = []

    def run_algorithm(self, schedule, T_0 = 1000, T_Final = 0, k = 20):
        current_time = 1
        current_state = self.get_first_state()
        while True:
            current_temperature = schedule(current_time, T_0, T_Final, k)
            if (current_temperature <= T_Final):
                self.graph_data()
                self.graph_schedule()

                print('done')
                return current_state

            next_state = self.get_random_successor_state(current_state)
            delta_E = self.value_function(current_state) - self.value_function(next_state)
                
            if (delta_E > 0):
                current_state = next_state
            else:
                random_num = random.uniform(0, 1)
                probability = math.exp((delta_E/current_temperature))
                print(probability)
                if random_num < probability:
                    current_state = next_state

            self.add_time(current_time)
            self.add_value(self.value_function(current_state))
            self.add_temperature(current_temperature)

            current_time += 1
            


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
    
    def add_time(self, time):
        self.times.append(time)

    def add_value(self, value):
        self.values.append(value)

    def add_temperature(self, temperature):
        self.temperatures.append(temperature)

    def graph_data(self):
        plt.plot(self.times, self.values)
        plt.xlabel('time')
        plt.ylabel('value')
        plt.show()

    def graph_schedule(self):
        plt.plot(self.times, self.temperatures)
        plt.xlabel('time')
        plt.ylabel('temperature')
        plt.show()
