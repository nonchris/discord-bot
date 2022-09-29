from .main import start_bot
from .version import VERSION

# this version will be read by setup.py and the bot itself
__version__ = VERSION


def main():
    start_bot()
