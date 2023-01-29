from simulated_annealing import simulated_annealing

class simulated_annealing_TSP(simulated_annealing):
    def __init__(self, graph, TSP_fitness, TSP_C, min_city = 0, max_city = 5, num_cities = 5, maxProblem = False):
        super().__init__(TSP_fitness, TSP_C, min_city, max_city, num_cities, maxProblem)
        self.graph = graph