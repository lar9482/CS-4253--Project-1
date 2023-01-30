from SA.simulated_annealing import simulated_annealing
import numpy as np
import random

class simulated_annealing_TSP(simulated_annealing):
    def __init__(self, graph, TSP_fitness, TSP_C, min_city = 0, max_city = 5, num_cities = 5, maxProblem = False):
        self.fitness_function = TSP_fitness
        self.graph = graph

        super().__init__(self.value_function, TSP_C, min_city, max_city, num_cities, maxProblem)

    def value_function(self, current_state):
        return self.fitness_function(current_state, self.graph)

    def get_first_state(self):
        #Get an array of ints between min_value and max_value
        first_state = np.array(range(self.min_value, self.max_value+1))
        return first_state

    def get_random_successor_state(self, current):
        #Copy the values of 'current' into the successor_state
        successor_state = np.empty(len(current), dtype=np.int32)
        for i in range(0, len(current)):
            successor_state[i] = int(current[i])

        #Get two random indexes for the sucessor state
        first_index = int(random.uniform(self.min_value, self.max_value))
        second_index = int(random.uniform(self.min_value, self.max_value))

        #Ensure that the indices are not equal to guarantee some change happens
        while (second_index == first_index):
            second_index = int(random.uniform(self.min_value, self.max_value))

        #Swap the values at the choosen indices in 'sucessor_state'
        successor_state[[second_index, first_index]] = successor_state[[first_index, second_index]]

        return successor_state

        