while True:
    print("Menu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Quit")

    try:
        choice = int(input("Enter your choice (1, 2, 3, or 4): "))

        if choice == 1:
            print("1 selected")
        elif choice == 2:
            print("2 selected")
        elif choice == 3:
            print("3 selected")
        elif choice == 4:
            print("Quit selected")
            break  # Exit the loop when option 4 is selected
        else:
            print("Option not recognized")
    except ValueError:
        print("Enter an integer choice (1, 2, 3, or 4)")
