class MovieReview:
    def __init__(self,movie,story,actors,music):
        self.movie_name=movie
        self.stroy_rating=story
        self.actors_rating=actors
        self.music_rating=music
        self.avg=int((self.stroy_rating+self.actors_rating+self.music_rating)/3)
        self.myrating={
            "Movie Name":self.movie_name,
            "Story Rating":self.stroy_rating,
            "Actor Rating":self.actors_rating,
            "Music Rating":self.music_rating,
            "Avg rating":self.avg
        }
    def add_movie_ratings(self,movie_list):
        movie_list.append(self.myrating)
    def avg_star_ratings(self,movie_list):
        for movie in movie_list:
            if(movie["Avg rating"]==1):
                print("Thanks for the response, you rated the movie with  *")
                print(movie)
            elif(movie["Avg rating"]==2):
                print("Thanks for the responce, you rated the movie with  **")
                print(movie)
            else:
                print("Thanks for the responce, you rated the movie with  ***")
movieweviews=[]
review2=MovieReview("Beautiful Sound",2,1,3)
review2.add_movie_ratings(movieweviews)
review2.avg_star_ratings(movieweviews)