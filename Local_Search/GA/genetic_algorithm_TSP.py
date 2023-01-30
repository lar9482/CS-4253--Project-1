from genetic_algorithm import genetic_algorithm

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

    def __initialize_population(self, population_size, individual_size, min_value, max_value):
        return super().__initialize_population(population_size, individual_size, min_value, max_value)

    def __crossover(self, parent1, parent2):
        return super().__crossover(parent1, parent2)

    def __mutate(self, individual):
        return super().__mutate(individual)