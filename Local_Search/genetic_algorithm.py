from chromosome import chromosome
from utils.ga_util import real_to_binary, binary_to_real

import random
import numpy as np

class genetic_algorithm:
    def __init__(self, fitness_function, population_size = 100, individual_size = 10, crossover_rate = 0.05, mutation_rate = 0.05,
                       min_value = 0, max_value = 10, maxProblem = True):

        self.fitness_function = fitness_function
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        
        self.population_size = population_size
        self.individual_size = individual_size
        self.min_value = min_value
        self.max_value = max_value

        self.maxProblem = maxProblem

        self.population = self.initialize_population(population_size, individual_size, min_value, max_value)
        
    def initialize_population(self, population_size, individual_size, min_value, max_value):
        population = np.empty((population_size, individual_size))
        for pop in range(0, population_size):
            for element in range(0, individual_size):
                population[pop, element] = random.uniform(min_value, max_value)

        return population

    def calculate_adjusted_fitness(self, population, fitness_function, maxProblem):
        weights = np.empty((self.population_size, 1))

        #For every individual, calculate the raw fitness
        for weight_index in range(0, self.population_size):
            weights[weight_index, 0] = fitness_function(population[weight_index, :])

        #Get the total sum all fitnesses
        total_fitness = np.sum(weights)

        #Adjust the weights based on minimization or maximization
        for weight_index in range(0, self.population_size):
            #Maximazation Problem
            if (maxProblem):
                weights[weight_index, 0] = (weights[weight_index, 0]) / (total_fitness)
            #Minimazation
            else:
                weights[weight_index, 0] = (total_fitness)/ (weights[weight_index, 0])

        #Normalize the weights
        min_weight = np.min(weights)
        max_weight = np.max(weights)

        for weight_index in range(0, self.population_size):
            weights[weight_index, 0] = (weights[weight_index, 0] - min_weight) / (max_weight - min_weight)
    
        return weights

    def run_algorithm(self, generations = 1000):
        current_generation = 0
        while current_generation < generations:
            weights = self.calculate_adjusted_fitness(self.population, self.fitness_function, self.maxProblem)
            new_population = np.empty(self.population.size)

            for i in range(0, self.population_size):
                parent1 = self.selection(self.population, weights)
                parent2 = self.selection(self.population, weights)
                child = np.empty((self.population_size))

                if (random.uniform(0, 1) < self.crossover_rate):
                    child = self.crossover(parent1, parent2)

                print()
            current_generation += 1

    def selection(self, population, weights):
        random_num = random.uniform(0, 1)
        choosen_weight = -1

        #Sorting all of the weights from least to greatest
        sorted_weights = weights[np.argsort(weights[:, 0])]
        for weight in sorted_weights:
            if (random_num < weight[0]):
                choosen_weight = weight[0]
                break
        
        choosen_index = np.argwhere(weights==choosen_weight)[0][0]

        return (population[choosen_index, :])
        

    def crossover(self, parent1, parent2):
        c = int(random.uniform(0, self.individual_size))

        subParent1 = parent1[0:c:1]
        subParent2 = parent2[c:self.individual_size:1]
        
        return np.concatenate((subParent1, subParent2), axis=0)

    def mutate(self, chromosome):
        print()