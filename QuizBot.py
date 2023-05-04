import discord

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f"{client.user} is now online")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "ping":
        await message.channel.send("pong")

client.run("MTEwMzUwODI0NTk2NTk3OTczOA.GQc7JV.ve2qDq80rUfpllVkkW4VbyjObzLB2_72s3r1rA")