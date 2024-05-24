from controller import *
from model import *

import matplotlib.pyplot as plt


def main():
    spaces = []
    values = []
    names = []
    for product in PRODUCTS:
        spaces.append(product.space)
        values.append(product.value)
        names.append(product.name)

    limit = 3
    population_size = 20
    generations = 2000
    mutation_tax = 0.01

    ga = GeneticAlgorithm(population_size)
    result = ga.solve(mutation_tax, generations, spaces, values, limit)

    # for i in range(len(PRODUCTS)):
    #     if result[i] == "1":
    #         print(f"Name: {names[i]} -> Value: {values[i]}")
    plt.plot(ga.solutions_history)
    plt.title("Best solution Evolution")
    plt.show()


if __name__ == "__main__":
    main()
