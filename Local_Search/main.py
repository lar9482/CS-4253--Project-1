from utils.ga_util import bitstr2float, real_to_binary, binary_to_real
from utils.ga_eval import sphere, shekel, micha, langermann, odd_square, bump
import random
from genetic_algorithm import genetic_algorithm

def main():
    algo = genetic_algorithm(sphere)
    print()

if __name__ == "__main__":
    main()