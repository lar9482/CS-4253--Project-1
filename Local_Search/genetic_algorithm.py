from chromosome import chromosome
from utils.ga_util import real_to_binary, binary_to_real

import random
import numpy as np

class genetic_algorithm:
    def __init__(self, fitness_function, population_size = 100, individual_size = 2, crossover_rate = 0.05, mutation_rate = 0.05,
                       min_value = 0, max_value = 10, maxProblem = True):

        self.fitness_function = fitness_function
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        
        self.population_size = population_size
        self.individual_size = individual_size
        self.min_value = min_value
        self.max_value = max_value

        self.maxProblem = maxProblem

        self.population = self.__initialize_population(population_size, individual_size, min_value, max_value)
        
    def __initialize_population(self, population_size, individual_size, min_value, max_value):
        population = np.empty((population_size, individual_size))
        for pop in range(0, population_size):
            for element in range(0, individual_size):
                population[pop, element] = random.uniform(min_value, max_value)

        return population

    def __calculate_adjusted_fitness(self, population, fitness_function, maxProblem):
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
            weights = self.__calculate_adjusted_fitness(self.population, self.fitness_function, self.maxProblem)
            new_population = np.empty((self.population_size, self.individual_size))

            for i in range(0, int(self.population_size/2)):
                #Performing the selection operation
                parent1 = self.__selection(self.population, weights)
                parent2 = self.__selection(self.population, weights)

                child1 = np.empty((self.population_size))
                child2 = np.empty((self.population_size))

                #Performing the crossover operation
                if (random.uniform(0, 1) < self.crossover_rate):
                    (child1, child2) = self.__crossover(parent1, parent2)
                else:
                    child1 = parent1
                    child2 = parent2

                #Performing the mutation operation
                if (random.uniform(0, 1) < self.mutation_rate):
                    child1 = self.__mutate(child1)
                
                if (random.uniform(0, 1) < self.mutation_rate):
                    child2 = self.__mutate(child2)
                
                #Appending the children to the new population
                new_population[i] = child1
                new_population[i + int(self.population_size/2)] = child2
            
            #Finishing the current generation.
            self.population = new_population
            current_generation += 1
            print("Generation: %s " % (current_generation))

    def __selection(self, population, weights):
        random_num = random.uniform(0, 1)
        choosen_weight = -1

        #Sorting all of the weights from least to greatest
        sorted_weights = weights[np.argsort(weights[:, 0])]

        #Get the 1st weight that's greater than the random_num.
        #This emulates a roulette with probability that's proportional to the weights
        for weight in sorted_weights:
            if (random_num < weight[0]):
                choosen_weight = weight[0]
                break
        
        #Get the row index that corresponds to the choosen weight
        choosen_index = np.argwhere(weights==choosen_weight)[0][0]

        return (population[choosen_index, :])
        
    #Todo:
    #Re-work implementation of crossover.
    #I think we're intended to split the bits of each number
    #not the numbers themselves 
    def __crossover(self, parent1, parent2):

        #Generate a random integer between 0 and the individual size
        split_point = int(random.uniform(0, self.individual_size))

        #For the 1st child, piece together the subsection of parent1 before the split_point
        # and the subsection of parent2 after the split_point
        child1_parent1 = parent1[0:split_point:1]
        child1_parent2 = parent2[split_point:self.individual_size:1]

        #For the 2nd child, piece together the subsection of parent1 after the split_point
        # and the subsection of parent2 before the split_point
        child2_parent1 = parent1[split_point:self.individual_size:1]
        child2_parent2 = parent2[0:split_point:1]

        #Join the subsections together to form the 1st and 2nd child
        child1 = np.concatenate((child1_parent1, child1_parent2), axis=0)
        child2 = np.concatenate((child2_parent1, child2_parent2), axis=0)

        return (child1, child2)

    def __mutate(self, individual):
        individual_index = int(random.uniform(0, self.individual_size))

        gene = individual[individual_index]
        gene_bitstring = real_to_binary(gene, self.min_value, self.max_value)

        bit_index = int(random.uniform(0, 52))
        if (gene_bitstring[bit_index] == '0'):
            gene_bitstring = gene_bitstring[:bit_index] + '1' + gene_bitstring[bit_index+1:]
        else:
            gene_bitstring = gene_bitstring[:bit_index] + '0' + gene_bitstring[bit_index+1:]
        
        new_gene = binary_to_real(gene_bitstring, self.min_value, self.max_value)
        individual[individual_index] = new_gene
        
        return individual

    def __report_progress(self, population):
        
        print()