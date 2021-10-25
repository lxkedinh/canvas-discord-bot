import discord
from dotenv import load_dotenv
import os

from canvasapi import Canvas

client = discord.Client()


load_dotenv()
#API STUFF
#Canvas API URL
API_URL="https://canvas.ucsc.edu" 
#Canvas API KEY
API_KEY =os.getenv("API_TOKEN")

#Initialize a new Canvas Object
canvas = Canvas(API_URL, API_KEY)


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
                
 #   if message.content.startswith('users?'):  #If bot senses message "AYO"
  #          users = course.get_users()
  #          for user in users:
   #             await message.channel.send(user) #Bot prints fuck jess

    if message.content.startswith('courses?'):  #If bot senses message "courses?"
            users = canvas.get_courses()
            for classe in users:
                await message.channel.send(classe.name) #Bot will print out all of your courses


client.run(os.getenv("TOKEN"))
