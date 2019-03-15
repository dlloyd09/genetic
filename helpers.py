from phrase import target
from termcolor import colored

def colorize(s):
    for i in range(len(s)):
        if s[i] == target[i]:
            print(colored(s[i], "green"), end="")
        else:
            print(colored(s[i], "red"), end="")

def summarize(gen, phr, fit):
    print(f"Generation #{gen:3}: ", end="")
    colorize(phr)
    print(f"  score: {fit:2}/{len(target)}")

