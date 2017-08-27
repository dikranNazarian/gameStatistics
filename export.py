from reports import count_games
from reports import decide
from reports import get_latest
from reports import count_by_genre
from reports import get_line_number_by_title
from reports import sort_abc
from reports import get_genres
from reports import when_was_top_sold_fps


def export_to_file(file_name="export.txt"):
    answers = []
    answers.append(count_games())
    answers.append(decide("game_stat.txt", 1998))
    answers.append(get_latest())
    answers.append(count_by_genre())
    answers.append(get_line_number_by_title())
    answers.append(sort_abc())
    answers.append(get_genres())
    answers.append(when_was_top_sold_fps())
    with open(file_name, "w") as file_export:
        for i in answers:
            i = str(i)
            file_export.write(i)
            file_export.write("\n")


def main():
    export_to_file()

main()