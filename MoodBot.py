import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')
bot.remove_command('help')

def getToken():
    tokenFile = open('TOKEN.txt','r')
    tokentxt = tokenFile.read()
    return tokentxt

@bot.event
async def on_ready():
    print("logged in as account: "+str(bot.user))

#help command
@bot.command(name = "help")
async def help(ctx):
    await ctx.channel.send("command prefix: /\ncommands:\nascii")

#ascii command
@bot.command(name = "ascii")
async def ascii(ctx,arg):
    print(f"converting {arg} to ascii")
    try:
        await ctx.channel.send(asciify(arg))
        print("converted")
    except Exception as e:
        print(e)

#ascii converter
def asciify(phrase):
    phrase = phrase.lower()
    str = ""
    art = open("ascii/ascii.txt",'r')
    arttxt = art.read().split("$")
    i = 0
    while(i<10):
        for ch in phrase:
            if ch.isalpha():
                artchar = arttxt[ord(ch)-97]
            else:
                artchar = arttxt[26]
            artline = artchar.split("\n")
            str = str + artline[i]
        str = str + "\n"
        i = i + 1
    str = str + "\n"
    str = "```" + str + "```"
    return str

bot.run(getToken())