from shipping.model import *

from random import random


class GeneticAlgorithm:
    def __init__(self, population_size):
        self.population_size = population_size
        self.population = []
        self.generation = 0
        self.best_solution = 0
        self.solutions_history = []

    def initialize_population(self, spaces, values, spaces_limit):
        for i in range(self.population_size):
            ind = Individual(spaces, values, spaces_limit)
            ind.evaluate()
            self.population.append(ind)
        self.order_population()
        self.best_solution = self.population[0]

    def order_population(self):
        self.population.sort(key=lambda x: x.evaluation_note, reverse=True)

    def best_individual(self, individual):
        if individual.evaluation_note > self.best_solution.evaluation_note:
            self.best_solution = individual

    def population_sum(self):
        evaluation_sum = sum([ind.evaluation_note for ind in self.population])
        return evaluation_sum

    def select_father(self, population_sum):
        father = -1
        sorted_value = random() * population_sum
        _sum, i = 0, 0
        while _sum < sorted_value:
            _sum += self.population[i].evaluation_note
            father += 1
            i += 1
        return father

    def visualize_generation(self):
        best_individual = self.population[0]
        print(f"Generation {self.generation} - > Value: {best_individual.evaluation_note} - > Space: {best_individual.used_space} Chromosomes: {best_individual.chromosomes}")

    def solve(self, mutation_tax, generations, spaces, values, spaces_limit):
        self.initialize_population(spaces, values, spaces_limit)
        self.visualize_generation()
        self.solutions_history.append(self.population[0].evaluation_note)
        for generation in range(generations-1):
            self.generation += 1
            new_generation = []
            population_sum = self.population_sum()
            for generated_individual in range(0, self.population_size, 2):
                father = self.select_father(population_sum)
                mother = self.select_father(population_sum)
                children = self.population[father].crossover(self.population[mother])
                for child in children:
                    child.mutation(mutation_tax)
                    new_generation.append(child)
            self.population = new_generation
            self.order_population()
            self.solutions_history.append(self.population[0].evaluation_note)
            self.best_individual(self.population[0])
            self.visualize_generation()
        print("-----------------------------------")
        print(f"Best solution -> Generation {self.best_solution.generation}: {self.best_solution.evaluation_note}")
        print(f"Space: {self.best_solution.used_space}")
        print(f"Chromosomes: {self.best_solution.chromosomes}")
        print("-----------------------------------")
        return self.best_solution.chromosomes