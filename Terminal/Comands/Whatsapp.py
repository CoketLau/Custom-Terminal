import pywhatkit
import json
import pathlib
import os
import colorama
import sys

BASE_DIR = pathlib.Path(__file__).parent.parent

File_Path = BASE_DIR / "Data" / "Contacts.json"

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def ReadData():
    with open(File_Path, "r") as File:
        return json.load(File)

def ListUsers():
    Data = ReadData()
    print("Available contacts: ")
    for i in Data["Users"]:
        print(colorama.Fore.WHITE + i["Name"])

def SendMessage():
    Choise = input(colorama.Fore.MAGENTA +"Chose contact: ").strip().lower()
    if Choise == "b":
        return False
    Data = ReadData()
    for i in Data["Users"]:
        if Choise == i["Name"].lower():
            msg = input(colorama.Fore.MAGENTA +"Msg: ")
            pywhatkit.sendwhatmsg_instantly(i["Number"], msg)
            if os.path.exists("PyWhatKit_DB.txt"):
                os.remove("PyWhatKit_DB.txt")
            clear_console()
            print(f"Message sent to {i['Name']}!")
            return True
    print(colorama.Fore.RED + "No se encontró usuario")
    return False

def AddContact():
    Name = input(colorama.Fore.MAGENTA +"Name: ").strip().lower()
    CountryCode = f"+{input(colorama.Fore.MAGENTA +'Country code: ').strip()}"
    Number = f"{CountryCode}{input(colorama.Fore.MAGENTA +'Number: ').strip()}".replace(" ", "")
    Data = ReadData()
    Data["Users"].append({"Name": Name, "Number": Number})
    with open(File_Path, "w") as JsonFile:
        json.dump(Data, JsonFile, indent=4)
    print(f"User {Name} added successfully!")
    return True

def DeleteContact():
    Name = input(colorama.Fore.MAGENTA + "Name: ").strip().lower()
    Data = ReadData()
    for i in Data["Users"]:
        if i["Name"].lower() == Name:
            Data["Users"].remove(i)
            with open(File_Path, "w") as JsonFile:
                json.dump(Data, JsonFile, indent=4)
            print(f"User {Name} deleted.")
            return True
    print(colorama.Fore.RED +"No user found")
    return False

def Help():
    Text = (colorama.Fore.YELLOW + """
            
-Type "List" or "L" to see all contacts
-Type "Msg" or "M" to send a WhatsApp message
-Type "Add" or "A" to add a new contact
-Type "Delete" or "D" to remove a contact
-Type "Back" or "B" to return to the previous menu
-Type "Help" or "H" to get information about other commands
            
            """)
    
    print(Text)
    

def Start():
    Done = False
    print(colorama.Fore.CYAN + colorama.Style.BRIGHT + 'Use the command "H" for help using the Whatsapp tab commands')
    while True:
        if Done == True:
            break
        Choise = input(colorama.Fore.MAGENTA + "List / Msg / Add / Delete / Back: ").strip().lower()
        if Choise in ["msg", "m"]:
            Done = SendMessage()
        elif Choise in ["list", "l"]:
            ListUsers()
        elif Choise in ["add", "a"]:
            Done = AddContact()
        elif Choise in ["delete", "d"]:
            Done = DeleteContact()
        elif Choise in ["back", "b"]:
            Done = True
        elif Choise in ["h", "help"]:
            Help()
        else:

            print(colorama.Fore.RED + "Choose a valid option please")
