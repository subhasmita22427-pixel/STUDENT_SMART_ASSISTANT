from auth import signup, login

# academics
from academics.assignment import add_assignment, view_assignments, mark_complete
from academics.attendance import add_attendance, view_attendance, check_shortage
from academics.marks import view_marks, check_fail  
from academics.syllabus import add_topic, mark_done, view_progress

# utilities
from utilities.todo import add_task, view_tasks, mark_done as todo_done, search_task
from utilities.expenses import add_expense, view_expenses
from utilities.calculator import *


#main menu
def main_menu():
    while True:
        print("\n----- STUDENT SMART ASSISTANT -----")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            signup()

        elif choice == "2":
            if login():
                student_menu()

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


# student menu
def student_menu():
    while True:
        print("\n----- STUDENT MENU -----")
        print("1. Assignment")
        print("2. Attendance")
        print("3. Marks")
        print("4. Syllabus")
        print("5. To-Do")
        print("6. Expense")
        print("7. Calculator")
        print("8. Logout")

        ch = input("Enter choice: ")

        if ch == "1":
            assignment_menu()
        elif ch == "2":
            attendance_menu()
        elif ch == "3":
            marks_menu()
        elif ch == "4":
            syllabus_menu()
        elif ch == "5":
            todo_menu()
        elif ch == "6":
            expense_menu()
        elif ch == "7":
            calculator_menu()
        elif ch == "8":
            print("Logged out")
            break
        else:
            print("Invalid choice")


#assignment
def assignment_menu():
    while True:
        print("\n--- ASSIGNMENT MENU ---")
        print("1. Add Assignment")
        print("2. View Assignments")
        print("3. Mark Complete")
        print("4. Back")

        c = input("Enter choice: ")

        if c == "1":
            add_assignment()
        elif c == "2":
            view_assignments()
        elif c == "3":
            mark_complete()
        elif c == "4":
            break
        else:
            print("Invalid choice")


# attendance
def attendance_menu():
    while True:
        print("\n--- ATTENDANCE MENU ---")
        print("1. Add Attendance")
        print("2. View Attendance")
        print("3. Check Shortage")
        print("4. Back")

        c = input("Enter choice: ")

        if c == "1":
            add_attendance()
        elif c == "2":
            view_attendance()
        elif c == "3":
            check_shortage()
        elif c == "4":
            break
        else:
            print("Invalid choice")


# marks
def marks_menu():
    while True:
        print("\n--- MARKS MENU ---")
        print("1. View Marks")
        print("2. Check Fail")
        print("3. Back")

        c = input("Enter choice: ")

        if c == "1":
            view_marks()
        elif c == "2":
            check_fail()
        elif c == "3":
            break
        else:
            print("Invalid choice")

#syllabus
def syllabus_menu():
    while True:
        print("\n--- SYLLABUS MENU ---")
        print("1. Add Topic")
        print("2. Mark Complete")
        print("3. View Progress")
        print("4. Back")

        c = input("Enter choice: ")

        if c == "1":
            add_topic()
        elif c == "2":
            mark_done()
        elif c == "3":
            view_progress()
        elif c == "4":
            break
        else:
            print("Invalid choice")


# todo
def todo_menu():
    while True:
        print("\n--- TO-DO MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Done")
        print("4. Search Task")
        print("5. Back")

        c = input("Enter choice: ")

        if c == "1":
            add_task()
        elif c == "2":
            view_tasks()
        elif c == "3":
            todo_done()
        elif c == "4":
            search_task()
        elif c == "5":
            break
        else:
            print("Invalid choice")


# expense
def expense_menu():
    while True:
        print("\n--- EXPENSE MENU ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Back")

        c = input("Enter choice: ")

        if c == "1":
            add_expense()
        elif c == "2":
            view_expenses()
        elif c == "3":
            break
        else:
            print("Invalid choice")


# calculator
def calculator_menu():
    while True:
        print("\n--- CALCULATOR MENU ---")
        print("1. Normal Calculator")
        print("2. Array Calculator")
        print("3. Matrix Calculator")
        print("4. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            normal_calculator()
        elif ch == "2":
            array_calculator()
        elif ch == "3":
            matrix_calculator()
        elif ch == "4":
            break
        else:
            print("Invalid choice")
main_menu()