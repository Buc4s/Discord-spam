from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.command(name='spam', help='Spams the input message for x number of times')
async def spam(ctx, amount:int, *, message):
    for i in range(amount): # Do the next thing amount times
        await ctx.send(message) # Sends message where command was called

Print = ("The bot is now on, if you close this it Will be offline")

bot.run('Bot token here')
