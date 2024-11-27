# A basic calculator that supports operations such as addition, subtraction, multiplication and division
# A menu will allow the user to perform operations
# Starting value is "0" so the user can choose starting value
# All numbers are rounded to the nearest whole number, no decimals
# A calculator.txt file will be created to store all values until

file = open("calculator.txt", "w") #create calculator.txt file
file.close()

def main(): #create the calculator
    while True:    # create the menu for user to choose which operation they want to do
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. View Calculations")
        print("6. Exit")
        choice = input("Enter your choice of operation: ")
        if choice == "1":
            add()
        elif choice == "2":
            subtract()
        elif choice == "3":
            multiply()
        elif choice == "4":
            divide()
        elif choice == "5":
            view_calculations()
        elif choice == "6":
            break               # exits the loop
        else:                   # user entered invalid option
            print("Invalid choice")


def add():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number"))
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")    # will print out the entire function, such as: 5 + 5 = 10
    file = open("calculator.txt", "a")
    file.write(f"{num1} + {num2} = {result}\n") # write the calculation to the calculator.txt file
    file.close()

def subtract():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number"))
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")    # will print out the entire function, such as: 20 - 10 = 10
    file = open("calculator.txt", "a")
    file.write(f"{num1} - {num2} = {result}\n") # write the calculation to the calculator.txt file
    file.close()

def multiply():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number"))
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")    # will print out the entire function, such as: 5 * 5 = 25
    file = open("calculator.txt", "a")
    file.write(f"{num1} * {num2} = {result}\n") # write the calculation to the calculator.txt file
    file.close()

def divide():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number"))
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")    # will print out the entire function, such as: 100 / 10 = 10
    file = open("calculator.txt", "a")
    file.write(f"{num1} / {num2} = {result}\n") # write the calculation to the calculator.txt file
    file.close()

def view_calculations():
    file = open("calculator.txt", "r")
    calculations = file.readlines() # read all lines in the calculator.txt file
    file.close()
    for c in calculations:
        print(c.strip())

main()

# thanks to some help from:
# https://www.geeksforgeeks.org/make-simple-calculator-using-python/
# https://medium.com/@muhamadafrizal5/building-a-simple-calculator-with-python-f676132d3e10
# https://www.geeksforgeeks.org/python-output-using-print-function/