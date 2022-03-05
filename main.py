import sys
 
while True:
    print("Options:")
    print("Enter '+' to add two numbers")
    print("Enter '-' to subtract two numbers")
    print("Enter '*' to multiply two numbers")
    print("Enter '/' to divide two numbers")
    print("Enter 'FOLD' to end the program")
    userInput = input(": ")
 
#Logic for expressions
    if userInput.upper() == "FOLD":
        break
    elif userInput == "+":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
        print("The answer is " + result)
        sys.exit()
    elif userInput == "-":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 - num2)
        print("The answer is " + result)
        sys.exit()
    elif userInput == "*":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 * num2)
        print("The answer is " + result)
        sys.exit()
        
    elif userInput == "/":
        num1 = float(input("Enter another number: "))
        num2 = float(input("Enter another number: "))
        if num1 + num2 == 0:
            print("Tried to Divide by 0 + ratio + no dad + stay mad + get better + didnt ask")
            sys.exit()
        result = str(num1 / num2)
        print("The answer is " + result)
        sys.exit()
    else:
        print("Error, Please try again.")
