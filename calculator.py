print("Welcome to the Calculator Program!")
print("Press '0' to quit at any time.")
while True:
    print("\nSelect operation:")
    print("1. Addition")   
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter choice (1/2/3/4): "))
    if choice == 0:
        break
    elif choice == 1:
        v1=int(input("Enter first number: "))
        v2=int(input("Enter second number: "))
        print(f"The sum is:", v1 + v2)
    elif choice == 2:
        v1=int(input("Enter first number: "))
        v2=int(input("Enter second number: "))
        print(f"The difference is:", v1 - v2)
    elif choice == 3:
        v1=int(input("Enter first number: "))
        v2=int(input("Enter second number: "))
        print(f"The product is:", v1 * v2)
    elif choice == 4:
        v1=int(input("Enter first number: "))
        v2=int(input("Enter second number: "))
        print(f"The quotient is:", v1 / v2)
    else:
        print("Invalid input. Please try again.")
        