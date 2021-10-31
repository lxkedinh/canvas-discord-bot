from canvasapi.current_user import CurrentUser
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from canvasapi import Canvas, requester


load_dotenv()
#API STUFF
#Canvas API URL



API_URL="https://canvas.ucsc.edu" 
#Canvas API KEY
API_KEY =os.getenv("API_TOKEN")
canvas = Canvas(API_URL, API_KEY)
Canvasuser = canvas.get_current_user()



intents = discord.Intents.default()
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix='/', description="description", intents=intents)


@bot.event
async def on_ready():# bot is working and ready
    print('We have logged in as {0.user}'.format(bot))
    print("------------------------------\n")


@bot.command()
async def login(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))


# /Call announcements  and prints out announcements for specific class
@bot.command()   
async def announcements(ctx):
    lst = [46335] 
    users = canvas.get_announcements(lst)
    for classe in users:
        print(classe, '\n')
        await ctx.send(classe) #Bot will print out all of your courses
        await ctx.send(classe.message)



#
#@bot.command()
#async def testa(ctx, *args):
#    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))
#Ask user to log into canvas, take the API_URL and get an API token
# @bot.command()
# if message.content.startswith('LOGMEIN'):  #If bot senses message "AYO"
#     await message.channel.send('Okay logging you in') #Bot prints fuck jess

# @bot.command()        
# async def users(ctx):
#     users = canvas.get_users()
#     for user in users:
#         await ctx.send(user) #Bot prints fuck jess


# /metoo   Command to view your name
@bot.command()   
async def metoo(ctx):
    await ctx.send(Canvasuser.name)


#Call /courses and the bot will print out all of the courses you are enrolled in.
@bot.command()   
async def courses(ctx):
    users = Canvasuser.get_courses(enrollment_state='active', enrollment_type='student', state=['avaliable'])
    for classe in users:
        print(classe.name)
        await ctx.send(classe) #Bot will print out all of your courses


#############################################USELESS SHIT################################################
# /ping pong
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# /sum to add two numbers
@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

# /AYO to print love u jess 3 times
@bot.command()
async def AYO(ctx):
    for i in range(1,3):
        await ctx.send('love u jess')
#############################################USELESS SHIT################################################



bot.run(os.getenv("TOKEN"))
