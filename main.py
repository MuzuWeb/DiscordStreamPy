import discord
from discord.ext import commands

token = "Votre Token"

bot = commands.Bot(command_prefix = "123456789")

status = "Votre Statut"

@bot.event
async def on_connect():
    stream = discord.Streaming(
        name = status,
        url = 'https://www.twitch.tv/twitch'
    )
    print('Tu stream : ' + status)
    await bot.change_presence(activity=stream)

bot.run(token, bot=False)  
