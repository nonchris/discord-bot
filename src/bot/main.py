#!/bin/env python

import discord
from discord.ext import commands

# setup of logging and env-vars
# logging must be initialized before environment, to enable logging in environment
from .log_setup import logger, formatter, console_logger
from .environment import PREFIX, TOKEN, ACTIVITY_NAME

"""
This bot is based on a template by nonchris
https://github.com/nonchris/discord-bot
"""


class MyBot(commands.Bot):
    """!
    Custom bot-class implementing useful defaults for loading cogs and pushing slash-commands
    This implementation is object-oriented.
    You can still overwrite / use the 'classic' decorator method like:

    @bot.event
    async def on_ready():
        ...

    """

    def __init__(self, intents: discord.Intents = discord.Intents.all()):
        """ Initialize bot with intents and init super """
        super().__init__(command_prefix=self._prefix_callable, intents=intents)

    async def setup_hook(self):
        """!
        A coroutine to be called to setup the bot, by default this is blank.
        This performs an asynchronous setup after the bot is logged in,
        but before it has connected to the Websocket (quoted from d.py docs)
        """

        # LOADING Extensions
        # this is done in on_ready() so that cogs can fetch data from discord when they're loaded
        bot.remove_command('help')  # unload default help message
        # TODO: Register your extensions here
        initial_extensions = [
            '.cogs.misc',
            '.cogs.help'
        ]

        for extension in initial_extensions:
            await bot.load_extension(extension, package=__package__)

    # login message
    async def on_ready(self):
        """!
        Function called when the bot is ready. Emits the '[Bot] has connected' message
        """

        # Walk all guilds, report connected guilds and push commands to guilds
        member_count = 0
        guild_string = ""
        for g in bot.guilds:
            guild_string += f"{g.name} - {g.id} - Members: {g.member_count}\n"
            member_count += g.member_count

            # PUSHING Commands
            # copy all commands to all guilds one after an other
            # this is inefficient, but a fast way to push new commands to all guilds
            await self.__sync_commands_to_guild(g)

        logger.info(f"\n---\n"
                    f"Bot '{bot.user.name}' has connected, active on {len(self.guilds)} guilds:\n{guild_string}"
                    f"---\n")

        # set the status of the bot
        await self.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name=ACTIVITY_NAME))

    async def on_guild_join(self, guild: discord.Guild):
        """!
        Function called when bot is invited onto a new server
        """
        logger.info(f"Bot joined guild: '{guild.name}'")
        # try to push slash commands to new server
        await self.__sync_commands_to_guild(guild)

    async def __sync_commands_to_guild(self, guild: discord.Guild):
        """!
        Function to push all commands to a guild
        Doing this for all guilds on startup is is inefficient, but a fast way to push new commands to all guilds
        """
        try:
            self.tree.copy_global_to(guild=guild)
            await bot.tree.sync(guild=guild)
            logger.info(f"Pushed commands to: {guild.name}")
        except discord.errors.Forbidden:
            logger.warning(f"Don't have the permissions to push slash commands to: '{guild.name}'")

    # inspired by https://github.com/Rapptz/RoboDanny
    # This function will be evaluated for each message
    # you can define specific behaviours for different messages or guilds, like custom prefixes for a guild etc...
    @staticmethod
    def _prefix_callable(_bot, msg: discord.Message):
        """!
        Function that evaluates whether a (chat)-command was triggered by a message
        Inspired by https://github.com/Rapptz/RoboDanny
        """
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


# Create instance of our bot
bot = MyBot()


# Entrypoint function called from __init__.py
def start_bot(token=None, log_handler=console_logger, log_formatter=formatter, root_logger=False):
    """ Start the bot, takes token, uses token from env if none is given """
    # TODO: Logs from d.py don't appear in the log file (note for the dev, not the template user)
    if token is not None:
        bot.run(token, log_handler=log_handler, log_formatter=log_formatter, root_logger=root_logger)
    if TOKEN is not None:
        bot.run(TOKEN, log_handler=log_handler, log_formatter=log_formatter, root_logger=root_logger)
    else:
        logger.error("No token was given! - Exiting")
