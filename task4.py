# task4.py
# This program counts the number of words in a sentence entered by the user

def main():
    print("""
#############################
      WORD COUNTER
#############################""")    
    phrase = input("Enter a phrase: ")
    phrase_split = phrase.split()
    print("The number of words in the phrase is:", len(phrase_split))
    
if __name__ == "__main__":
    main()
        