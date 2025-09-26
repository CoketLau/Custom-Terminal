from googletrans import Translator
import colorama

lang_map = {
    "spanish": "es",
    "english": "en",
    "french": "fr",
    "german": "de",
    "russian": "ru",
    "mandarin": "zh-cn"
}

async def Translate():
    while True:
        text = input(colorama.Fore.GREEN + "Translate: ")
        to_lang = input(colorama.Fore.GREEN + "To Spanish / English / French / German / Russian / Mandarin: ").lower()
        
        if to_lang in lang_map:
            lang_code = lang_map[to_lang]

            translator = Translator()
            translation = await translator.translate(text, dest=lang_code)  # <--- await here
            print(colorama.Fore.CYAN + f"Translation in {to_lang.capitalize()}: {translation.text}\n")
            break
        else:
            print(colorama.Fore.RED + "Please choose a valid option")