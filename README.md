# discord-bot-template
Generic, functional bot based on discord.py  
Including logging configuration, some utils and a general bot setup

## setup
`pip install -r requirements.txt`  
`export TOKEN="your-key"`  
`python3 main.py`  
_Remember using a virtual environment!_

## features
This bot does 'nothing' but is completely functional!  
_What is does:_  
* setup logging
* overwrite `on_ready()` function for information at startup
* register example cog with `b!ping` command
* util function for easy embed creation

## about
This repository contains code that was written by me across various bot-projects, like:
https://github.com/nonchris/discord-fury
https://github.com/Info-Bonn/poll-bot

I collected the most useful and generic functions to save me some time when starting the next bot-project. 

### dependencies 
This project is based on `discord.py V1.x` minimum required: V1.5.1