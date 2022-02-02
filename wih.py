# WIH bot for Discord servers.
# Developed by M.T.N. in August/September 2021.
# Made with Python 3.7...I think. I don't remember LOL
# This is free software, use as you wish.
# I probably won't maintain this, as I no longer use Discord.
# Questions? Contact me: mtngithub@protonmail.com

'''

HOW TO USE THIS SCRIPT

0. Generate your Discord bot and its token.
    - Stuck? Use the following link to learn how.
    - https://www.writebots.com/discord-bot-token/

1. Install the latest version of Python on your system.

2. Open your command line/terminal.
    - For Windows users, use Win+R, type "cmd", then hit enter.
    - Linux users...I don't think you need help, haha.

3. Edit WIH.py in your preferred text editor. THIS STEP IS VERY IMPORTANT.
    - Make sure to replace all the #your user ID here#s in the code with your user ID (not your tag)!
    - Otherwise, the bot will not work properly :( so you better do it!
    - Make sure to add your bot token too, otherwise it won't run at all!

These next steps are all done within the terminal.

4. Type in "pip install discord" or "pip3 install discord". 
    - This installs the scripts used to be able to connect the bot to Discord.
    - If this doesn't work, search engines and forums are your friends.

5. Go to the folder that WIH.py is in. (Stuck? Look up the cd command how-to guides.)

6. Type in "python WIH.py" or "python3 WIH.py" and hit enter.

Have fun!

'''

import discord
from discord.ext import commands, tasks
import os
import random
import requests

responses8ball = [
        'It is certain.','It is decidedly so.','Without a doubt.','Yes, definitely.','You may rely on it.','As I see it, yes.','Most likely.','Outlook good.','Yes.','Signs point to yes.',
        'Reply hazy, try again.','Ask again later.','Better not tell you now.','Cannot predict now.','Concentrate and ask again.',
        'Don\'t count on it.','My reply is no.','My sources say no.','Outlook not so good.','Very doubtful.']

emoji = [u"\U0001F49C"]# Add your own emoji here!

def Latency():
    global latC
    latC = round(client.latency * 1000) # Checks ping (network speed).

client = commands.Bot(command_prefix = "!") # Use your own bot prefix here (i.e. commands using $ would be $8ball, and !8ball for !).
client.remove_command('help') # Removes the default help command. Delete if you want it for whatever reason, but it's better to make your own.

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Activity(type=discord.ActivityType.playing, name = 'WIH Bot Demo')) # Modify this as you'd like! You just have to rerun the bot script after editing.
    print('Running the bot successfully.') # Says this in the terminal it's running in. Otherwise, it gives an error which means you messed up.

@client.event
async def on_message(message):
    await client.process_commands(message)
    if '' in message.content.lower():
        lolcat = random.randint(1,64)
        if lolcat > 63: # There is a one out of 64 chance for the bot to send a random cat photo after every message. :D
            r = requests.get("https://api.thecatapi.com/v1/images/search").json()
            cat_em = discord.Embed(title = "Random cat picture!", color = 0x9900dd)
            cat_em.set_image(url=f'{r[0]["url"]}')
            await message.channel.send(embed=cat_em)
    if 'lol' in message.content.lower(): # Whenever you type "lol" with the bot online, it will give you a special reaction and give a normal one for everyone else.
        if message.author.id == #your user ID here#:
            await message.add_reaction(u"\U0001F49C") # The u"gibberish" string is a unicode (?) emoji! You can add custom Discord emojis to this too.
        else:
            await message.add_reaction(random.choice(emoji))


# This sends a message to users through the bot!
@client.command()
async def message(ctx, member:discord.User = None, *, reason = None):
    if member == None or reason == None:
        await ctx.channel.send("`No message was sent.`")
        return
    message = reason
    if ctx.message.author.id == #your user ID here#:
        await member.send(message)
        await ctx.channel.send(f"`{member} has been messaged.`")

# Magic 8Ball
@client.command(aliases = ['8ball', 'eightball', 'magic8', '8Ball', '8BALL'])
async def _8ball(ctx, *, question):
    embed = discord.Embed(title = "Magic Eight Ball :8ball:", description = f"{random.choice(responses8ball)}", color = 0x9900dd)
    await ctx.send(content = None, embed = embed)

# This tells you how popular you are (not to scale).
@client.command(aliases = ['popular','relevance'])
async def _popu(ctx):
    x = random.randint(0,100)
    y = str(x)
    embed = discord.Embed(title = "Relevancy", description = f'Your relevancy is {y} percent.', color = 0x9900dd)
    await ctx.send(content = None, embed = embed)

# This checks your bot ping.
@client.command(aliases = ['Ping',  'ping'])
async def _ping(ctx):
    Latency()
    embed = discord.Embed(title = "Latency Test", color = 0x9900dd)
    embed.add_field(name = "Pong.", value = "\n" + str(latC)+ " ms :ping_pong:'")
    await ctx.send(embed = embed)

# This is just a demo from when I was learning how to use widgets lol
@client.command(aliases = ['testing', 'test'])
async def _test(ctx):
    embed = discord.Embed(title = "Test Embed", description = "LOL hi this is a demo", color = 0x9900dd)
    embed.add_field(name = "Test1", value = "Sample text")
    embed.add_field(name = "Test2", value = "More sample text")
    Latency()
    embed.add_field(name = "Response Time", value = str(latC)+ " ms")
    await ctx.send(content = None, embed = embed)

client.run('') # Paste your bot token between the quotes here.

