def simple_calculator():
    print("Welcome to the Simple Calculator!")

    try:
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print("Choose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        operation = input("Enter the symbol of the operation (+, -, *, /): ")

        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                return
        else:
            print("Invalid operation selected.")
            return

        
        print(f"The result of {num1} {operation} {num2} is: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


simple_calculator()
