# task6.py
# This program manages a list of a users favourite movies.

def main():
    print("""
1. Add Movie: Add a new movie to the list.
2. View Movies: Display all the movies in the list.
3. Remove Movie: Remove a movie from the list by its name.
4. Search for a Movie: Check is a specific movie is in the list.
5. Exit.
""")
    movies = []
    choice = eval(input("Enter your choice: "))
    while choice != 5:
        if choice == 1:
            print("______________________________________________\n")
            movie_name = input("Enter the name of the movie: ")
            movies.append(movie_name)
            print(movie_name, "has been added to your list!")
            print("______________________________________________\n")
        elif choice == 2:
            print("______________________________________________\n")
            print("Favourite movies:")
            for i in movies:
                print(i)
            print("______________________________________________\n")
        elif choice == 3:
            print("______________________________________________\n")
            movie_name = input("Enter the name of the movie: ")
            movie_position = movies.remove(movie_name)
            print(movie_name, "has been removed from your list!")
            print("______________________________________________\n")            
        elif choice == 4:
            print("______________________________________________\n")
            movie_name = input("Enter the name of the movie: ")
            if movies.index(movie_name) >= 0:
                print(movie_name, "has been found in your list!")
                print("______________________________________________\n")
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
            
            
            