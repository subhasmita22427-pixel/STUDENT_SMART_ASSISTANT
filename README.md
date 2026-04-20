#  Student Smart Assistant System

A Python-based smart assistant designed to help students manage their academic and daily activities efficiently.  
This project combines core programming concepts with real-world use cases such as tracking assignments, attendance, expenses, and performing data analysis.

---

##  Overview

The **Student Smart Assistant System** is a menu-driven application that allows users to:

- Manage assignments and syllabus progress  
- Track attendance and predict shortage  
- Analyze marks and identify weak subjects  
- Maintain a to-do list with deadlines  
- Record and analyze expenses  
- Perform calculations using NumPy (including matrix operations)

The project is built using modular programming and demonstrates practical implementation of Python fundamentals.

---

##  Project Structure
student_smart_assistant/
│
├── main.py
├── auth.py
│
├── academics/
│ ├── assignment.py
│ ├── attendance.py
│ ├── marks.py
│ └── syllabus.py
│
├── utilities/
│ ├── todo.py
│ ├── expense.py
│ └── calculator.py
│
├── data/
│ ├── users.txt
│ ├── assignments.txt
│ ├── attendance.csv
│ ├── marks.txt
│ ├── syllabus.csv
│ ├── todo.csv
│ └── expenses.txt


---

##  Features

###  User Authentication
- Signup and login system
- Data stored using file handling
- Input validation using regular expressions

###  Assignment Tracker
- Add and manage assignments
- Track completion status
- Implemented using lists

###  Attendance Manager
- Store subject-wise attendance
- Calculate percentage
- Predict shortage and safe bunk limit
- Uses NumPy and Pandas

###  Marks Analyzer
- Calculate total and percentage
- Identify failed subjects
- Uses tuple and set

###  Syllabus Tracker
- Add and track topics
- Monitor completion progress
- Uses Pandas and Set

###  To-Do List Manager
- Add tasks with deadlines
- Mark tasks as complete
- Search tasks using regex
- Uses Pandas Series and Dictionary

###  Expense Tracker
- Record daily expenses
- Generate category-wise summary
- Uses Dictionary

###  Calculator System
- Basic operations (add, subtract, multiply, divide)
- Array operations (sum, average, min, max)
- Matrix multiplication using NumPy

---

##  Concepts Implemented

| Concept | Usage |
|--------|------|
| List | Assignment management |
| Tuple | Attendance, Marks |
| Set | Marks, Syllabus |
| Dictionary | To-do, Expense |
| NumPy | Calculator, Attendance |
| Pandas | To-do, Attendance, Syllabus |
| Regex | Authentication, Search |
| File Handling | Data storage |

---

##  How to Run

1. Install required libraries:
   ```bash
   pip install numpy pandas