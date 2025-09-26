import os
import colorama

Commands = ["flushdns", "del /q /f /s %TEMP%\*", "ie4uinit.exe -show"]

def Reload():
    print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "Reloading...")

    for i in Commands:
        os.system(i)
    
    os.system("cls")
    print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "Finished reload.")