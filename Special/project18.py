def check_age():

    while True:

        try:

            age = int(input("Enter your age: "))

            if age < 0:

                raise ValueError("Age cannot be negative.")
    
            break
        except ValueError:

            print("Invalid input. Please enter a number.")


    if age % 2 == 0:

        print(f"Your age {age} is even.")
    else:

        print(f"Your age {age} is odd.")


check_age()