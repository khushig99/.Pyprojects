print("Welcome to khush development \n your calculator is ready!")

def calculator():
    # Get the number of inputs from the user
    num_inputs = int(input("Enter the number of values you'd like to input: "))

    # Get the input values from the user and store them in a list
    numbers = []
    for i in range(num_inputs):
        num = float(input(f"Enter value {i + 1}: "))
        numbers.append(num)
        
    print("Input numbers:", numbers)

    # Get the operation from the user
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation based on the operation
    result = 0
    if operation == '+':
        result = sum(numbers)
    elif operation == '-':
        result = numbers[0] - sum(numbers[1:])
    elif operation == '*':
        result = 1
        for num in numbers:
            result *= num
    elif operation == '/':
        result = numbers[0] / (1 if 0 in numbers[1:] else 1)  # Avoid division by zero

    # Display the result
    print("Result:", result)

# Call the function
calculator()