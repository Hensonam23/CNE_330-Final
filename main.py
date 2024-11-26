# A basic calculator that supports operations such as addition, subtraction, multiplication and division
# A menu will allow the user to perform operations
# Allows continuous operations
# Starting value is "0" so the user can choose starting value
# All numbers are rounded to the nearest whole number, no decimals
# A calculator.txt file will be created to store all values until

file = open("calculator.txt", "w")
file.write("0")
file.close()

def main():
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Reset")
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
            reset()
        elif choice == "6":
            break
        else:
            print("Invalid choice")


def add():
    num = int(input("Enter a number: "))
    file = open("calculator.txt", "r")
    value = int(file.read())
    file.close()
    file = open("calculator.txt", "w")
    value += num
    file.write(str(value))
    file.close()
    print("Result:", value)

def subtract():
    num = int(input("Enter a number: "))
    file = open("calculator.txt", "r")
    value = int(file.read())
    file.close()
    file = open("calculator.txt", "w")
    value -= num
    file.write(str(value))
    file.close()
    print("Result:", value)

def multiply():
    num = int(input("Enter a number: "))
    file = open("calculator.txt", "r")
    value = int(file.read())
    file.close()
    file = open("calculator.txt", "w")
    value *= num
    file.write(str(value))
    file.close()
    print("Result:", value)

def divide():
    num = int(input("Enter a number: "))
    file = open("calculator.txt", "r")
    value = int(file.read())
    file.close()
    file = open("calculator.txt", "w")
    value //= num
    file.write(str(value))
    file.close()
    print("Result:", value)

def reset():
    file = open("calculator.txt", "w")
    file.write("0")
    file.close()
    print("Result: 0")

main()