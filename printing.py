from reports import count_games
from reports import decide
from reports import get_latest
from reports import count_by_genre
from reports import get_line_number_by_title
from reports import sort_abc
from reports import get_genres
from reports import when_was_top_sold_fps


def main():
    print(count_games())
    print(decide("game_stat.txt", 2004))
    print(get_latest())
    print(count_by_genre())
    print(get_line_number_by_title())
    print(sort_abc())
    print(get_genres())
    print(when_was_top_sold_fps())
main()