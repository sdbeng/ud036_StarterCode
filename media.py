import webbrowser


class Movie():
    """ This class creates a data structure that defines
    the methods to store movie properties """
    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ method to display movies trailer on a web browser """
        webbrowser.open(self.trailer_youtube_url)
