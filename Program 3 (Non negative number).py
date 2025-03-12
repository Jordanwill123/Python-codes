def calculate_factorial(n):
    # Check if the number is 0
    if n == 0:
        return 1

    # Initialize result as 1
    result = 1

    # Loop to compute the factorial
    for i in range(1, n + 1):
        result *= i

    return result


def main():
    # Prompt user for input
    user_input = input("Please enter a non-negative integer: ")

    try:
        # Try to convert input to an integer
        number = int(user_input)

        # Check if the number is non-negative
        if number < 0:
            print("Error: The input is a negative number. Please enter a non-negative integer.")
        else:
            # Calculate and display the factorial
            result = calculate_factorial(number)
            print(f"The factorial of {number} is {result}.")

    except ValueError:
        # Handle case where input is not a valid integer
        print("Error: Invalid input. Please enter a valid non-negative integer.")


# Run the program
if __name__ == "__main__":
    main()
