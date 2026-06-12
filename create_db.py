import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS movies")
cursor.execute("""
CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    name TEXT,
    year INTEGER,
    rating REAL,
    genre TEXT
)
""")

movies = [
    (1, "Inception", 2010, 4.8, "Sci-Fi"),
    (2, "Interstellar", 2014, 4.7, "Sci-Fi"),
    (3, "Titanic", 1997, 4.5, "Romance"),
    (4, "The Dark Knight", 2008, 4.9, "Action"),
    (5, "Avengers: Endgame", 2019, 4.6, "Action"),
    (6, "Avatar", 2009, 4.4, "Sci-Fi"),
    (7, "The Matrix", 1999, 4.7, "Sci-Fi"),
    (8, "Gladiator", 2000, 4.6, "Action"),
    (9, "Forrest Gump", 1994, 4.8, "Drama"),
    (10, "The Shawshank Redemption", 1994, 4.9, "Drama"),

    (11, "Fight Club", 1999, 4.8, "Drama"),
    (12, "Pulp Fiction", 1994, 4.7, "Crime"),
    (13, "The Godfather", 1972, 5.0, "Crime"),
    (14, "The Godfather Part II", 1974, 4.9, "Crime"),
    (15, "The Dark Knight Rises", 2012, 4.5, "Action"),
    (16, "Django Unchained", 2012, 4.6, "Western"),
    (17, "The Lord of the Rings: Fellowship of the Ring", 2001, 4.9, "Fantasy"),
    (18, "The Lord of the Rings: Two Towers", 2002, 4.8, "Fantasy"),
    (19, "The Lord of the Rings: Return of the King", 2003, 4.9, "Fantasy"),
    (20, "Harry Potter and the Sorcerer's Stone", 2001, 4.3, "Fantasy"),

    (21, "Harry Potter and the Deathly Hallows", 2011, 4.5, "Fantasy"),
    (22, "Jurassic Park", 1993, 4.6, "Adventure"),
    (23, "The Lion King", 1994, 4.7, "Animation"),
    (24, "Toy Story", 1995, 4.6, "Animation"),
    (25, "Toy Story 3", 2010, 4.7, "Animation"),
    (26, "Finding Nemo", 2003, 4.5, "Animation"),
    (27, "Shrek", 2001, 4.4, "Comedy"),
    (28, "Shrek 2", 2004, 4.3, "Comedy"),
    (29, "Frozen", 2013, 5, "Animation"),
    (30, "Coco", 2017, 4.6, "Animation"),

    (31, "Inside Out", 2015, 4.5, "Animation"),
    (32, "Black Panther", 2018, 4.5, "Action"),
    (33, "Iron Man", 2008, 4.6, "Action"),
    (34, "Spider-Man: No Way Home", 2021, 4.7, "Action"),
    (35, "Doctor Strange", 2016, 4.3, "Fantasy"),
    (36, "Joker", 2019, 4.6, "Drama"),
    (37, "The Batman", 2022, 4.5, "Action"),
    (38, "Mad Max: Fury Road", 2015, 4.7, "Action"),
    (39, "The Wolf of Wall Street", 2013, 4.6, "Crime"),
    (40, "Good Will Hunting", 1997, 4.7, "Drama"),

    (41, "The Social Network", 2010, 4.4, "Drama"),
    (42, "The Prestige", 2006, 4.6, "Mystery"),
    (43, "The Truman Show", 1998, 4.5, "Drama"),
    (44, "Se7en", 1995, 4.7, "Thriller"),
    (45, "Fight Club", 1999, 4.8, "Psychological"),
    (46, "The Avengers", 2012, 4.5, "Action"),
    (47, "Guardians of the Galaxy", 2014, 4.4, "Sci-Fi"),
    (48, "Deadpool", 2016, 4.3, "Comedy"),
    (49, "John Wick", 2014, 4.6, "Action"),
    (50, "The Revenant", 2015, 5, "Adventure"),
]


cursor.executemany(
    "INSERT INTO movies (id, name, year, rating, genre) VALUES (?, ?, ?, ?, ?)",
    movies
)

conn.commit()
conn.close()

print("Database created!")