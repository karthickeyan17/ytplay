from .search import search
from .ui import display_results, ask_choice, clear_screen
from .player import play
from .cli import parse_args

def main():
    
    args = parse_args()

    if args.query:
        query = " ".join(args.query)
    else:
        query = input("Enter query: ")
    
    videos = search(query,args.results)
        
    clear_screen()

    display_results(query, videos)

    selection = ask_choice(videos)

    if selection:
        play(selection)

if __name__ == "__main__" :
    main()
