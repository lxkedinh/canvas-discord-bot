import discord
from dotenv import load_dotenv
import os

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():# bot is working and ready
        print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): #If bot senses a message in the server
    if message.author == client.user: #If I'm sending the message then don't do anything
        return

    if message.content.startswith('AYO'):  #If bot senses message "AYO"
            for i in range(1,10):
                await message.channel.send('love u jess') #Bot prints fuck jess

client.run(os.getenv("TOKEN"))
