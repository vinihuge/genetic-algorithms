from random import random


class Individual:

    def __init__(self, spaces, values, spaces_limit, generation=0):
        self.spaces = spaces
        self.values = values
        self.spaces_limit = spaces_limit
        self.evaluation_note = 0
        self.used_space = 0
        self.generation = generation
        self.chromosomes = []
        self.generate_chromosomes()

    def generate_chromosomes(self):
        for i in range(len(self.spaces)):
            if random() < 0.5:
                self.chromosomes.append("0")
            else:
                self.chromosomes.append("1")

    def evaluate(self):
        note = 0
        sum_spaces = 0
        for i in range(len(self.chromosomes)):
            if self.chromosomes[i] == "1":
                note += self.values[i]
                sum_spaces += self.spaces[i]
        if sum_spaces > self.spaces_limit:
            note = 1
        self.evaluation_note = note
        self.used_space = sum_spaces

    def crossover(self, other_individual):
        cut = round(random() * len(self.chromosomes))
        children1 = other_individual.chromosomes[0:cut] + self.chromosomes[cut::]
        children2 = self.chromosomes[0:cut] + other_individual.chromosomes[cut::]
        childrens = [
            Individual(self.spaces, self.values, self.spaces_limit, self.generation + 1),
            Individual(self.spaces, self.values, self.spaces_limit, self.generation + 1)
        ]
        childrens[0].chromosomes = children1
        childrens[1].chromosomes = children2
        return childrens

    def mutation(self, tax):
        for i in range(len(self.chromosomes)):
            if random() < tax:
                if self.chromosomes[i] == "1":
                    self.chromosomes[i] = "0"
                else:
                    self.chromosomes[i] = "1"
        self.evaluate()
