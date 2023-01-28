#A bunch of multiplicative cooling functions 
def exponential_schedule(t, T_0 = 1000, alpha = 0.8):
    return (T_0)*(alpha ** t)

def linear_schedule(t, T_0 = 1000, alpha = 0.8):
    return (T_0) / (1 + alpha*t)

def quadratic_schedule(t, T_0 = 1000, alpha = 0.8):
    return (T_0) / (1 + alpha*(t ** 2))
