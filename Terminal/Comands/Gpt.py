from gpt4all import GPT4All
from pathlib import Path
import colorama

colorama.init(autoreset=True)
system_prompt = "respont to the promts asked in english, max 200 caracters: "

BASE_DIR = Path(__file__).parent.parent

MODEL_PATH = BASE_DIR / "Data" / "LlamaModel.gguf"

model = GPT4All(str(MODEL_PATH), n_threads=8)

def Ask():
    print(colorama.Fore.YELLOW + "Type \"Back\" or \"B\" to stop the conversation")

    while True:
        prompt = input(colorama.Fore.MAGENTA + "Ask gpt: ").lower()
        
        if prompt in ["back", "b"]:
            break
        else:
            print(colorama.Fore.GREEN + "Thinking..."
                "")
            response = model.generate((system_prompt + prompt), max_tokens= 200)
            print(colorama.Fore.WHITE + response)