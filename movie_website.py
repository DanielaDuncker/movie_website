import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "http://www.youtube.com/watch?v=vwyZH85NQC4")
# print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")
# print(avatar.storyline)
# avatar.show_trailer()

harry_potter = media.Movie("Harry Potter and the Sorcerer's stone",
                           "A boy finds out he's a wizard and goes to magic school",
                           "https://www.vintagemovieposters.co.uk/wp-content/uploads/2015/07/hpphilosopherquadlarge1.jpg",
                           "https://www.youtube.com/watch?v=eKSB0gXl9dw")
# print(harry_potter.storyline)
# harry_potter.show_trailer()

ratatouille = media.Movie("Ratatoouille", "A rat is a chef in Paris",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors",
                                "http://4.bp.blogspot.com/-3Ivbv2KGJ98/TikWAdH_6yI/AAAAAAAAIMU/ozf_9q8y4zQ/s1600/midnight-in-paris-poster.jpg",
                                "https://youtube.com/watch?v=atLg2wQQxvU")

school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

movies = [toy_story, avatar, harry_potter, ratatouille, midnight_in_paris, school_of_rock]
fresh_tomatoes.open_movies_page(movies)
