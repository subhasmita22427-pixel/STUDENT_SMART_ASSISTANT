import numpy as np

# for basic
def normal_calculator():
    while True:
        print("\n--- BASIC CALCULATOR ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Back")

        ch = input("Enter choice: ")

        if ch == "5":
            break

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except:
            print("Invalid input")
            continue

        if ch == "1":
            print("Result:", np.add(a, b))
        elif ch == "2":
            print("Result:", np.subtract(a, b))
        elif ch == "3":
            print("Result:", np.multiply(a, b))
        elif ch == "4":
            if b == 0:
                print("Cannot divide by zero")
            else:
                print("Result:", np.divide(a, b))
        else:
            print("Invalid choice")


# for array
def array_calculator():
    while True:
        print("\n--- ARRAY OPERATIONS ---")
        print("1. Add Arrays")
        print("2. Subtract Arrays")
        print("3. Multiply Arrays")
        print("4. Divide Arrays")
        print("5. Sum of elements")
        print("6. Average")
        print("7. Max & Min")
        print("8. Back")

        ch = input("Enter choice: ")

        if ch == "8":
            break

        try:
            arr1 = list(map(float, input("Enter first array: ").split()))
            arr2 = list(map(float, input("Enter second array: ").split()))

            np1 = np.array(arr1)
            np2 = np.array(arr2)

        except:
            print("Invalid input")
            continue

        if ch == "1":
            print("Result:", np.add(np1, np2))
        elif ch == "2":
            print("Result:", np.subtract(np1, np2))
        elif ch == "3":
            print("Result:", np.multiply(np1, np2))
        elif ch == "4":
            print("Result:", np.divide(np1, np2))
        elif ch == "5":
            print("Sum:", np.sum(np1))
        elif ch == "6":
            print("Average:", np.mean(np1))
        elif ch == "7":
            print("Max:", np.max(np1), "| Min:", np.min(np1))
        else:
            print("Invalid choice")


# for matrix
def matrix_calculator():
    while True:
        print("\n--- MATRIX OPERATIONS ---")
        print("1. Matrix Addition")
        print("2. Matrix Subtraction")
        print("3. Matrix Multiplication")
        print("4. Back")

        ch = input("Enter choice: ")

        if ch == "4":
            break

        try:
            r = int(input("Enter rows: "))
            c = int(input("Enter columns: "))

            print("Enter Matrix 1:")
            m1 = [list(map(float, input().split())) for _ in range(r)]

            print("Enter Matrix 2:")
            m2 = [list(map(float, input().split())) for _ in range(r)]

            m1 = np.array(m1)
            m2 = np.array(m2)

        except:
            print("Invalid input")
            continue

        if ch == "1":
            print("Result:\n", np.add(m1, m2))

        elif ch == "2":
            print("Result:\n", np.subtract(m1, m2))

        elif ch == "3":
            if m1.shape[1] != m2.shape[0]:
                print("Multiplication not possible")
            else:
                print("Result:\n", np.dot(m1, m2))

        else:
            print("Invalid choice")

