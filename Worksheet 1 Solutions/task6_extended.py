# task6_extended.py
# This program manages a list of a users favourite movies.
# Changelog: Functions created for each task
#            Error handling
#            File I/O - Movies are stored in a binary file.

import pickle

movies = []

def loadData():
    moviefile = open('movies', 'rb')
    movlist = pickle.load(moviefile)
    for i in movlist:
        movies.append(i)
    moviefile.close()    

def storeData():
    moviefile = open('movies', 'wb')
    pickle.dump(movies, moviefile)
    moviefile.close()

def add_movie(movie_name):
    movies.append(movie_name)
    return movie_name + " has been added to your list!"

def view_movies():
    print("Favourite movies:")
    for i in movies:
        print(i)

def remove_movie(movie_name):
    if len(movies) > 0:
        try:
            movie_position = movies.remove(movie_name)
            print(movie_name, "has been removed from your list!")  
        except:
            print("The movie you have entered is not on your list.")
    else:
        print("Your movie list is empty!")
    
def search_for_movie(movie_name):
    try:
        if movies.index(movie_name) >= 0:
            print(movie_name, "has been found in your list!")
            print("______________________________________________\n")  
    except:
        print(movie_name, "is not in your list")
        print("______________________________________________\n")
        
def main():
    loadData()
    print("""
1. Add Movie: Add a new movie to the list.
2. View Movies: Display all the movies in the list.
3. Remove Movie: Remove a movie from the list by its name.
4. Search for a Movie: Check is a specific movie is in the list.
5. Exit.
""")
    try:
        choice = eval(input("Enter your choice: "))
        while choice != 5:
            if choice == 1:
                print("______________________________________________\n")
                movie_name = input("Enter the name of the movie: ")
                print(add_movie(movie_name))
                print("______________________________________________\n")
            elif choice == 2:
                print("______________________________________________\n")
                view_movies()
                print("______________________________________________\n")
            elif choice == 3:
                print("______________________________________________\n")
                movie_name = input("Enter the name of the movie: ")
                remove_movie(movie_name)
                print("______________________________________________\n")            
            elif choice == 4:
                print("______________________________________________\n")
                movie_name = input("Enter the name of the movie: ")
                search_for_movie(movie_name)
            else: 
                print("______________________________________________\n")
                print("Invalid input!")
                print("______________________________________________\n")
            print("""
    1. Add Movie: Add a new movie to the list.
    2. View Movies: Display all the movies in the list.
    3. Remove Movie: Remove a movie from the list by its name.
    4. Search for a Movie: Check is a specific movie is in the list.
    5. Exit.
            """)        
            choice = eval(input("Enter your choice: "))
        storeData()
    except:
        print("The program expects a number as input.")   
        storeData()

if __name__ == "__main__":
    main()
            
            
