import argparse

def parse_args():
    parser = argparse.ArgumentParser(
            prog="ytplay",
            description="search and play  Youtube videos using mpv",
            )
    parser.add_argument(
            "query",
            nargs="*",
            help = "search query",
            )
    parser.add_argument(
            "-n",
            "--results",
            type=int,
            default=10,
            help = "number of search result",
            )
    return parser.parse_args()

