import sys

if __package__ is None and not hasattr(sys, "frozen"):
    import os.path

    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))

from discord_bot.main import start_bot
from discord_bot.version import VERSION

# this version will be read by setup.py and the bot itself
__version__ = VERSION


def main():
    start_bot()


if __name__ == "__main__":
    main()
