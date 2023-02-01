from utils.ga_eval import sphere, griew, shekel, micha, langermann, odd_square, bump, _plot_f, _mesh
from utils.ga_eval import sphere_c, griew_c, shekel_c, micha_c, langermann_c, odd_square_c, bump_c
from utils.TSP import TSP_15,TSP_26, TSP_C, TSP_fitness

from GA.genetic_algorithm import genetic_algorithm
from GA.genetic_algorithm_TSP import genetic_algorithm_TSP

import numpy as np
import pandas as pd
import math

# {function_name: [constraint_function, min_value, max_value]}
f_params = {sphere: [sphere_c, -5, 5],
                   griew: [griew_c, 0, 100],
                   shekel: [shekel_c, 0, 10],
                   micha: [micha_c, -100, 100],
                   langermann: [langermann_c, 0, 10],
                   odd_square: [odd_square_c, -5*np.pi, 5*np.pi],
                   bump: [bump_c, math.sqrt(0.75), 15]}

TSP_params = {'TSP_15': [TSP_15, 0, 14],
              'TSP_26': [TSP_26, 0, 25]}

possible_population = [10, 100]
possible_crossover = [0, 0.5, 0.75, 1]
possible_mutation = [0, 0.05, 0.1, 0.25]
num_generation = 100
dim = 2
maxProblem = False
elitism_applied = True

def GA_function_tests():
    for f in f_params.keys():

        for population in possible_population:
            all_states = []
            all_results = []
            for cross_over in possible_crossover:
                states_cross = []
                results_cross = []
                for mutation in possible_mutation:
                    GA = genetic_algorithm(f, population, dim, cross_over, mutation,
                                           f_params[f][1], f_params[f][2], 
                                           maxProblem, elitism_applied)
                    (fitness, individual) = GA.run_algorithm(num_generation)
                    
                    states_cross.append(np.array2string(individual))
                    results_cross.append(fitness)

                all_states.append(states_cross)
                all_results.append(results_cross)
            
            df_states = pd.DataFrame(all_states, index=possible_crossover, columns=possible_mutation)
            df_results = pd.DataFrame(all_results, index=possible_crossover, columns=possible_mutation)
            df_states.to_excel(str(f).split(' ')[1] + '_' +str(population) +'_states_GA.xlsx', sheet_name=str(f).split(' ')[1])
            df_results.to_excel(str(f).split(' ')[1] + '_'+str(population) +'_results_GA.xlsx', sheet_name=str(f).split(' ')[1])