import media
import fresh_tomatoes

# Iron Man movie: title, storyline, image and trailer 
iron_man = media.Movie(
    "Iron Man",
    "A Genius engineer got to build a robot from metal scraps",
    "http://www.gstatic.com/tv/thumb/movieposters/170620/p170620_p_v8_ax.jpg",  # NOQA
    "https://www.youtube.com/watch?v=LWbjrFCecPY")

# Rambo movie: title, storyline, image and trailer
rambo = media.Movie(
    "Rambo",
    "A Vietnam Veteran back home",
    "http://www.gstatic.com/tv/thumb/movieposters/6343/p6343_p_v8_aj.jpg",  # NOQA
    "https://www.youtube.com/watch?v=YMGdRUSJwq0")

# Terminator movie: title, storyline, image and trailer
terminator = media.Movie(
    "Terminator",
    "Present robotics",
    "https://vignette.wikia.nocookie.net/terminator/images/c/ca/Terminator_poster.jpg/revision/latest?cb=20110513152209",  # NOQA
    "https://www.youtube.com/watch?v=fratdVlBiOM")

# Fury movie: title, storyline, image and trailer
fury = media.Movie(
    "Fury",
    "Sherman ride",
    "https://upload.wikimedia.org/wikipedia/en/thumb/1/17/Fury_2014_poster.jpg/220px-Fury_2014_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=SKu5lGfRBxc")

# Private Ryan movie: title, storyline, image and trailer
private_ryan = media.Movie(
    "Saving Private Ryan",
    "Normandy landing",
    "https://scriptslug.com/assets/uploads/posters/_540xAUTO_crop_center-center_75_none/saving-private-ryan-1998.jpg",  # NOQA
    "https://www.youtube.com/watch?v=RYID71hYHzg")

# Stars Wars movie: title, storyline, image and trailer
stars_wars = media.Movie(
    "Stars Wars - The Force Awakens",
    "Falcon at its best",
    "https://vignette.wikia.nocookie.net/starwars/images/f/fd/Star_Wars_Episode_VII_The_Force_Awakens.jpg/revision/latest?cb=20151018162823",  # NOQA
    "https://www.youtube.com/watch?v=OMOVFvcNfvE")

# create a list to hold all the movie instances
movies = [iron_man, rambo, terminator, fury, private_ryan, stars_wars]

# call open_movies_page method on fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
