import media
import fresh_tomatoes

# create several Movie class instances
iron_man = media.Movie(
    "Iron Man",
    "A Genius engineer got to build a robot from metal scraps",
    "http://www.gstatic.com/tv/thumb/movieposters/170620/p170620_p_v8_ax.jpg",
    "https://www.youtube.com/watch?v=LWbjrFCecPY")
# test print
# print(iron_man.storyline)
rambo = media.Movie(
    "Rambo",
    "A Vietnam Veteran back home",
    "http://www.gstatic.com/tv/thumb/movieposters/6343/p6343_p_v8_aj.jpg",
    "https://www.youtube.com/watch?v=YMGdRUSJwq0")

terminator = media.Movie(
    "Terminator",
    "Present robotics",
    "https://ibb.co/dCeKAy",
    "https://www.youtube.com/watch?v=fratdVlBiOM")

fury = media.Movie(
    "Fury",
    "Sherman ride",
    "https://ibb.co/igsZcd",
    "https://www.youtube.com/watch?v=SKu5lGfRBxc")

private_ryan = media.Movie(
    "Saving Private Ryan",
    "Normandy landing",
    "https://ibb.co/gys0Hd",
    "https://www.youtube.com/watch?v=RYID71hYHzg")

stars_wars = media.Movie(
    "Stars Wars - The Force Awakens",
    "Falcon at its best",
    "https://ibb.co/fyEmqy",
    "https://www.youtube.com/watch?v=OMOVFvcNfvE")
# print(stars_wars.title)

# create a list to hold all the movie instances
movies = [iron_man, rambo, terminator, fury, private_ryan, stars_wars]

# call open_movies_page method on fresh_tomatoes
# then generate a valid html file by passing a list of movies
fresh_tomatoes.open_movies_page(movies)
