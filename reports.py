def count_games(file_name="game_stat.txt"):
    with open(file_name, "r") as game_stat:
        file_read = game_stat.readlines()
        number_of_games = len(file_read)
    return number_of_games


def decide(file_name="game_stat.txt", year=0):
    year = str(year)
    with open(file_name, "r") as game_stat:
        file_read = game_stat.readlines()
        for tab in file_read:
            tab = tab.split()
            if year in tab:
                return True
        return False


def get_latest(file_name="game_stat.txt"):
    file_read = []
    games_dictionary = {}
    with open(file_name, "r") as game_stat:
        for line in game_stat:
            file_read.append(line)
    for tab in file_read:
        tab = tab.replace("\n", "")
        tab = tab.split("\t")
        games_dictionary[tab[0]] = tab[1:]
    search_for_lastest_year = 0
    for tab in games_dictionary:
        take_year_from_list = games_dictionary.get(tab)
        take_year_from_list = int(take_year_from_list[1])
        if take_year_from_list > search_for_lastest_year:
            search_for_lastest_year = take_year_from_list
            lastest_game_title = tab
    return lastest_game_title


def count_by_genre(file_name="game_stat.txt", genre="RPG"):
    file_read = []
    games_dictionary = {}
    with open(file_name, "r") as game_stat:
        for line in game_stat:
            file_read.append(line)
    for number in file_read:
        number = number.replace("\n", "")
        number = number.split("\t")
        games_dictionary[number[0]] = number[1:]
    count_games_by_genre = 0
    for number in games_dictionary:
        take_genre_from_list = games_dictionary.get(number)
        take_genre_from_list = take_genre_from_list[2]
        if take_genre_from_list == genre:
            count_games_by_genre += 1
    return count_games_by_genre


def get_line_number_by_title(file_name="game_stat.txt", title="Terraria"):
    line_number = 0
    with open(file_name, "r") as game_stat:
        for line in game_stat.readlines():
            line_number += 1
            if title in line:
                return line_number
    raise ValueError


def sort_abc(file_name="game_stat.txt"):
    file_read = []
    games_dictionary = {}
    with open(file_name, "r") as game_stat:
        for line in game_stat:
            file_read.append(line)
    for tab in file_read:
        tab = tab.replace("\n", "")
        tab = tab.split("\t")
        games_dictionary[tab[0]] = tab[1:]
    game_titles = games_dictionary.keys()
    game_titles = sorted(game_titles)
    return game_titles

def get_genres(file_name="game_stat.txt"):
    file_read = []
    games_dictionary = {}
    with open(file_name, "r") as game_stat:
        for line in game_stat:
            file_read.append(line)
    for tab in file_read:
        tab = tab.replace("\n", "")
        tab = tab.split("\t")
        games_dictionary[tab[0]] = tab[1:]
    genre_list = []
    for tab in games_dictionary:
        take_genre_from_list = games_dictionary.get(tab )
        take_genre_from_list = take_genre_from_list[2]
        if take_genre_from_list not in genre_list:
            genre_list.append(take_genre_from_list)
    genre_list = sorted(genre_list, key=str.lower)
    return genre_list


def when_was_top_sold_fps(file_name="game_stat.txt"):
    file_read = []
    games_dictionary = {}
    with open(file_name, "r") as game_stat:
        for line in game_stat:
            file_read.append(line)
    for tab in file_read:
        tab = tab.replace("\n", "")
        tab = tab.split("\t")
        games_dictionary[tab[0]] = tab[1:]
    fps_list = {}
    for tab in games_dictionary:
        take_genre_from_list = games_dictionary.get(tab)
        take_genre_from_list = take_genre_from_list[2]
        if take_genre_from_list == "First-person shooter":
            fps_list[tab] = games_dictionary.get(tab)
    top_sells = 0
    for tab in fps_list:
        take_sells_from_list = fps_list.get(tab)
        take_sells_from_list = float(take_sells_from_list[0])
        if top_sells < take_sells_from_list:
            top_sells = take_sells_from_list
            year = fps_list.get(tab)
            year = int(year[1])
    return year
    

def main():
    count_games()
    decide()
    get_latest()
    count_by_genre()
    get_line_number_by_title()
    sort_abc()
    get_genres()
    when_was_top_sold_fps()
main()