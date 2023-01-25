from utils.ga_util import bitstr2float, real_to_binary, binary_to_real
from utils.ga_eval import sphere, shekel, micha, langermann, odd_square, bump
import random
from genetic_algorithm import genetic_algorithm

def main():
    fitness_function = sphere
    population_size = 100
    individual_size = 10
    crossover_rate = 1
    mutation_rate = 0.05
    min_value = 0
    max_value = 100
    maxProblem = False

    algo = genetic_algorithm(fitness_function, population_size, individual_size, crossover_rate, mutation_rate, min_value, max_value, maxProblem)
    algo.run_algorithm(1)


if __name__ == "__main__":
    main()