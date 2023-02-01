from Local_Search.SA.schedule import linear_schedule, quadratic_schedule, trigonometric_schedule
from Local_Search.utils.ga_eval import sphere, griew, shekel, micha, langermann, odd_square, bump, _plot_f, _mesh

from Local_Search.utils.ga_eval import sphere_c, griew_c, shekel_c, micha_c, langermann_c, odd_square_c, bump_c

import numpy as np
# import pandas as pd

#{function_name: [constraint_function, min_value, max_value]}
function_params = {sphere: [sphere_c, -5, 5],
                   griew: [griew_c, 0, 100],
                   shekel: [shekel_c, 0, 10],
                   micha: [micha_c, -100, 100],
                   langermann: [langermann_c, 0, 10],
                   odd_square: [odd_square_c, -5*np.pi, 5*np.pi],
                   bump: [bump_c, 0, 100]}

TSP_params = {}

#These are the parameters that will be varied
possible_schedules = [linear_schedule, quadratic_schedule, trigonometric_schedule]
possible_k = [500, 1000, 5000, 7500]

#These are the parameters that will be fixed throughout the tests
T_0 = 100
T_Final = 0
dim = 2
maxProblem = False

def SA_function_tests():
    print()