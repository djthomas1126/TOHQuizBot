import random
import os
import time

directory = os.path.dirname(__file__)

namesFile = open("EpisodeNames.txt")
episodeNames = namesFile.readlines()

def generateQuote(speakerGiven):
    episodeIndex = random.randint(0, len(episodeNames) - 1)
    name = episodeNames[episodeIndex].strip("\n")
    if speakerGiven:
        file = open(directory + "\\" + "NamedTranscripts\\" + name + ".txt")
    else:
        file = open(directory + "\\" + "UnnamedTranscripts\\" + name + ".txt")
    allQuotes = file.readlines()
    lineNumber = random.randint(0, len(allQuotes) - 1)
    quote = allQuotes[lineNumber]
    return quote, name


quote, name = generateQuote(True)
print("Your quote is:\n")

print(quote)

print("What is the name of the episode this quote is from?")
guess = input("> ")
guess = guess.replace(" ", "")
guess = guess.replace("'", "")
guess = guess.replace(",", "")
guess = guess.lower()

if guess == name.lower():
    print("Correct!\n")
else:
    print("Sorry, that is incorrect. The correct answer was:")
    print(name)


