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
    if speakerGiven:
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
    quizActive = False
    print(f"{client.user} is now online")

@client.event
async def on_message(message):
    global quizActive
    global name
    if message.author == client.user:
        return
    if quizActive:
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
    elif message.content == "!quiz":
        quizActive = True
        await message.channel.send("What episode is the following quote from?")
        quote, name = generateQuote(True)
        await message.channel.send(quote)

client.run(BotToken)
