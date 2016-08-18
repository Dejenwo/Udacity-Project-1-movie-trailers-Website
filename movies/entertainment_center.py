import media
import fresh_tomatoes

"""
declare favorite movies, with 4 args each:
title (movie's title)
story (short story of movie)
poster_url (url to poster image)
trailer_url (url to youtube trailer)
"""
mechanic = media.Movie(
    "Mechanic",
    "Mechanic in the sequel to the 2011 action thriller",
    "https://upload.wikimedia.org/wikipedia/en/4/40/Mechanic_Resurrection_poster.jpg",
    "https://youtu.be/QF903RaKLvs")
ouija = media.Movie(
    "Ouija",
    "Origin of Evil Official Trailer",
    "https://upload.wikimedia.org/wikipedia/en/9/9b/Ouija_two_xxlg.jpeg",
    "https://youtu.be/H-eSWIZkAH8")
moana = media.Movie(
    "Moana",
    "3D computer-animated musical fantasy comedy adventure",
    "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",
    "https://www.youtube.com/watch?v=M5dnZKrUpdA")
sing = media.Movie(
    "Sing",
    "3D computer-animated musical comedy",
    "https://upload.wikimedia.org/wikipedia/en/b/bb/Sing_%282016_film%29_poster.jpg",
    "https://www.youtube.com/watch?v=Y7uGHY-t80I")
the_gift = media.Movie(
    "The Gift",
    "American-Australian psychological thriller film  ",
    "https://upload.wikimedia.org/wikipedia/en/9/97/The_Gift_2015_Film_Poster1.png",
    "https://www.youtube.com/watch?v=I3IiZU9JBuE")
nerve = media.Movie(
    "Nerve",
    "American crime techno-thriller survival film",
    "https://upload.wikimedia.org/wikipedia/en/e/e2/Nerve_2016_poster.jpg",
    "https://www.youtube.com/watch?v=zOJYRjALUqI")


# assign individual movies to movies array
movies = [mechanic,ouija,moana,sing,the_gift,nerve]

# call movie trailer page method and pass movies array and sorting option
fresh_tomatoes.open_movies_page(movies)
