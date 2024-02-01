while True:
    user_input = input("Enter a number: ")

    try:
        number = int(user_input)
        print(f"{number} is a valid integer.")
        # Now you can work with 'number' as an integer
        break  # Exit the loop if input is a valid integer
    except ValueError:
        print(f"{user_input} is not a valid integer. Please try again.")


""" while True:
    user_input = input("Enter something")
    print(type(user_input)) """