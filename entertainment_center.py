import os
import media
import fresh_tomatoes

# print os.getcwd()
curr_directory = os.getcwd()

# Instances of class Movie
thor_ragnarok = media.Movie("Thor:Ragnarok","MCU1",
                            curr_directory + "\Thor_Ragnarok_poster.jpg",
                            "https://www.youtube.com/watch?v=ue80QwXMRHg")

civil_war = media.Movie("Civil War","MCU2",
                        curr_directory + "\Captain_America_Civil_War_poster.jpg",
                        "https://www.youtube.com/watch?v=dKrVegVI0Us")

infinity_war = media.Movie("Avengers: Infinity War","MCU3",
                           curr_directory + "\download.jpg",
                           "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

black_panther = media.Movie("Black Panther","MCU4",
                            curr_directory + "\Black_Panther_film_poster.jpg",
			    "https://www.youtube.com/watch?v=xjDjIWPwcPU")

spiderman = media.Movie("Spider-Man: Homecoming","MCU5",
                        curr_directory + "\Spider-Man_Homecoming_poster.jpg",
                        "https://www.youtube.com/watch?v=U0D3AOldjMU")

iron_man = media.Movie("IronMan 3", "MCU6",
                       curr_directory + "\Iron_Man_3_theatrical_poster.jpg",
                       "https://www.youtube.com/watch?v=2CzoSeClcw0")
    
# List of movies 
movies = [iron_man, civil_war, spiderman, thor_ragnarok,
          black_panther, infinity_war]


fresh_tomatoes.open_movies_page(movies)
