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

        self.population = self.initialize_population(population_size, individual_size, min_value, max_value)
        
    def initialize_population (self, population_size, individual_size, min_value, max_value):
        population = np.empty((population_size, individual_size))
        for pop in range(0, population_size):
            for element in range(0, individual_size):
                population[pop, element] = random.uniform(min_value, max_value)

        return population

    def calculate_adjusted_fitness(self, population, fitness_function, maxProblem):
        weights_to_population = []

        #For every individual, calculate the raw weights(fitness-values)
        #Assign raw weight and the individual to a single tuple.
        for weight_index in range(0, self.population_size):
            raw_weight_value = fitness_function(population[weight_index, :])
            weights_to_population.append((raw_weight_value, population[weight_index, :]))

        #Then, sort the raw weights from least to greatest
        weights_to_population = sorted(weights_to_population, key=itemgetter(0))
        total_rank = ((self.population_size)*(self.population_size+1)) / 2 

        #Adjust the raw weights based on rank selection for a minimization or maximization problem.
        for weight_index in range(0, self.population_size):
            #Maximization problem
            if maxProblem:
                adjusted_weight = (weight_index+1) / (total_rank)
                weights_to_population[weight_index] = (adjusted_weight, weights_to_population[weight_index][1])

            #Minimization problem
            else:
                adjusted_weight = (total_rank) / (weight_index+1)
                weights_to_population[weight_index] = (adjusted_weight, weights_to_population[weight_index][1])
        
        return weights_to_population

    def run_algorithm(self, generations = 1000):
        current_generation = 0
        while current_generation < generations:
            weights_to_population = self.calculate_adjusted_fitness(self.population, self.fitness_function, self.maxProblem)
            new_population = np.empty((self.population_size, self.individual_size))

            for i in range(0, int(self.population_size/2)):

                child1 = np.empty((self.population_size))
                child2 = np.empty((self.population_size))

                #If the algorithm requests elitism, the two fittest
                #individuals from the last generation are copied over
                if (i == 0 and self.elitism_applied):
                    (child1, child2) = self.get_elite_individuals(weights_to_population)

                #Else, perform the selection, crossover, and mutation operators
                else:
                    #Performing the selection operation
                    parent1 = self.selection(weights_to_population)
                    parent2 = self.selection(weights_to_population)

                    #Performing the crossover operation
                    if (random.uniform(0, 1) < self.crossover_rate):
                        (child1, child2) = self.crossover(parent1, parent2)
                    else:
                        child1 = parent1
                        child2 = parent2

                    #Performing the mutation operation
                    if (random.uniform(0, 1) < self.mutation_rate):
                        child1 = self.mutate(child1)
                
                    if (random.uniform(0, 1) < self.mutation_rate):
                        child2 = self.mutate(child2)
                
                #Appending the children to the new population
                new_population[i] = child1
                new_population[i + int(self.population_size/2)] = child2
            
            #Finishing the current generation.
            self.population = new_population
            current_generation += 1

            #Console reporting
            print("Generation: %s " % (current_generation))
            if (current_generation % 10 == 0):
                self.report_progress(self.population)

    #This function may be broken
    def get_elite_individuals(self, weights_to_population):
        return(weights_to_population[self.population_size-1][1], weights_to_population[self.population_size-2][1])

    def selection(self, weights_to_population):

        #Getting the minimum weight and maximum weight from the calculated weights
        min_weight = min(weights_to_population, key = itemgetter(0))[0]
        max_weight = max(weights_to_population, key = itemgetter(0))[0]


        random_num = random.uniform(min_weight, max_weight)

        #Get the 1st weight that's greater than the random_num.
        #This emulates a roulette with probability that's proportional to the weights
        for i in range(0, self.population_size):
            if (random_num < weights_to_population[i][0]):
                return weights_to_population[i][1]

        
    def crossover(self, parent1, parent2):

        child1 = np.empty(self.individual_size)
        child2 = np.empty(self.individual_size)


        for i in range(0, self.individual_size):

            #Get a random splitting point .
            splitpoint = int(random.uniform(0, 52))

            #Convert both of the parents into a bitstring
            parent1_bitstring = real_to_binary(parent1[i], self.min_value, self.max_value)
            parent2_bitstring = real_to_binary(parent2[i], self.min_value, self.max_value)

            #For child1, piece together the sub-bitstring of parent1 before the splitpoint and 
            #the sub-bitstring of parent2 after the splitpoint.
            #For child2, switch parent1 and parent2 relative placement to the splitpoint
            child1_bitstring = parent1_bitstring[0:splitpoint:1] + parent2_bitstring[splitpoint:52:1]
            child2_bitstring = parent2_bitstring[0:splitpoint:1] + parent1_bitstring[splitpoint:52:1]

            #Convert the newly crossed-over bitstring back into a real number
            child1_num = binary_to_real(child1_bitstring, self.min_value, self.max_value)
            child2_num = binary_to_real(child2_bitstring, self.min_value, self.max_value)

            #Store the new real number
            child1[i] = child1_num
            child2[i] = child2_num

        return (child1, child2)

    def mutate(self, individual):
        new_individual = np.empty((self.individual_size))
        for individual_index in range(0, self.individual_size):
            gene = individual[individual_index]
            gene_bitstring = real_to_binary(gene, self.min_value, self.max_value)

            bit_index = int(random.uniform(0, len(gene_bitstring)))
            if (gene_bitstring[bit_index] == '0'):
                gene_bitstring = gene_bitstring[:bit_index] + '1' + gene_bitstring[bit_index+1:]
            else:
                gene_bitstring = gene_bitstring[:bit_index] + '0' + gene_bitstring[bit_index+1:]
        
            new_gene = binary_to_real(gene_bitstring, self.min_value, self.max_value)
            new_individual[individual_index] = new_gene
        
        return new_individual

    def report_progress(self, population):
        raw_fitness = np.empty((self.population_size, 1))

        #For every individual, calculate the raw fitness
        for weight_index in range(0, self.population_size):
            raw_fitness[weight_index, 0] = self.fitness_function(population[weight_index, :])
        
        min_fitness = np.min(raw_fitness)
        max_fitness = np.max(raw_fitness)

        print("Max fitness: %s" % (max_fitness))
        print("Min fitness: %s" % (min_fitness))
        print()