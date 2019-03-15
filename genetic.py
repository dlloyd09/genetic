import random

from phrase import Phrase, target
from helpers import summarize
from cs50 import get_int

# prompt the user for a generation size
popSize = get_int("How many individuals in each generation? ")

# keep track of our population, generation, and the best score we've seen so far
population = []
bestScore = 0
generation = 1

# initial population from which other generations will follow
for i in range(popSize):
    population.append(Phrase())

# keep going until we've found the target string
while bestScore < len(target):

    # assess the fitness of each member of the population
    for i in range(popSize):
        population[i].getFitness()

        # if it's the best we've seen so far, let's report on it
        if population[i].fitness > bestScore:
            bestScore = population[i].fitness
            summarize(generation, population[i].getContents(), bestScore)

    # create the mating pool for the next generation
    matingPool = []

    # clear the population array, but save the parents
    parents = population[:]
    population = []

    # for each one of the parents, add it to the mating pool more often if
    # its fitness is higher
    for i in range(popSize):
        for j in range(parents[i].fitness):
            matingPool.append(parents[i])

    # build the next generation
    for i in range(popSize):

        # arbitrarily choose two parents from the mating pool
        x = random.choice(range(len(matingPool)))
        y = random.choice(range(len(matingPool)))

        # crossover/breed those two parents together
        child = matingPool[x].crossover(matingPool[y])

        # small chance that some characters in the child may mutate
        child.mutate()

        # add the child to the next generation's population
        population.append(child)

    # done assessing the current generation
    generation += 1
