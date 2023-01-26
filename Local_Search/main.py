from utils.ga_util import bitstr2float, real_to_binary, binary_to_real
from utils.ga_eval import sphere, shekel, micha, langermann, odd_square, bump
import random
from genetic_algorithm import genetic_algorithm
import numpy as np

def main():
    fitness_function = sphere
    population_size = 100
    individual_size = 2
    crossover_rate = 1
    mutation_rate = 0.05
    min_value = -5
    max_value = 5
    maxProblem = False

    # algo = genetic_algorithm(fitness_function, population_size, individual_size, crossover_rate, mutation_rate, min_value, max_value, maxProblem)
    # algo.run_algorithm(1000)

    test1 = np.array([1, 5])
    test2 = np.array([5, 1])
    print(langermann(test1))
    print(langermann(test2))


if __name__ == "__main__":
    main()