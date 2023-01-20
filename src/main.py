import discord
import os
import scraper

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

    if message.content.lower()[:7] == '#search':
        await message.channel.send(f'Searching for class # {message.content.lower()[8:]}...')

        if scraper.scrape(f'https://catalog.apps.asu.edu/catalog/classes/classlist?advanced=true&campusOrOnlineSelection=C&classNbr={message.content.lower()[8:]}&honors=F&promod=F&searchType=open&term=2231') == 1:
            await message.channel.send(f'Class {message.content.lower()[8:]} has seats!!!')
            return
        
        await message.channel.send(f'The class you requested has no seats in it :(')
        return

        
client.run(TOKEN)