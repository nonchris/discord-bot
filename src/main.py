import os
import logging

import discord
from discord.ext import commands

from environment import PREFIX, TOKEN

# path for databases or config files
if not os.path.exists('data/'):
    os.mkdir('data/')

# set logging format
formatter = logging.Formatter("[{asctime}] [{levelname}] [{name}] {message}", style="{")

# logger for writing to file
file_logger = logging.FileHandler('data/events.log')
file_logger.setLevel(logging.INFO)  # everything into the logging file
file_logger.setFormatter(formatter)

# logger for console prints
console_logger = logging.StreamHandler()
console_logger.setLevel(logging.WARNING)  # only important stuff to the terminal
console_logger.setFormatter(formatter)

# get new logger
logger = logging.getLogger('my-bot')
logger.setLevel(logging.INFO)

# register loggers
logger.addHandler(file_logger)
logger.addHandler(console_logger)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)


# login message
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected')
    guild = discord.utils.get(bot.guilds)  # , name=GUILD)

    print(f'Bot is connected to the following guilds:')
    print()
    member_count = 0
    for g in bot.guilds:
        print(f"{g.name} - {g.id} - Members: {g.member_count}")
        member_count += g.member_count
    print()
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name=f"{PREFIX}help"))

# LOADING Extensions
bot.remove_command('help')  # unload default help message
initial_extensions = [
    'cogs.misc',
    'cogs.help'
]

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

    bot.run(TOKEN)
