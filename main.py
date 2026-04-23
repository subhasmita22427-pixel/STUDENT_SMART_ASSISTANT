"""
PROGRAM SUMMARY:
* Acts as the OOP Orchestrator for the Student Smart Assistant, replacing functional calls with Object-Oriented Method calls.
* Instance Management: Initializes all Manager objects (Auth, Assignment, Attendance, etc.) at the start of the execution.
* Encapsulation: Ensures that the Main Menu does not need to know 'how' data is saved, only 'which' method to call.
* Navigation Logic: Maintains a robust nested-loop structure, allowing seamless transition between academic and utility sub-menus.
* Integration: Synchronizes multiple specialized modules into a single interactive terminal interface.
"""

# Import the Classes from your modules
from auth import AuthManager
from academics.assignment import AssignmentManager
from academics.attendance import AttendanceTracker
from academics.marks import MarksManager
from academics.syllabus import SyllabusManager
from utilities.todo import TodoManager
from utilities.expenses import ExpenseManager
from utilities.calculator import SmartCalculator

# OBJECT INITIALIZATION 
# Create one instance of each class to use throughout the program
auth_obj = AuthManager()
assign_obj = AssignmentManager()
attend_obj = AttendanceTracker()
marks_obj = MarksManager()
syll_obj = SyllabusManager()
todo_obj = TodoManager()
exp_obj = ExpenseManager()
calc_obj = SmartCalculator()

# main menu
def main_menu():
    while True:
        print("\n----- STUDENT SMART ASSISTANT -----")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            auth_obj.signup()
        elif choice == "2":
            if auth_obj.login():
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

# --- SUB-MENUS (Updated to use Objects) ---

def assignment_menu():
    while True:
        print("\n--- ASSIGNMENT MENU ---")
        print("1. Add Assignment")
        print("2. View Assignments")
        print("3. Mark Complete")
        print("4. Back")
        c = input("Enter choice: ")
        if c == "1": assign_obj.add_assignment()
        elif c == "2": assign_obj.view_assignments()
        elif c == "3": assign_obj.mark_complete()
        elif c == "4": break

def attendance_menu():
    while True:
        print("\n--- ATTENDANCE MENU ---")
        print("1. Add Attendance")
        print("2. View Attendance")
        print("3. Check Shortage")
        print("4. Back")
        c = input("Enter choice: ")
        if c == "1": attend_obj.add_attendance()
        elif c == "2": attend_obj.view_attendance()
        elif c == "3": attend_obj.check_shortage()
        elif c == "4": break

def marks_menu():
    while True:
        print("\n--- MARKS MENU ---")
        print("1. View Marks")
        print("2. Check Fail")
        print("3. Back")
        c = input("Enter choice: ")
        if c == "1": marks_obj.view_marks()
        elif c == "2": marks_obj.check_fail()
        elif c == "3": break

def syllabus_menu():
    while True:
        print("\n--- SYLLABUS MENU ---")
        print("1. Add Topic")
        print("2. Mark Complete")
        print("3. View Progress")
        print("4. Back")
        c = input("Enter choice: ")
        if c == "1": syll_obj.add_topic()
        elif c == "2": syll_obj.mark_done()
        elif c == "3": syll_obj.view_progress()
        elif c == "4": break

def todo_menu():
    while True:
        print("\n--- TO-DO MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Done")
        print("4. Search Task")
        print("5. Back")
        c = input("Enter choice: ")
        if c == "1": todo_obj.add_task()
        elif c == "2": todo_obj.view_tasks()
        elif c == "3": todo_obj.mark_done()
        elif c == "4": todo_obj.search_task()
        elif c == "5": break

def expense_menu():
    while True:
        print("\n--- EXPENSE MENU ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Back")
        c = input("Enter choice: ")
        if c == "1": exp_obj.add_expense()
        elif c == "2": exp_obj.view_expenses()
        elif c == "3": break

def calculator_menu():
    while True:
        print("\n--- CALCULATOR MENU ---")
        print("1. Normal Calculator")
        print("2. Array Calculator")
        print("3. Matrix Calculator")
        print("4. Back")
        ch = input("Enter choice: ")
        if ch == "1": calc_obj.normal_calculator()
        elif ch == "2": calc_obj.array_calculator()
        elif ch == "3": calc_obj.matrix_calculator()
        elif ch == "4": break

if __name__ == "__main__":
    main_menu()