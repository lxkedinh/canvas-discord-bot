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

#Ask for user to log in
@bot.command()
async def login(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))



@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)


@bot.command()
async def testa(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

@bot.command()
async def AYO(ctx):
    for i in range(1,3):
        await ctx.send('love u jess')


#Ask user to log into canvas, take the API_URL and get an API token
# @bot.command()
# if message.content.startswith('LOGMEIN'):  #If bot senses message "AYO"
#     await message.channel.send('Okay logging you in') #Bot prints fuck jess

# @bot.command()        
# async def users(ctx):
#     users = canvas.get_users()
#     for user in users:
#         await ctx.send(user) #Bot prints fuck jess






#Command to view self
@bot.command()   
async def metoo(ctx):
    await ctx.send(Canvasuser.name)



@bot.command()   
async def courses(ctx):
    users = Canvasuser.get_courses(enrollment_status='active')
    for classe in users:
        print(classe.name)
        await ctx.send(classe) #Bot will print out all of your courses


bot.run(os.getenv("TOKEN"))
