def add(x,y):
    """Add two numbers."""
    return x + y
def subtract(x,y):
    """Subtract two numbers."""
    return x - y
def multiply(x,y):
    """Multiply two numbers."""
    return x * y
def divide(x,y):
    """Divide two numbers."""
    if y == 0:
        return None
    return x / y

def main():
    print("Welcome to the simple calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            if result is None:
                print("Error: Division by zero.")
            else:
                print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input")

# This is a simple calculator application that performs basic arithmetic operations.
if __name__ == "__main__":
    main()