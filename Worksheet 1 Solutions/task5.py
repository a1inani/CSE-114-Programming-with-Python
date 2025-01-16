# task5.py
# This program calculates class standing from the number of credits earned.

def main():
    credits = eval(input("Enter the number of credits earned: "))
    if credits >= 26:
        print("Class standing: SENIOR")
    elif credits >= 16:
        print("Class standing: JUNIOR")
    elif credits >= 7:
        print("Class standing: SOPHOMORE")
    else:
        print("Class standing: FRESHMAN")
    
if __name__ == "__main__":
    main()