from model import *

from deap import base, creator, tools, algorithms
import matplotlib.pyplot as plt
import numpy as np

import random


spaces = []
values = []
names = []
limit = 3

for product in PRODUCTS:
    spaces.append(product.space)
    values.append(product.value)
    names.append(product.name)


def evaluate(ind):
    note = 0
    sum_spaces = 0
    for i in range(len(ind)):
        if ind[i] == 1:
            note += values[i]
            sum_spaces += spaces[i]
    if sum_spaces > limit:
        note = 1
    return note / 100000,


def main():
    # random.seed(42)
    toolbox = base.Toolbox()
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox.register("attr_bool", random.randint, 0, 1)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=len(spaces))
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", evaluate)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.01)
    toolbox.register("select", tools.selRoulette)

    population = toolbox.population(n=50)
    CXPB = 1  # crossover probability
    MUTPB = 0.01  # mutation probability
    NGEN = 1000  # number of generations

    statistics = tools.Statistics(lambda ind: ind.fitness.values)
    statistics.register("max", np.max)
    statistics.register("min", np.min)
    statistics.register("med", np.mean)
    statistics.register("std", np.std)

    population, info = algorithms.eaSimple(population, toolbox, cxpb=CXPB, mutpb=MUTPB, ngen=NGEN, stats=statistics)

    best_individuals = tools.selBest(population, 2)
    for bi in best_individuals:
        print(bi)
        print(bi.fitness)
        _sum = 0
        for i in range(len(PRODUCTS)):
            if bi[i] == 1:
                _sum += PRODUCTS[i].value
                # print(PRODUCTS[i])

        print("Sum: ", _sum)

    chart = info.select("max")
    plt.plot(chart)
    plt.title("Max Fitness")
    plt.show()


if __name__ == "__main__":
    main()
