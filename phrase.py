import random

from phrase import Phrase, target
from helpers import summarize
from cs50 import get_int

popSize = get_int("How many individuals in each generation? ")
population = []
bestScore = 0
generation = 1

for i in range(popSize):
    population.append(Phrase())

while bestScore < len(target):
    
    for i in range(popSize):
        population[i].getFitness()
        
        if population[i].fitness > bestScore:
            bestScore = population[i].fitness
            summarize(generation, population[i].getContents(), bestScore)
    
    matingPool = []
    
    parents = population[:]
    population = []
    
    for i in range(popSize):
        for j in range(parents[i].fitness):
            matingPool.append(parents[i])
    
    for i in range(popSize):
        x = random.choice(range(len(matingPool)))
        y = random.choice(range(len(matingPool)))
        
        child = matingPool[x].crossover(matingPool[y])
        child.mutate(generation)
        
        population.append(child)

    generation += 1
