import webbrowser

#make a class that creates space for inputting movie information


class Movie():
    #create movie information parameters inside class's initialized space
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #create object that uses the open() function to play the movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
