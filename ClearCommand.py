# Install discord.py
# Command: pip install discord.py

import discord
from discord.ext import commands

# erm u have to like put ur token here?
TOKEN = 'YOUR_BOT_TOKEN'

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

#prefix settings (i have it set to !)
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def clear(ctx, amount: int):
    if ctx.author.guild_permissions.manage_messages:
        # ghe part that deletes the messages (up to 100 at a time due to api limitations)
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'Successfully cleared {amount} messages.')
    else:
        await ctx.send("You don't have permission to use this command.")


bot.run(TOKEN)
