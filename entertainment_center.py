import fresh_tomatoes
import media

#create movie objects; these are instances of the class Movie()
castle_in_the_sky = media.Movie("Castle In the Sky",
                                "Whimsical, artistic brilliance from the master of animation, Hayao Miyazaki",
                                "https://upload.wikimedia.org/wikipedia/en/4/40/Castle_in_the_Sky_%28Movie_Poster%29.jpg",
                                "https://www.youtube.com/watch?v=McM0_YHDm5A")

passion_of_the_christ = media.Movie("Passion of the Christ",
                                    "Hope for Adam's race",
                                    "https://upload.wikimedia.org/wikipedia/en/6/61/Thepassionposterface-1-.jpg",
                                    "https://www.youtube.com/watch?v=4Aif1qEB_JU")

dunkirk = media.Movie("Dunkirk",
                      "The evacuation of English armed forces at Dunkirk",
                      "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU")
                      
return_of_the_king = media.Movie("Lord of the Rings: Return of the King",
                                 "The final installment in the epic trilogy",
                                 "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
                                 "https://www.youtube.com/watch?v=WIrRJ8bCZYQ")

equilibrium = media.Movie("Equilibrium",
                          "Thought-provoking, dystopian fiction",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/f/f6/Equilibriumposter.jpg/220px-Equilibriumposter.jpg",
                          "https://www.youtube.com/watch?v=raleKODYeg0")

secondhand_lions = media.Movie("Secondhand Lions",
                               "A hilarious adventure with emotional depth",
                               "https://upload.wikimedia.org/wikipedia/en/thumb/6/6a/SecondhandLions.jpg/220px-SecondhandLions.jpg",
                               "https://www.youtube.com/watch?v=Ebkrm7u44UI")

#create object containing the above instances of Movie(), to be used in fresh_tomatoes.py to construct the visual elements of the website
movies = [castle_in_the_sky, passion_of_the_christ, dunkirk, return_of_the_king, equilibrium, secondhand_lions]
#call the function from fresh_tomatoes.py that opens the webpage - execute code from this file
fresh_tomatoes.open_movies_page(movies)
