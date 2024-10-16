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
]