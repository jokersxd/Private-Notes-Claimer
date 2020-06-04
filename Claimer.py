from colorama import Fore, init, Style
from discord.ext import commands
import pyPrivnote
import requests
import discord
import ctypes
import os

ctypes.windll.kernel32.SetConsoleTitleW('Private Notes Claimer | Developed by jokers')
client = commands.Bot(command_prefix='.', self_bot=True)
init(autoreset=True, convert=True)
client.remove_command('help')
os.system('cls')
token = ''

@client.event
async def on_connect():
    print(Fore.GREEN + '\n -- ' + Fore.WHITE + Style.BRIGHT + 'Ready')
    
@client.event
async def on_message(message):
    if 'https://privnotes.com/' in message.content:
        try:
            Code = message.content.split('https://privnotes.com/')[1]
            r = requests.get('https://privnotes.com/view-message/' + str(Code)).text
            if 'If you need to keep it, copy it before closing this window.' in r:
                Note = r.split('name="note_desc" id="i">')[1].split('<')[0]
                print(Fore.GREEN + '\n[SUCCESS] ' + Fore.WHITE + Style.BRIGHT + 'Grabbed note | Details:' + Fore.RED + '\n -- ' + Fore.WHITE + Style.BRIGHT + 'URL: ' + str(message.content) + Fore.RED + '\n -- ' + Fore.WHITE + Style.BRIGHT + 'Note deleted' + Fore.RED + '\n -- ' + Fore.WHITE + Style.BRIGHT + 'Content: ' + str(Note))
            else:
                if 'name="note_desc" id="i">' in r:
                    Note = r.split('name="note_desc" id="i">')[1].split('<')[0]
                    print(Fore.GREEN + '\n[SUCCESS] ' + Fore.WHITE + Style.BRIGHT + 'Grabbed note | Details:' + Fore.RED + '\n -- ' + Fore.WHITE + Style.BRIGHT + 'URL: ' + str(message.content) + Fore.RED + '\n -- ' + Fore.WHITE + Style.BRIGHT + 'Note deleted' + Fore.RED + '\n -- ' + Fore.WHITE + Style.BRIGHT + 'Content: ' + str(Note))
        except:
            pass

try:
    client.run(token, bot=False)
except Exception as e:
    print(' ')
    print(Fore.RED + '[ERROR] ' + Fore.WHITE + Style.BRIGHT + str(e))
    input()
    quit()
