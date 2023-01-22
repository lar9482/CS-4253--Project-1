from chromosome import chromosome
from utils.ga_util import real_to_binary, binary_to_real

import random
import numpy as np

class genetic_algorithm:
    def __init__(self, fitness_function, population_size = 100, crossover_rate = 0.05, mutation_rate = 0.05,
                       min_value = 0, max_value = 10):

        self.fitness_function = fitness_function
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.population = self.initialize_population(population_size, min_value, max_value)
        
    def initialize_population(self, population_size, min_value, max_value):
        population = np.empty(population_size)
        for i in range(0, population_size):
            initial_value = random.uniform(min_value, max_value)
            population[i] = initial_value

        return population