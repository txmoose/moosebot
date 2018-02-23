import discord
from dice import *
from discord.ext import commands
import time
import os
import xkcd as XKCD

description = '''MooseBot'''

bot = commands.Bot(command_prefix='~', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def sting():
    """Returns a ba dump tss"""
    await bot.say("*ba dump tss*")
    await bot.say("http://i.imgur.com/oEhVvjZ.gif")

@bot.command()
async def train():
    """Returns a Moose Train """
    await bot.say("http://i.imgur.com/aj4iuMB.gifv")

@bot.command()
async def moose():
    """Returns a Moose Train """
    await bot.say("http://i.imgur.com/aj4iuMB.gifv")

@bot.command()
async def botsnack():
    """Returns a Moose Train """
    await bot.say("https://media.giphy.com/media/xT5LMQ8rHYTDGFG07e/giphy.gif")

@bot.command(pass_context=True)
async def roll(ctx, *dice : str):
    """calls my dice roller"""

    modifier = 0
    dice = list(dice)

    for die in dice:
        if re.match('[+-]\s?\d+', die):
            modifier = re.sub(r'\s+', '', die)
            dice.remove(die)

    throw = full_throw(ensure_input(dice))
    output = ''

    for die in throw:
        output += "{} => {}\n".format(die[0], die[1])

    output += "\n{} => {}\n".format("Mod", modifier)

    total = int(modifier)

    for die in throw:
        total += die[1]

    await bot.say("{} rolled:\n```{}\nTotal => {}```".format(ctx.message.author.mention, output, total))

@bot.command(pass_context=True)
async def statroll(ctx):
    """Rolls stats via 4d6 keep 3"""

    dice = ['4d6']
    output = ''
    total = [0] * 6

    for x in range(6):
        throw = full_throw(dice)

        for die in throw:
            output += "{} => {}\n".format(die[0], die[1])

        numbers = []

        for die in throw:
            numbers.append(die[1])

        numbers.remove(min(numbers))
        total[x] = sum(numbers)

        output += "Stat => {}\n\n".format(total[x])

    output += "Stats => {}".format(sorted(total, reverse=True))

    await bot.say("{} rolled:\n```{}```".format(ctx.message.author.mention, output))

@bot.command(pass_context=True)
async def echo(ctx, member : discord.Member = None):
    if member is None:
        member = ctx.message.author
    message = ctx.message
    await bot.say('{0} says: ```{1}```'.format(member, message))

@bot.command()
async def xkcd():
    comic = XKCD.getRandomComic()
    comment = "{0}\n{1}".format(comic.getTitle(), comic.getImageLink())
    await bot.say(comment)
    time.sleep(2)
    await bot.say(comic.getAltText())

@bot.command()
async def xkcdlast():
    comic = XKCD.getLatestComic()
    comment = "{0}\n{1}".format(comic.getTitle(), comic.getImageLink())
    await bot.say(comment)
    time.sleep(2)
    await bot.say(comic.getAltText())

@bot.command()
async def reg_fortune():
    comment = "{}".format(os.popen("/usr/games/fortune 50% futurama 50% starwars").read())
    await bot.say(comment)

@bot.command()
async def fortune():
    comment = "```{}```".format(os.popen("/usr/games/fortune 50% futurama 50% starwars | /usr/games/cowsay").read())
    await bot.say(comment)

@bot.command()
async def sit():
    comment = "*plants his butt*"
    await bot.say(comment)

@bot.command()
async def stay():
    comment = "*wanders off*"
    await bot.say(comment)

@bot.command()
async def speak():
    comment = "http://i.imgur.com/J5BjpEG.png"
    await bot.say(comment)

