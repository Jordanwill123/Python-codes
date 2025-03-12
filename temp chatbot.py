def chatbot():
    print("Hello! Welcome to the weather chatbot.")

    # Ask about the user's day with restricted options
    while True:
        user_mood = input("How is your day going? (good, bad, ok): ").strip().lower()
        if user_mood in ["good", "bad", "ok"]:
            if user_mood == "good":
                print("That’s great to hear!")
            elif user_mood == "ok":
                print("Got it! Hope the rest of your day goes well.")
            else:
                print("Sorry to hear that. I hope things get better!")
            break  # Exit loop if input is valid
        else:
            print("Error: Please enter 'good', 'bad', or 'ok'.")

    # Ask for temperature with validation
    while True:
        temp_input = input("What is the temperature outside (in degrees Fahrenheit)? ").strip()

        try:
            temp = float(temp_input)  # Convert input to a float
            if -10 <= temp <= 115:
                break  # Valid input, exit loop
            else:
                print("Error: Please enter a temperature between -10°F and 115°F.")
        except ValueError:
            print("Error: Please enter a valid number for the temperature.")

    # Provide clothing advice
    if temp <= 54:
        print("It's too cold! Put on a coat.")
    elif 55 <= temp <= 70:
        print("It's a bit chilly. You should wear a jacket.")
    else:
        print("The weather is nice. You don’t need a jacket!")

    print("Have a great day!")  # Farewell message


# Run the chatbot
chatbot()
