# File : chaos.py
# A simple program illustrating chaotic behaviour .

print("This program illustrates chaotic behaviour")
x = eval(input("Enter a number between 0 and 1: "))
n = eval(input("How many numbers should I print? "))
for i in range(n):
    x = 3.9 * x * (1 - x)
    print(x)