print("Welcome to the Pattern Generator and Number Analyzer")

while True:

    print("\nSelect an option:")
    print("1. Generate a pattern")
    print("2. Analyze a range of numbers")
    print("3. Exit")

    option = int(input("Select your option: "))

    match option:

        case 1:
            for i in range(1, 6):
                for j in range(1, i + 1):
                    print("*", end="")
                print()

        case 2:
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))

            total = 0

            for num in range(start, end + 1):
                if num % 2 == 0:
                    print("Number", num, "is Even")
                else:
                    print("Number", num, "is Odd")

                total += num

            print("Sum of all numbers from", start, "to", end, "is:", total)

        case 3:
            print("\nExiting the program. Goodbye!")
            break

        case _:
            print("Invalid option! Please select 1, 2, or 3.")
