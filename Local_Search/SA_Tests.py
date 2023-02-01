from SA.schedule import linear_schedule, quadratic_schedule, trigonometric_schedule
from SA.simulated_annealing import simulated_annealing
from SA.simulated_annealing_TSP import simulated_annealing_TSP
from utils.ga_eval import sphere, griew, shekel, micha, langermann, odd_square, bump, _plot_f, _mesh

from utils.ga_eval import sphere_c, griew_c, shekel_c, micha_c, langermann_c, odd_square_c, bump_c

import numpy as np
import pandas as pd

#{function_name: [constraint_function, min_value, max_value]}
f_params = {sphere: [sphere_c, -5, 5],
                   griew: [griew_c, 0, 100],
                   shekel: [shekel_c, 0, 10],
                   micha: [micha_c, -100, 100],
                   langermann: [langermann_c, 0, 10],
                   odd_square: [odd_square_c, -5*np.pi, 5*np.pi],
                   bump: [bump_c, 0.75, 15]}

TSP_params = {}

#These are the parameters that will be varied
possible_schedules = [linear_schedule, quadratic_schedule, trigonometric_schedule]
possible_k = [500, 1000, 2500, 5000, 10000]

#These are the parameters that will be fixed throughout the tests
T_0 = 1000
T_Final = 0
dim = 2
maxProblem = False

def SA_function_tests():
    for f in f_params.keys():
        all_results = []

        for k in possible_k:
            results_k = []
            for schedule in possible_schedules:
                SA = simulated_annealing(f, f_params[f][0], f_params[f][1], f_params[f][2], dim, maxProblem)
                state = SA.run_algorithm(schedule, T_0, T_Final, k)
                value = f(state)
                results_k.append(value)
            
            all_results.append(results_k)
    
        schedule_names = [str(i).split(' ')[1] for i in possible_schedules]
        df = pd.DataFrame(all_results, index=possible_k, columns=schedule_names)
        df.to_excel(str(f).split(' ')[1] + '_SA.xlsx', sheet_name=str(f).split(' ')[1])
    # print(df)
    # print()

    


