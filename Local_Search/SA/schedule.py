import math

#A bunch of additive cooling functions 
# def exponential_schedule(t, T_0 = 1000, T_N = 0, n = 10):
#     return (T_0)*(alpha ** t)

def linear_schedule(t, T_0 = 1000, T_N = 0, n = 2):
    return (T_N) + (T_0 - T_N)*((n - t) / (n))

def quadratic_schedule(t, T_0 = 1000, T_N = 0, n = 2):
    return (T_N) + (T_0 - T_N)*(((n - t) / (n)) ** 2)

def trigonometric_schedule(t, T_0 = 1000, T_N = 0, n = 2):
    return (T_N) + 0.5*(T_0 - T_N)*(1 + math.cos((t*math.pi) / (n)))