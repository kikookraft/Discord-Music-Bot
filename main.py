import os
import json
import random
import asyncio

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
from colorama import init