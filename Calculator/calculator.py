import art

# Define the basic math operation functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2  # Note: This does not handle division by zero

# Dictionary mapping operators to corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Main calculator function
def calculator():
    
    print(art.logo)
    
    # Boolean to keep the calculator running
    reiterate = True
    f_number = float(input("Enter first number: "))

    # Start a loop for continuous calculation
    while reiterate:
        # Print available operation symbols
        for symbols in operations:
            print(symbols)
        operators = input("Pick an operation: ")
        l_number = float(input("Enter next number: "))

        output = operations[operators](f_number, l_number)

        print(f'{f_number} {operators} {l_number} = {output}')

        # Ask the user if they want to continue calculating
        recalculate = input(
            f"Type 'y' to continue calculating with {output}, or type 'n' to start new calculation: "
        ).lower()

        # If yes, continue using the result as the first number
        if recalculate == 'y':
            f_number = float(output)
        # If no, clear the screen and start a new calculation
        elif recalculate == 'n':
            reiterate = False
            print("\n" * 20)
            calculator()  # Recursively calls the calculator to restart

calculator()
