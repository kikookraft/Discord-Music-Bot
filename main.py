import os
import json
import random
import asyncio
import colorama

#discord
import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio

#multimedia
from youtube_dl import YoutubeDL
from pytube import YouTube
import validators
import pyttsx3
import logging
import colorama

#initialisations
colorama.init()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# discord
TOKEN = 'oops...'
client = commands.Bot(command_prefix='!')

class bcolors: #pour afficher en couleur dans la console
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
color = [bcolors.HEADER, bcolors.OKBLUE, bcolors.OKCYAN, bcolors.OKGREEN, bcolors.WARNING, bcolors.FAIL, bcolors.ENDC, bcolors.BOLD, bcolors.UNDERLINE]
async def print_color(txt, col):
    print(color[col] + str(txt) + bcolors.ENDC)
