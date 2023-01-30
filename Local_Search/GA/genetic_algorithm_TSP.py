from GA.genetic_algorithm import genetic_algorithm
import numpy as np
import random 

class genetic_algorithm_TSP(genetic_algorithm):

    def __init__(self, graph, TSP_Fitness, TSP_C, population_size, individual_size, crossover_rate, mutation_rate,
                       min_value, max_value, maxProblem, elitism_applied):

        self.graph = graph
        self.TSP_Fitness = TSP_Fitness
        self.TSP_C = TSP_C
        super().__init__(self.fitness_function, population_size, individual_size, crossover_rate, mutation_rate,
                         min_value, max_value, maxProblem, elitism_applied)

    def fitness_function(self, individual):
        return self.TSP_Fitness(individual, self.graph)

    def initialize_population(self, population_size, individual_size, min_value, max_value):
        population = np.empty((population_size, individual_size), dtype=np.int32)
        for pop in range(0, population_size):
            individual = np.array(range(min_value, max_value+1))
            random.shuffle(individual)

            population[pop] = individual
        
        return population

    def crossover(self, parent1, parent2):
        return super().crossover(parent1, parent2)

    def mutate(self, individual):
        return super().mutate(individual)