# discord-bot-template
Generic, functional bot based on discord.py V2.    
Including:
- general bot setup, saving your time
  - overwritten behaviour in `on_ready()`, `setup_hook()` and `on_guild_join()`  
  - cog-structure

- commands
  - ping-commands for slash- and chat-usage as demonstration
  - a custom help command for old-style chat-command as examples
  - old-style reacts to prefix and mention

- logging setup for console and file
- utils for easy embed creation, id-extraction and more
- easy to use external configuration using json or env-variables
- overall project structure for easy packaging and deployment

This template is aimed at beginners ([how to start](#I'm-new-to-bots---where-to-start?)) for learning purposes and 
advanced users for 
saving time.


## Setup

###### Setup a [venv](https://docs.python.org/3/library/venv.html) (optional, but recommend)
`python3 -m venv venv`   
`source venv/bin/activate` 


##### Using pip to install the bot as editable package:  
` python3 -m pip install -e .`  
`export TOKEN="your-key"`  
`discord-bot`  
##### Or using the launch script:  
`pip install -r requirements.txt`  
`export TOKEN="your-key"`   
`python3 ~/git/discord-bot/launcher.py`  

### Intents
The bot uses all intents by default, those are required for such simple things like 'display member-count at startup'.  
You need to enable those intents in the [discord developers portal](https://discord.com/developers/applications) 
under `*YourApplication*/Bot/Privileged Gateway Intents`.   
It's possible reconfigure the requested intents in `main.py` if you don't need them.  
But I'd suggest using them all for the beginning, especially if you're relatively new to discord.py.  
This will only be an issue if your bot reaches more than 100 servers, then you've got to apply for those intents. 

#### Optional env variables
| parameter |  description |
| ------ |  ------ |
| `PREFIX="b!"`  | Command prefix |
| `OWNER_NAME="unknwon"` | Name of the bot owner |
| `OWNER_ID="100000000000000000"` | ID of the bot owner |
| `ACTIVITY_NAME=f"{PREFIX}help"`| Activity bot plays |  

The shown values are the default values that will be loaded if nothing else is specified.  
Expressions like `{PREFIX}` will be replaced by during loading the variable and can be used in specified env variables.

Set those variables using env-variables (suggested):  
`export PREFIX="b!"`  
Or use a json-file expected at: `./data/config.json` like:  
```json
{
  "TOKEN": "[your-token]",
  "PREFIX": "b!"
}
```

_If a variable is set using env and json **the environment-variable replaces the json**!_


# I'm new to bots - where to start?
Have a look at `src/discord_bot/cogs/misc.py` this is a good place to start with your first smaller functions.  
You'll find some basic examples there.  
Try to modify the `ping`-command or start with a small listener (`on_message`) that responds to each message the bot receives.  
Or write a slash command that sends the date the [member joined the server](https://discordpy.readthedocs.io/en/latest/api.html?highlight=joined#discord.Member.joined_at).  

You can expand to yor own, new modules when you feel ready for it :)  
The official docs for discord.py are [here](https://discordpy.readthedocs.io/en/latest/api.html?highlight=guild#api-reference).  
There are also very well documented [examples in the official repository](https://github.com/Rapptz/discord.py/tree/master/examples).

### about
This repository contains code that was written by me across various bot-projects, like:  
https://github.com/nonchris/discord-fury  
https://github.com/nonchris/quiz-bot  
https://github.com/Info-Bonn/verification-listener  
https://github.com/nonchris/discord-role-selection/tree/main/src/bot

I collected the most useful and generic functions to save me some time when starting the next bot-project.

### documentation
In order to render this documentation, just call `doxygen`
