import webbrowser


class Movie():
    """ Movie class contains following attributes:
    Attributes:
        title (str): Movie title
        storyline (str): Movies storyline
        poster_image_url (str): Link to the poster image of Movie
        trailer_youtube_url (str): Link to the youtube trailer
    """
    def __init__(self,movie_title,movie_storyline,
                 poster_image,trailer_youtube):  
        # instance variables
        self.title = movie_title 
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):  # instance method
        webbrowser.open(self.trailer_youtube_url)

print Movie.__doc__

        

        

