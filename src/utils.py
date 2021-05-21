import re

import discord
from discord.errors import Forbidden

# color scheme for embeds as rbg
blue_light = (20, 255, 255)  # default color
yellow = (245, 218, 17)  # waring like 'hey, that's not cool'
orange = (245, 139, 17)  # waring - rather critical like 'no more votes left'


async def send_embed(ctx, embed):
    """
    Handles the sending of embeds
    -> Takes context and embed to send
    - tries to send embed in channel
    - tries to send normal message when that fails
    - tries to send embed private with information abot missing permissions
    If this all fails: https://youtu.be/dQw4w9WgXcQ
    """
    try:
        await ctx.send(embed=embed)
    except Forbidden:
        try:
            await ctx.send("Hey, seems like I can't send embeds. Please check my permissions :)")
        except Forbidden:
            await ctx.author.send(
                f"Hey, seems like I can't send any message in {ctx.channel.name} on {ctx.guild.name}\n"
                f"May you inform the server team about this issue? :slight_smile:", embed=embed)


# creating and returning an embed with keyword arguments
# please note that name and value can't be empty - name and value contain a zero width non-joiner
def make_embed(title="", color=blue_light, name="‌", value="‌", footer=None) -> discord.Embed:
    """
    Function to generate generate an embed in one function call

    :param title: Headline of embed
    :param color: RGB Tuple (Red, Green, Blue)
    :param name: Of field (sub-headline)
    :param value: Text of field (actual text)
    :param footer: Text in footer
    :return: Embed ready to send
    """
    # make color object
    color = discord.Color.from_rgb(*color)  # * unwraps the elements in the tuple
    emb = discord.Embed(title=title, color=color)
    emb.add_field(name=name, value=value)
    if footer:
        emb.set_footer(text=footer)

    return emb
