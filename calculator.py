def calculator():
    """
    Simple Calculator Program
    Allows the user to perform basic arithmetic operations:
    Addition, Subtraction, Multiplication, and Division.
    """
    
    print("Simple Calculator")
    print("-----------------")

    # Get user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Operation menu
    print("\nSelect Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1/2/3/4 or +, -, *, /): ")

    # Perform calculation
    if choice in ('1', '+'):
        result = num1 + num2
        operation = '+'
    elif choice in ('2', '-'):
        result = num1 - num2
        operation = '-'
    elif choice in ('3', '*'):
        result = num1 * num2
        operation = '*'
    elif choice in ('4', '/'):
        if num2 == 0:
            print("Error: Division by zero is undefined.")
            return
        result = num1 / num2
        operation = '/'
    else:
        print("Invalid operation choice!")
        return

    # Output result
    print(f"\nResult: {num1} {operation} {num2} = {result}")


if __name__ == "__main__":
    calculator()
