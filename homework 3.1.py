def classify_hurricane(wind_speed):
    # Check if wind speed is below hurricane level
    if wind_speed < 39:
        return "The wind speed is below hurricane level. It is not a tropical storm or hurricane."
    elif wind_speed >= 39 and wind_speed <= 73:
        return "Tropical Storm: Winds are between 39 and 73 mph."
    elif wind_speed >= 74 and wind_speed <= 95:
        return "Category 1 Hurricane: Very dangerous winds will produce some damage."
    elif wind_speed >= 96 and wind_speed <= 110:
        return "Category 2 Hurricane: Extremely dangerous winds will cause extensive damage."
    elif wind_speed >= 111 and wind_speed <= 129:
        return "Category 3 Hurricane: Devastating damage will occur."
    elif wind_speed >= 130 and wind_speed <= 156:
        return "Category 4 Hurricane: Catastrophic damage will occur."
    elif wind_speed >= 157:
        return "Category 5 Hurricane: Catastrophic damage; high devastation."
    else:
        return "Error: Invalid wind speed."


def main():
    # Prompt user for input
    user_input = input("Please enter the wind speed in miles per hour (mph): ")

    try:
        # Try to convert the input to an integer
        wind_speed = int(user_input)

        #Check for negative wind speeds
        if wind_speed < 0:
            print("Error: Wind speed cannot be negative. Please enter a valid wind speed.")
        else:
            # Classify the wind speed and display the result
            result = classify_hurricane(wind_speed)
            print(result)

    except ValueError:
        # Handle case where input is not an integer
        print("Error: Invalid input. Please enter a valid integer for the wind speed.")


# Run the program
if __name__ == "__main__":
    main()
