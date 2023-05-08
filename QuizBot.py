import discord
import subprocess
import random
import os

BotToken = os.environ["TOH_QUIZ_BOT_TOKEN"]
directory = os.path.dirname(__file__)

namesFile = open("EpisodeNames.txt")
episodeNames = namesFile.readlines()

def generateQuote(speakerGiven):
    episodeIndex = random.randint(0, len(episodeNames) - 1)
    name = episodeNames[episodeIndex].strip("\n")
    if speakerGiven == "EASY":
        file = open(directory + "\\" + "NamedTranscripts\\" + name + ".txt")
    else:
        file = open(directory + "\\" + "UnnamedTranscripts\\" + name + ".txt")
    allQuotes = file.readlines()
    lineNumber = random.randint(0, len(allQuotes) - 1)
    quote = allQuotes[lineNumber]
    return quote, name

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    global quizActive
    global mode
    quizActive = False
    mode = "NONE"
    print(f"{client.user} is now online")

@client.event
async def on_message(message):
    global quizActive
    global name
    global mode
    if message.author == client.user:
        return
    if quizActive:
        if (mode == "NONE"):
            if message.content.upper() == "EASY":
                mode = "EASY"
                await message.channel.send("What episode is the following quote from?")
                quote, name = generateQuote(mode)
                await message.channel.send(quote)
            elif message.content.upper() == "HARD":
                mode = "HARD"
                await message.channel.send("What episode is the following quote from?")
                quote, name = generateQuote(mode)
                await message.channel.send(quote)
            else:
                mode = "NONE"
                await message.channel.send("Input could not be understood, please try again.")
                return
        else:
            guess = message.content
            guess = guess.replace(" ", "")
            guess = guess.replace("'", "")
            guess = guess.replace(",", "")
            guess = guess.lower()
            if guess == name.lower():
                await message.channel.send("Correct!")
            else:
                await message.channel.send("Incorrect. The correct answer is: " + name)
            quizActive = False
            mode = "NONE"
    elif message.content == "!quiz":
        quizActive = True
        await message.channel.send("Which mode would you like to play? Enter:\n```EASY``` or ```HARD```")

client.run(BotToken)
