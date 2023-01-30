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

    #Implementing ordered crossover
    def crossover(self, parent1, parent2):
        first_splitpoint = int(random.uniform(0, self.individual_size))
        second_splitpoint = int(random.uniform(0, self.individual_size))

        while (second_splitpoint < first_splitpoint):
             second_splitpoint = int(random.uniform(0, self.individual_size))

        # print(parent1[0:first_splitpoint:1])
        # print(parent2[first_splitpoint:second_splitpoint:1])
        # print()
        # print(parent2[0:first_splitpoint:1])
        # print(parent1[first_splitpoint:second_splitpoint:1])

        child1 = np.concatenate((parent1[0:first_splitpoint:1], parent2[first_splitpoint:second_splitpoint:1]))
        child2 = np.concatenate((parent2[0:first_splitpoint:1], parent1[first_splitpoint:second_splitpoint:1]))

        child1 = np.concatenate((child1, parent1[second_splitpoint:self.individual_size:1]))
        child2 = np.concatenate((child2, parent2[second_splitpoint:self.individual_size:1]))

        return (child1, child2)

    def mutate(self, individual):
        #Copy the values of 'individual' into a new individual
        new_individual = np.empty(len(individual), dtype=np.int32)
        for i in range(0, len(individual)):
            new_individual[i] = int(individual[i])

        #Get two random indexes for the new individual
        first_index = int(random.uniform(self.min_value, self.max_value))
        second_index = int(random.uniform(self.min_value, self.max_value))

        #Ensure that the indices are not equal to guarantee some change happens
        while (second_index == first_index):
            second_index = int(random.uniform(self.min_value, self.max_value))

        #Swap the values at the choosen indices in 'new_individual'
        new_individual[[second_index, first_index]] = new_individual[[first_index, second_index]]

        return new_individual