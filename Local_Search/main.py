from utils.ga_util import bitstr2float, real_to_binary, binary_to_real
from utils.ga_eval import sphere, griew, shekel, micha, langermann, odd_square, bump, _plot_f, _mesh

from utils.ga_eval import sphere_c, griew_c, shekel_c, micha_c, langermann_c, odd_square_c

from GA.genetic_algorithm import genetic_algorithm
from SA.simulated_annealing import simulated_annealing
from SA.schedule import linear_schedule, quadratic_schedule, trigonometric_schedule

from utils.TSP import TSP_fitness, TSP_C, TSP_5, TSP_15
from SA.simulated_annealing_TSP import simulated_annealing_TSP
from GA.genetic_algorithm_TSP import genetic_algorithm_TSP

import matplotlib.pyplot as plt

import numpy as np

def run_general_tests():
    _plot_f(sphere, *_mesh(-5, 5, -5, 5), title="The Sphere Function")
    _plot_f(griew, *_mesh(0, 200, 0, 200), title="Griewank's function")
    _plot_f(shekel, *_mesh(0, 10, 0, 10), title="Modified Shekel's Foxholes")
    _plot_f(micha, *_mesh(-10, 10, -10, 10), title="Michalewitz's function")
    _plot_f(langermann, *_mesh(0, 10, 0, 10), title="Langermann's function")
    _plot_f(odd_square, *_mesh(-5 * np.pi, 5 * np.pi, -5 * np.pi, 5 * np.pi), title="Odd Square Function")
    _plot_f(bump, *_mesh(0.1, 5, 0.1, 5), title="The Bump Function")

def run_genetic_algorithm_tests():
    fitness_function = sphere
    population_size = 10
    individual_size = 2
    crossover_rate = 1
    mutation_rate = 0.25
    min_value = -5
    max_value = 5
    maxProblem = False
    elitism_applied = True

    algo = genetic_algorithm(fitness_function, population_size, individual_size, crossover_rate, mutation_rate, min_value, max_value, maxProblem, elitism_applied)
    algo.run_algorithm(100)
    print()

def run_simulated_annealing_tests():
    value_function = shekel
    constraint_function = shekel_c
    min_value = 0
    max_value = 10
    dim = 2
    maxProblem = False
    algo = simulated_annealing(value_function, constraint_function, min_value, max_value, dim, maxProblem)

    schedule = trigonometric_schedule
    T_0 = 1
    T_Final = 0
    k = 5000
    test1 = algo.run_algorithm(schedule, T_0, T_Final, k)

    print()

def test_TSP_SA():
    graph = TSP_15
    value_function = TSP_fitness
    constraint_function = TSP_C
    min_value = 0
    max_value = 14
    dim = 15
    maxProblem = False

    algo = simulated_annealing_TSP(graph, value_function, constraint_function, min_value, max_value, dim, maxProblem)
    schedule = trigonometric_schedule
    T_0 = 50
    T_Final = 0
    k = 2500
    test1 = algo.run_algorithm(schedule, T_0, T_Final, k)
    print()

def test_TSP_GA():
    graph = TSP_15
    TSP_Fitness = TSP_fitness
    TSP_c = TSP_C

    population_size = 100
    individual_size = 15
    crossover_rate = 1
    mutation_rate = 0.35
    min_value = 0
    max_value = 14
    maxProblem = False
    elitism_applied = True

    algo = genetic_algorithm_TSP(graph, TSP_Fitness, TSP_c, population_size, individual_size, crossover_rate,
                                 mutation_rate, min_value, max_value, maxProblem, elitism_applied)
    algo.run_algorithm(100)
    print()

def main():
    # run_general_tests()
    run_genetic_algorithm_tests()
    # run_simulated_annealing_tests()
    # test_TSP_SA()
    # test_TSP_GA()

if __name__ == "__main__":
    main()