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

    embed = discord.Embed(
        title = "Help: Command Prefix '/'",
        colour = discord.Colour.from_rgb(0,255,255),
        url = "https://github.com/CSE-23",
        description = "lists all possible commands")
    
    embed.add_field(name="help", value="displays this message", inline=False)
    embed.add_field(name="ascii <text>", value="converts your text to ascii art", inline=False)

    await ctx.channel.send(embed = embed)


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