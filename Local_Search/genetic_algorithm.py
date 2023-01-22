from chromosome import chromosome
from utils.ga_util import real_to_binary

class genetic_algorithm:
    def __init__(self, fitness_function, crossover_rate = 0.05, mutation_rate = 0.05):
        self.population = []
        self.fitness_function = fitness_function
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        
    def add_chromosome(self, num):
        self.population.append(chromosome(real_to_binary(num)))