from search import search
from ui import display_results, ask_choice, clear_screen
from player import play

query = input("Search: ")

videos = search(query)

clear_screen()

display_results(query, videos)

selection = ask_choice(videos)

if selection:
    play(selection)
