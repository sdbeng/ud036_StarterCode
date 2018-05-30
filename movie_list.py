import movie_factory
import fresh_tomatoes

iron_man = movie_factory.Movie("Iron Man",
 "A Genius engineer got to build a robot from metal scraps", "http://www.gstatic.com/tv/thumb/movieposters/170620/p170620_p_v8_ax.jpg",
  "https://www.youtube.com/watch?v=LWbjrFCecPY")

print(iron_man.storyline)

nuclear_man = movie_factory.Movie("Nuclear Man",
 "A pilot gets a new bionic arm and leg", "https://upload.wikimedia.org/wikipedia/en/b/b7/Sixmilliondollar1.jpg",
  "https://www.youtube.com/watch?v=IFhEN8PcgVE")

terminator = movie_factory.Movie("Terminator",
 "Present robotics", "http://t1.gstatic.com/images?q=tbn:ANd9GcRHzSaUCOKu1RwS-bfbaUeeo_I1JcBkiuJRjBElvJi7qsHXkUkJ",
  "https://www.youtube.com/watch?v=fratdVlBiOM")

fury = movie_factory.Movie("Fury",
 "Sherman ride", "http://t2.gstatic.com/images?q=tbn:ANd9GcR_ppNO9FR1hT0mRhqD1lWovgQZMwxJRhYrEa7vYmTb-atN1Opu",
  "https://www.youtube.com/watch?v=SKu5lGfRBxc")

private_ryan = movie_factory.Movie("Saving Private Ryan",
 "Normandy landing", "http://t2.gstatic.com/images?q=tbn:ANd9GcR0lDhR_dXAKTm9wysp3nWu6kP0V5skJBVbCNC_Q8urAWcr4iF_",
  "https://www.youtube.com/watch?v=RYID71hYHzg")

stars_wars = movie_factory.Movie("Stars Wars - The Force Awakens",
 "Falcon at its best", "http://t0.gstatic.com/images?q=tbn:ANd9GcT6nGxj1D4P-9EiVSY32sb6Ql-XQrbeK5FgM37UI6QxcZwfcfVw",
  "https://www.youtube.com/watch?v=OMOVFvcNfvE")

movies = [iron_man, nuclear_man, terminator, fury, private_ryan, stars_wars]
# fresh_tomatoes.open_movies_page(movies)