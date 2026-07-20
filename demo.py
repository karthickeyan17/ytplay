from search import search
from ui import display_results, ask_choice, clear_screen

query = input("Search: ")

videos = search(query)

clear_screen()

display_results(query, videos)

choice = ask_choice(len(videos))

print(choice)
