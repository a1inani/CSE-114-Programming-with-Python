# task6.py
# This program manages a list of a users favourite movies.

movies = []

def add_movie(movie_name):
    movies.append(movie_name)
    return movie_name + " has been added to your list!"

def view_movies():
    print("Favourite movies:")
    for i in movies:
        print(i)

def remove_movie(movie_name):
    movie_position = movies.remove(movie_name)
    print(movie_name, "has been removed from your list!")   
    
def search_for_movie(movie_name):
    if movies.index(movie_name) >= 0:
        print(movie_name, "has been found in your list!")
        print("______________________________________________\n")    
        
def main():
    print("""
1. Add Movie: Add a new movie to the list.
2. View Movies: Display all the movies in the list.
3. Remove Movie: Remove a movie from the list by its name.
4. Search for a Movie: Check is a specific movie is in the list.
5. Exit.
""")
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

if __name__ == "__main__":
    main()
            
            
