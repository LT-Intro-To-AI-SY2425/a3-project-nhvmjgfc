from match import match
from music2 import music_db

def get_title(musicinfo):
    return musicinfo[0]

def get_artist(musicinfo):
    return musicinfo[1]

def get_genre(musicinfo):
    return musicinfo[2]

def get_length(musicinfo):
    return int(musicinfo[3])

def get_year(musicinfo):
    return int(musicinfo[4])


def title_by_year(matches):
    year = int(matches[0])

    result = filter(lambda songinfo: get_year(songinfo) == year, music_db)
    result = list(map(lambda songinfo : get_title(songinfo), result))
    return result


def title_by_year_range(matches):
    startYear = int(matches[0])
    endYear = int(matches[1])

    result = filter(lambda songinfo: get_year(songinfo) >= startYear and get_year(songinfo) <= endYear, music_db)
    result = list(map(lambda songinfo : get_title(songinfo), result))
    return result


def title_before_year(matches):
    year = int(matches[0])

    result = filter(lambda songinfo: get_year(songinfo) < year, music_db)
    result = list(map(lambda songinfo : get_title(songinfo), result))
    return result


def title_after_year(matches):
    year = int(matches[0])

    result = filter(lambda songinfo: get_year(songinfo) > year, music_db)
    result = list(map(lambda songinfo : get_title(songinfo), result))
    return result


def artist_by_title(matches):
    title = matches[0]

    return list(map(lambda songinfo: get_artist(songinfo), filter(lambda songinfo: get_title(songinfo) == title, music_db)))


def title_by_artist(matches):
    artist = matches[0]

    return list(map(lambda songinfo: get_title(songinfo), filter(lambda songinfo: get_artist(songinfo) == artist, music_db)))


def year_by_title(matches):
    title = matches[0]

    return list(map(lambda songinfo: get_year(songinfo), filter(lambda songinfo: get_title(songinfo) == title, music_db)))

pa_list = [
    (str.split("what songs were made in _"), title_by_year),
    (str.split("what songs were made between _ and _"), title_by_year_range),
    (str.split("what songs were made before _"), title_before_year),
    (str.split("what songs were made after _"), title_after_year),
    (str.split("who produced %"), artist_by_title),
    (str.split("who was the artist of %"), artist_by_title),
    (str.split("what songs were produced by %"), title_by_artist),
    (str.split("when was % made"), year_by_title)
]


def search_pa_list(src):
    for pa in pa_list:
        result = match(pa[0], src)
        if result:
            answers = pa[1](result)
            return answers if len(answers) > 0 else ["No answers"]

    return ["I don't understand"]


def query(input):
    answers = search_pa_list(input)
    for ans in answers:
        print(ans)