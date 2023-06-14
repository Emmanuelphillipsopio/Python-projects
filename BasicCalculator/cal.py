#define the functions needed: add, sub, multiply, division
#print the option
#ask for the input values
#call a fuctions and add a while loop for program continuation

def add(a,b):
    answer = a + b
    print(f"{a} + {b} = {answer}\n\n")

def sub(a,b):
    answer = a - b
    print(f"{a} - {b} = {answer}\n\n")

def mult(a,b):
    answer = a * b
    print(f"{a} * {b} = {answer}\n\n")

def div(a,b):
    answer = a / b
    print(f"{a} / {b} = {answer}\n\n")
    
while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit Calculator")

    choice = input("Input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Input first number: "))
        b = int(input("input second number: "))
        add(a,b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("Input first number: "))
        b = int(input("input second number: "))
        sub(a,b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("Input first number: "))
        b = int(input("input second number: "))
        mult(a,b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("Input first number: "))
        b = int(input("input second number: "))
        div(a,b)
    elif choice == "e" or choice == "E":
        print("Calculator Terminated")
        quit()