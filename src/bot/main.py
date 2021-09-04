#!/bin/env python
import os

import discord
from discord.ext import commands

# setup of logging and env-vars
# logging must be initialized before environment, to enable logging in environment
from .log_setup import logger
from .environment import PREFIX, TOKEN, ACTIVITY_NAME

"""
This bot is based on a template by nonchris
https://github.com/nonchris/discord-bot
"""

intents = discord.Intents.all()


# inspired by https://github.com/Rapptz/RoboDanny
# This function will be evaluated for each message
# you can define specific behaviours for different messages or guilds, like custom prefixes for a guild etc...
def _prefix_callable(_bot: commands.Bot, msg: discord.Message):

    user_id = _bot.user.id
    # way discord expresses mentions
    # mobile and desktop have a different syntax how mentions are sent, so we handle both
    prefixes = [f'<@!{user_id}> ', f'<@{user_id}> ']
    if msg.guild is None:  # we're in DMs, using default prefix
        prefixes.append(PREFIX)
        return prefixes

    # TODO: This would be the place to add guild specific custom prefixes
    # you've got the current message hence the guild-id which is perfect to store and load prefixes for a guild
    # just append them to base and only append the default prefix if there is no custom prefix for that guild

    prefixes.append(PREFIX)
    return prefixes


bot = commands.Bot(command_prefix=_prefix_callable, intents=intents)


# login message
@bot.event
async def on_ready():
    """!
    function called when the bot is ready. Emits the '[Bot] has connected' message
    """

    print()
    member_count = 0
    guild_string = ""
    for g in bot.guilds:
        guild_string += f"{g.name} - {g.id} - Members: {g.member_count}\n"
        member_count += g.member_count

    logger.info(f"Bot '{bot.user.name}' has connected, active on {len(bot.guilds)} guilds:\n{guild_string}")

    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name=ACTIVITY_NAME))

    # LOADING Extensions
    # this is done in on_ready() so that cogs can fetch data from discord when they're loaded
    bot.remove_command('help')  # unload default help message
    # TODO: Register your extensions here
    initial_extensions = [
        '.cogs.misc',
        '.cogs.help'
    ]

    for extension in initial_extensions:
        bot.load_extension(extension, package=__package__)


def start_bot(token=None):
    """ Start the bot, takes token, uses token from env if none is given """
    if token is not None:
        bot.run(token)
    if TOKEN is not None:
        bot.run(TOKEN)
    else:
        logger.error("No token was given! - Exiting")
