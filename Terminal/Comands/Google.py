import serpapi
import colorama

colorama.init(autoreset=True)

key = "c1e649ca3ac26cfa71c0c20c41fff1ad781fcf036c99719815601cc65682c4a5"

def Search():
    query = input(colorama.Fore.MAGENTA + "Search: ").strip()
    
    params = {
        "q": query,
        "api_key": key,
        "engine": "google"  # mandatory to specify search engine
    }
    
    search = serpapi.search(params)
    results = search.as_dict()  # <-- use as_dict() here
    
    if "organic_results" in results and len(results["organic_results"]) > 0:
        print(colorama.Fore.CYAN + "Top result:")
        print(colorama.Fore.WHITE + results["organic_results"][0]["link"])
    else:
        print(colorama.Fore.RED + "No results found.")

if __name__ == "__main__":
    Search()
