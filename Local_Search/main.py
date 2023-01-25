from utils.ga_util import bitstr2float, real_to_binary, binary_to_real
from utils.ga_eval import sphere, shekel, micha, langermann, odd_square, bump
import random
from genetic_algorithm import genetic_algorithm

def main():
    # algo = genetic_algorithm(shekel, 10, 0.05, 0.05, 11, 11)
    # algo.run_algorithm(1)


    min_value = -50
    max_value = 50

    test1 = -10
    test2 = 10
    # test3 = 50
    # test4 = 67.52354432145

    bitTest1 = real_to_binary(test1, min_value, max_value)
    bitTest2 = real_to_binary(test2, min_value, max_value)

    # bitTest3 = real_to_binary(test3, min_value, max_value)
    # bitTest4 = real_to_binary(test4, min_value, max_value)

    # print(bitTest1)
    # print(bitTest2)
    # print(bitTest3)
    # print(bitTest4)

    print(binary_to_real(bitTest1, min_value, max_value))
    print(binary_to_real(bitTest2, min_value, max_value))
    # print(binary_to_real(bitTest3, min_value, max_value))
    # print(binary_to_real(bitTest4, min_value, max_value))

    print()

if __name__ == "__main__":
    main()