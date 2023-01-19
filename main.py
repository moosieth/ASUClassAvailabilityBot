import discord
import os

tokenFile = open(os.environ.get('TOKEN'), 'r')

TOKEN = tokenFile.readline()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event

async def on_ready():
    print('We have successfully loggged in as {0.user}'.format(client))

@client.event

async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'hello':
        await message.channel.send(f'Hello, {message.author.mention}!')
        return

    if message.content.lower() == 'bye':
        await message.channel.send(f'See you later, {message.author.mention}!')
        return

    if message.content.lower() == '#ping':
        await message.channel.send(f'Wow, how original...')
        return

        
client.run(TOKEN)