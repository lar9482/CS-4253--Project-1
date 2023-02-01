from SA.schedule import linear_schedule, quadratic_schedule, trigonometric_schedule
from SA.simulated_annealing import simulated_annealing
from SA.simulated_annealing_TSP import simulated_annealing_TSP
from utils.ga_eval import sphere, griew, shekel, micha, langermann, odd_square, bump, _plot_f, _mesh
from utils.ga_eval import sphere_c, griew_c, shekel_c, micha_c, langermann_c, odd_square_c, bump_c
from utils.TSP import TSP_15,TSP_26, TSP_C, TSP_fitness

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
# f_params = {bump: [bump_c, math.sqrt(0.75), 15]}

TSP_params = {'TSP_15': [TSP_15, 0, 14],
              'TSP_26': [TSP_26, 0, 25]}

#These are the parameters that will be varied
possible_schedules = [linear_schedule, quadratic_schedule, trigonometric_schedule]
possible_k = [500, 1000, 2500, 5000, 10000]

#These are the parameters that will be fixed throughout the tests
T_0 = 1000
T_Final = 0
dim = 2
maxProblem = False

def SA_function_tests():

    #Scanning through all of the possible functions in 'f_params'
    for f in f_params.keys():

        #The results(values) and states(2-d vectors) to store from the SA results
        all_results = []
        all_states = [] 

        #For all possible k and schedule combinations,
        #run the SA algorithm and store them in 'all_results' and 'all_states'
        for k in possible_k:
            results_k = []
            states_k = []
            for schedule in possible_schedules:
                SA = simulated_annealing(f, f_params[f][0], f_params[f][1], f_params[f][2], dim, maxProblem)
                state = SA.run_algorithm(schedule, T_0, T_Final, k)
                value = f(state)
                states_k.append(np.array2string(state))
                results_k.append(value)
            all_states.append(states_k)
            all_results.append(results_k)

        #Once the tests are over, save 'all_results' and 'all_states' as Excel spreadsheets
        schedule_names = [str(i).split(' ')[1] for i in possible_schedules]
        df_states = pd.DataFrame(all_states, index=possible_k, columns=schedule_names)
        df_results = pd.DataFrame(all_results, index=possible_k, columns=schedule_names)
        df_states.to_excel(str(f).split(' ')[1] + '_states_SA.xlsx', sheet_name=str(f).split(' ')[1])
        df_results.to_excel(str(f).split(' ')[1] + '_results_SA.xlsx', sheet_name=str(f).split(' ')[1])

    
def SA_TSP_tests():

    #Scanning through all possible TSP graph options in 'TSP_params'
    for g in TSP_params:
        all_states = []
        all_results = []
        #For all possible k and schedule combinations,
        #run the SA algorithm and store them in 'all_results' and 'all_states'
        for k in possible_k:
            results_k = []
            states_k = []
            for schedule in possible_schedules:
                SA_TSP = simulated_annealing_TSP(TSP_params[g][0], TSP_fitness, TSP_C, 
                                                 TSP_params[g][1], TSP_params[g][2],
                                                 TSP_params[g][2]+1, maxProblem)

                state = SA_TSP.run_algorithm(schedule, T_0, T_Final, k)
                value = SA_TSP.value_function(state)

                states_k.append(np.array2string(state))
                results_k.append(value)
            
            all_states.append(states_k)
            all_results.append(results_k)
        
        #Once the tests are over, save 'all_results' and 'all_states' as Excel spreadsheets
        schedule_names = [str(i).split(' ')[1] for i in possible_schedules]
        df_states = pd.DataFrame(all_states, index=possible_k, columns=schedule_names)
        df_results = pd.DataFrame(all_results, index=possible_k, columns=schedule_names)
        df_states.to_excel(g + '_states_SA.xlsx', sheet_name=g)
        df_results.to_excel(g + '_results_SA.xlsx', sheet_name=g)
