import discord
from discord.ext import commands
from discord.ext import tasks

from ..log_setup import logger
from ..utils import utils as ut


### @package misc
#
# Collection of miscellaneous helpers.
#

class Misc(commands.Cog):
    """
    Various useful Commands for everyone
    """

    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command(name='ping', help="Check if Bot available")
    async def ping(self, ctx):
        """!
        ping to check if the bot is available

        @param ctx Context of the message
        """
        logger.info(f"ping: {round(self.bot.latency * 1000)}")

        await ctx.send(
            embed=ut.make_embed(
                name='Bot is available',
                value=f'`{round(self.bot.latency * 1000)}ms`')
        )

    # Example for an event listener
    # This one will be called on each message the bot recieves
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        pass

    # Example for a task
    # It can be started using self.my_task.start() e.g. from this cogs __init__
    @tasks.loop(seconds=60)
    async def my_task(self):
        pass

def setup(bot):
    bot.add_cog(Misc(bot))
