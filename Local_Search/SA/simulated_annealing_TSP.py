from simulated_annealing import simulated_annealing
import numpy as np
import random

class simulated_annealing_TSP(simulated_annealing):
    def __init__(self, graph, TSP_fitness, TSP_C, min_city = 0, max_city = 5, num_cities = 5, maxProblem = False):
        super().__init__(TSP_fitness, TSP_C, min_city, max_city, num_cities, maxProblem)
        self.graph = graph

    def get_first_state(self):

        first_state = np.array((self.dim))

        for i in range(0, first_state):
            while (random_city in first_state):
                random_city = int(random.uniform(self.min_value, self.max_value))
            first_state[i] = random_city
        
        return first_state

    def get_random_successor_state(self, current):
        first_index = int(random.uniform(self.min_value, self.max_value))
        second_index = int(random.uniform(self.min_value, self.max_value))

        return super().get_random_successor_state(current)

        