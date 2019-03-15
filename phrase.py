import random
from cs50 import get_string

target = get_string("What target do you want to match? ")

class Phrase:
    def __init__(self):
        self.characters = []
        for i in range(len(target)):
            character = chr(random.choice(range(32, 127)))
            self.characters.append(character)
    
    def getContents(self):
        return ''.join(self.characters)
    
    def getFitness(self):
        self.fitness = 0
        for i in range(len(self.characters)):
            if self.characters[i] == target[i]:
                self.fitness += 1
    
    def crossover(self, partner):
        child = Phrase()
        for i in range(len(self.characters)):
            if random.random() < 0.5:
                child.characters[i] = self.characters[i]
            else:
                child.characters[i] = partner.characters[i]
        
        return child
    
    def mutate(self, generation):
        for i in range(len(self.characters)):
            if generation > 100:
                mrate = random.random()
                mrate *= (generation / 100)
                if mrate < 0.01:
                    self.characters[i] = chr(random.choice(range(32, 127)))
