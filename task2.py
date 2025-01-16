# task2.py
# This program accepts an exam score and prints out the corresponding letter grade.

def main():
    exam_score = eval(input("Enter the exam score: "))
    if exam_score >= 90:
        print("A")
    elif exam_score >= 80:
        print("B")
    elif exam_score >= 70:
        print("C")
    elif exam_score >= 60:
        print("D")
    else:
        print("F")
    
if __name__ == "__main__":
    main()