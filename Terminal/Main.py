from Comands import Whatsapp, Google, Gpt, Translate, Reload
import colorama
import os
import asyncio
import shutil
import pathlib

colorama.init(autoreset=True)
os.system("cls")
if pathlib.Path("Consola\Comandos\__pycache__").exists():
    shutil.rmtree("Consola\Comandos\__pycache__")

print(colorama.Fore.CYAN + colorama.Style.BRIGHT + 'Use "H" to get useful information about the terminal commands.')

HelpText = (
    colorama.Fore.YELLOW + "- Use \"W\" to use all WHATSAPP related commands.\n"
    "- Use \"H\" to get HELP about the terminal commands.\n"
    "- Use \"S\" to SEARCH any topic on Google, will return a link.\n"
    "- Use \"G\" to use CHATGPT. \n"
    "- Use \"C\" to CLEAR the terminal. \n"
    "- Use \"T\" to TRANSLATE any text. \n"
    "- Use \"R\" to RELOAD, meaning automaticly making your computer faster \n"
)

while True:
    Command = input(colorama.Fore.GREEN + ">>> ").strip().lower()

    if Command == "w":
        Whatsapp.Start()
    elif Command == "s":
        Google.Search()
    elif Command == "g":
        Gpt.Ask()
    elif Command == "t":
        asyncio.run(Translate.Translate())
    elif Command == "r":
        Reload.Reload()
    elif Command == "c":
        os.system("cls" if os.name == "nt" else "clear")
    elif Command == "h":
        print(HelpText)
    else:
        os.system(Command)
