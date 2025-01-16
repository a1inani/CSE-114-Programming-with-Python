# task3.py
# This program creates an acronym from a provided phrase.

def main():
    print("""
#############################
      ACRONYM GENERATOR
#############################""")
    phrase = input("Enter a phrase: ")
    split_phrase = phrase.split()
    output_string = ""
    for i in split_phrase:
        output_string = output_string + i[0].upper()
    print("The acronym of -", phrase, "- is:", output_string)
    
if __name__ == "__main__":
    main()