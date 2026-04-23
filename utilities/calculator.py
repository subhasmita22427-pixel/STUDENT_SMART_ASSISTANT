"""
PROGRAM SUMMARY:
* Consolidates high-performance mathematical operations into the 'SmartCalculator' class using NumPy.
* Organization: Groups distinct calculation modes (Scalar, Array-based, and Linear Algebra) into class methods.
* Advanced Computation: Leverages NumPy's 'ufuncs' (universal functions) for efficient element-wise array operations.
* Matrix Logic: Implements 2D array processing with dimensionality validation for dot product multiplication (m1.shape[1] == m2.shape[0]).
* Statistical Analysis: Integrates NumPy functions like mean, sum, max, and min to provide quick data insights on arrays.
* OOP Design: Demonstrates method grouping to provide a clean and intuitive user interface for complex math tasks.
"""

import numpy as np

class SmartCalculator:
    def __init__(self):
        # No file handling needed here, but the class 
        # acts as a container for all NumPy operations.
        pass

    # for basic
    def normal_calculator(self):
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
            except:
                print("Invalid input")

    # for array
    def array_calculator(self):
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
                arr1 = list(map(float, input("Enter first array (space separated): ").split()))
                arr2 = list(map(float, input("Enter second array (space separated): ").split()))

                np1 = np.array(arr1)
                np2 = np.array(arr2)

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
            except:
                print("Invalid input or shape mismatch")

    # for matrix
    def matrix_calculator(self):
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

                print("Enter Matrix 1 (row by row):")
                m1 = [list(map(float, input().split())) for _ in range(r)]

                print("Enter Matrix 2 (row by row):")
                m2 = [list(map(float, input().split())) for _ in range(r)]

                m1 = np.array(m1)
                m2 = np.array(m2)

                if ch == "1":
                    print("Result:\n", np.add(m1, m2))
                elif ch == "2":
                    print("Result:\n", np.subtract(m1, m2))
                elif ch == "3":
                    if m1.shape[1] != m2.shape[0]:
                        print("Multiplication not possible (Cols of M1 must equal Rows of M2)")
                    else:
                        print("Result:\n", np.dot(m1, m2))
                else:
                    print("Invalid choice")
            except:
                print("Invalid input")