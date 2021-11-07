from canvasapi.current_user import CurrentUser
import discord
import aiohttp
from discord.ext import commands
from discord.webhook import AsyncWebhookAdapter, Webhook
from dotenv import load_dotenv
import os
from canvasapi import Canvas, requester


load_dotenv()
# API STUFF
# Canvas API URL


API_URL = "https://canvas.ucsc.edu"
# Canvas API KEY
API_KEY = os.getenv("API_TOKEN")
canvas = Canvas(API_URL, API_KEY)
Canvasuser = canvas.get_current_user()

intents = discord.Intents.default()
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix='/',
                   description="description", intents=intents)


@bot.event
async def on_ready():  # bot is working and ready
    print('We have logged in as {0.user}'.format(bot))
    print("------------------------------\n")

# /Call announcements  and prints out announcements for specific class


@bot.command()
async def announcements(ctx):
    lst = [46335]
    users = canvas.get_announcements(lst)
    for classe in users:
        print(classe, '\n')
        await ctx.send(classe)  # Bot will print out all of your courses
        await ctx.send(classe.message)

# Call /courses and the bot will print out all of the courses you are enrolled in.


@bot.command()
async def courses(ctx):
    users = Canvasuser.get_courses(
        enrollment_state='active', enrollment_type='student', state=['avaliable'])
    for classe in users:
        print(classe.name)
        await ctx.send(classe)  # Bot will print out all of your courses

bot.run(os.getenv("TOKEN"))
