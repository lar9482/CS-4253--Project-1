import math

#A bunch of additive cooling functions 
#Source:
#http://what-when-how.com/artificial-intelligence/a-comparison-of-cooling-schedules-for-simulated-annealing-artificial-intelligence/

#Either bias toward exploitation or exploration
def linear_schedule(t, T_0 = 1000, T_N = 0, n = 20):
    return (T_N) + (T_0 - T_N)*((n - t) / (n))

#Bias toward exploitation
def quadratic_schedule(t, T_0 = 1000, T_N = 0, n = 20):
    return (T_N) + (T_0 - T_N)*(((n - t) / (n)) ** 2)

#Bias toward exploration
def trigonometric_schedule(t, T_0 = 1000, T_N = 0, n = 2):
    return (T_N) + 0.5*(T_0 - T_N)*(1 + math.cos((t*math.pi) / (n)))