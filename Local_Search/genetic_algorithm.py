from utils.ga_util import real_to_binary, binary_to_real

import random
import numpy as np
from operator import itemgetter

class genetic_algorithm:
    def __init__(self, fitness_function, population_size = 100, individual_size = 2, crossover_rate = 0.7, mutation_rate = 0.05,
                       min_value = 0, max_value = 10, maxProblem = True, elitism_applied = True):

        self.fitness_function = fitness_function
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        
        self.population_size = population_size
        self.individual_size = individual_size
        self.min_value = min_value
        self.max_value = max_value

        self.maxProblem = maxProblem
        self.elitism_applied = elitism_applied

        self.population = self.__initialize_population(population_size, individual_size, min_value, max_value)
        
    def __initialize_population(self, population_size, individual_size, min_value, max_value):
        population = np.empty((population_size, individual_size))
        for pop in range(0, population_size):
            for element in range(0, individual_size):
                population[pop, element] = random.uniform(min_value, max_value)

        return population

    def __calculate_adjusted_fitness(self, population, fitness_function, maxProblem):
        weights_to_population = []

        #For every individual, calculate the raw weights(fitness-values)
        #Assign raw weight and the individual to a tuple.
        for weight_index in range(0, self.population_size):
            raw_weight_value = fitness_function(population[weight_index, :])
            weights_to_population.append((raw_weight_value, population[weight_index, :]))

        #Get the total sum of all of the weights
        total_weight = sum(fitness for fitness,individual in weights_to_population)

        #Adjust the weights based on minimization or maximization
        for weight_index in range(0, self.population_size):
            #Maximization Problem
            if (maxProblem):
                adjusted_weight = (weights_to_population[weight_index][0]) / (total_weight)
                weights_to_population[weight_index] = (adjusted_weight, weights_to_population[weight_index][1])
            #Minimization
            else:
                adjusted_weight = (total_weight)/ (weights_to_population[weight_index][0])
                weights_to_population[weight_index] = (adjusted_weight, weights_to_population[weight_index][1])

        #Normalize the weights
        min_weight = min(weights_to_population)[0]
        max_weight = max(weights_to_population)[0]

        for weight_index in range(0, self.population_size):
            normalized_weight = (weights_to_population[weight_index][0] - min_weight) / (max_weight - min_weight)
            weights_to_population[weight_index] = (normalized_weight, weights_to_population[weight_index][1])
            

        #Finally, sort all of the tuples based on weight from least to greatest
        weights_to_population = sorted(weights_to_population, key=itemgetter(0))

        return weights_to_population

    def run_algorithm(self, generations = 1000):
        current_generation = 0
        while current_generation < generations:
            weights_to_population = self.__calculate_adjusted_fitness(self.population, self.fitness_function, self.maxProblem)
            new_population = np.empty((self.population_size, self.individual_size))

            for i in range(0, int(self.population_size/2)):

                child1 = np.empty((self.population_size))
                child2 = np.empty((self.population_size))

                #If the algorithm requests elitism, the two fittest
                #individuals from the last are copied over
                if (self.elitism_applied):
                
                    print()

                #Else, perform the selection, crossover, and mutation operators
                else:
                    #Performing the selection operation
                    parent1 = self.__selection(weights_to_population)
                    parent2 = self.__selection(weights_to_population)

                    #Performing the crossover operation
                    if (random.uniform(0, 1) < self.crossover_rate):
                        (child1, child2) = self.__crossover(parent1, parent2)
                    else:
                        child1 = parent1
                        child2 = parent2

                    #Performing the mutation operation
                    if (random.uniform(0, 1) < self.mutation_rate):
                        child1 = self.__mutate(child1, self.mutation_rate)
                
                    if (random.uniform(0, 1) < self.mutation_rate):
                        child2 = self.__mutate(child2, self.mutation_rate)
                
                #Appending the children to the new population
                new_population[i] = child1
                new_population[i + int(self.population_size/2)] = child2
            
            #Finishing the current generation.
            self.population = new_population
            current_generation += 1

            #Console reporting
            print("Generation: %s " % (current_generation))
            if (current_generation % 50 == 0):
                self.__report_progress(self.population)

    def __get_elite_individuals(self, population, weights):
        print()

    def __selection(self, weights_to_population):
        random_num = random.uniform(0, 1)

        #Get the 1st weight that's greater than the random_num.
        #This emulates a roulette with probability that's proportional to the weights
        for i in range(0, self.population_size):
            if (random_num < weights_to_population[i][0]):
                return weights_to_population[i][1]

        
    #Todo:
    #Re-work implementation of crossover.
    #I think we're intended to split the bits of each number
    #not the numbers themselves 
    def __crossover(self, parent1, parent2):

        child1 = np.empty(self.individual_size)
        child2 = np.empty(self.individual_size)

        for i in range(0, self.individual_size):
            splitpoint = int(random.uniform(0, 52))
            parent1_bitstring = real_to_binary(parent1[i], self.min_value, self.max_value)
            parent2_bitstring = real_to_binary(parent2[i], self.min_value, self.max_value)

            child1_bitstring = parent1_bitstring[0:splitpoint:1] + parent2_bitstring[splitpoint:52:1]
            child2_bitstring = parent2_bitstring[0:splitpoint:1] + parent1_bitstring[splitpoint:52:1]

            child1_num = binary_to_real(child1_bitstring, self.min_value, self.max_value)
            child2_num = binary_to_real(child2_bitstring, self.min_value, self.max_value)

            child1[i] = child1_num
            child2[i] = child2_num

        return (child1, child2)

    def __mutate(self, individual, mutation_rate):
        new_individual = np.empty((self.individual_size))
        for individual_index in range(0, self.individual_size):
            gene = individual[individual_index]
            gene_bitstring = real_to_binary(gene, self.min_value, self.max_value)

            for bit_index in range(0, len(gene_bitstring)):
                if (random.uniform(0, 1) < mutation_rate):   
                    if (gene_bitstring[bit_index] == '0'):
                        gene_bitstring = gene_bitstring[:bit_index] + '1' + gene_bitstring[bit_index+1:]
                    else:
                        gene_bitstring = gene_bitstring[:bit_index] + '0' + gene_bitstring[bit_index+1:]
        
            new_gene = binary_to_real(gene_bitstring, self.min_value, self.max_value)
            new_individual[individual_index] = new_gene
        
        return new_individual

    def __report_progress(self, population):
        raw_fitness = np.empty((self.population_size, 1))

        #For every individual, calculate the raw fitness
        for weight_index in range(0, self.population_size):
            raw_fitness[weight_index, 0] = self.fitness_function(population[weight_index, :])
        
        min_fitness = np.min(raw_fitness)
        max_fitness = np.max(raw_fitness)
        print("Max fitness: %s" % (max_fitness))
        print("Min fitness: %s" % (min_fitness))
        print()