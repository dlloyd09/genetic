import random
from cs50 import get_string

# ask the user for a target string
target = get_string("What target do you want to match? ")

class Phrase:

    # constructor method
    def __init__(self):
        self.characters = []

        # append len(target) number of randomly chosen printable ASCII chars
        for i in range(len(target)):
            character = chr(random.choice(range(32, 127)))
            self.characters.append(character)

    # render the character array as a string instead of an array of chars
    def getContents(self):
        return ''.join(self.characters)

    # score the current entity's fitness by counting matches to target
    def getFitness(self):
        self.fitness = 0
        for i in range(len(self.characters)):
            if self.characters[i] == target[i]:
                self.fitness += 1

    # create a child of two members of the current generation
    def crossover(self, partner):

        # create a spot for the characters to go
        child = Phrase()

        # flip a coin for each character, selecting from one parent each time
        for i in range(len(self.characters)):
            if random.random() < 0.5:
                child.characters[i] = self.characters[i]
            else:
                child.characters[i] = partner.characters[i]

        return child

    # some portion of the time, need some characters to randomly change
    def mutate(self):

        # less than 1% of the time, change a character into something else
        for i in range(len(self.characters)):
            if random.random() < 0.01:
                self.characters[i] = chr(random.choice(range(32, 127)))
