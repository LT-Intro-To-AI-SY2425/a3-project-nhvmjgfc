# Database for music Order is title, artist, genre, length in seconds, and year released.

from typing import List, Tuple

music_db: List[Tuple[str,str,str,int,int]]=[
    (
        "tengo motivos", #title
        "junior h", #artist
        "regional mexican", #genre
        187, #length
        2020, #year released
    ),
    (
        "paper soldier", 
        "brent faiyaz", 
        "r&b", 
        201,
        2021, 
    ),
    (
        "safe 2",
        "veeze",
        "rap",
        151,
        2023,
    ),
    (
        "desenfocao'",
        "rauw alejandro",
        "funk",
        170,
        2021,
    ),
    (
        "b.o.r. (birth of rap)",
        "lil b",
        "rap",
        233,
        2009,
    ),
    (
        "king for a day",
        "pierce the veil",
        "rock",
        236,
        2012,
    ),
    (
        "paint",
        "che",
        "rap",
        118,
        2024,
    ),
    (
        "go stupid",
        "polo g",
        "rap",
        165,
        2020,
    ),
    (
        "cherry waves",
        "deftones",
        "alt rock",
        317,
        2006,
    ),
    (
        "only if",
        "steve lacy",
        "alt r&b",
        100,
        2019,
    ),
    (
        "keep it cool",
        "rich amiri",
        "rap",
        106,
        2024,
    ),
    (
        "we fell in love in october",
        "girl in red",
        "alt/indie",
        184,
        2018,
    ),
    (
        "my gasoline",
        "maddix",
        "electronic dance",
        236,
        2023,
    ),
    (
        "see you again",
        "tyler the creator",
        "pop rap",
        180,
        2017,
    ),
    (
        "frozone",
        "homixide gang",
        "rap",
        166,
        2023,
    ),
    (
        "corazon sin cara",
        "prince royce",
        "bachata",
        211,
        2010,
    ),
    (
        "you should see me in a crown",
        "billie eilish",
        180,
        2019,
    ),
    (
        "when we ride",
        "chris travis",
        "hip hop",
        206,
        2012,
    ),
    (
        "freestyle 1",
        "ken carson",
        "rap",
        231,
        2022,
    ),
    (
        "tu es foutu",
        "conki",
        "house",
        124,
        2022,
    ),
]