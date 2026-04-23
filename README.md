# Student Smart Assistant System

A Python-based smart assistant designed to help students manage their academic and daily activities efficiently. This project integrates core programming concepts with data analysis techniques to track assignments, attendance, expenses, and academic performance.

---

## Overview

The Student Smart Assistant System is a modular, class-based application that provides the following functionalities:

- Manage assignments by tracking deadlines and identifying overdue tasks.
- Track attendance, calculate percentages, and estimate safe absence limits using NumPy.
- Analyze academic performance to determine strongest and weakest subjects using Pandas.
- Monitor syllabus completion for both college coursework and self-study.
- Maintain a searchable to-do list using Regular Expressions.
- Record and analyze expenses, including categorization by source of income.
- Perform calculations including arithmetic operations, array processing, and matrix operations.

---

## Features

### User Authentication
- Secure signup and login system.
- Password validation using regular expressions.
- Persistent user data storage through file handling.

### Academic Modules

Assignment Management:
- Uses Pandas and datetime to track deadlines.
- Identifies overdue assignments automatically.

Attendance Tracking:
- Maintains subject-wise attendance records.
- Calculates attendance percentage and predicts shortages using NumPy.

Marks Analysis:
- Uses Pandas DataFrame for performance analysis.
- Identifies highest and lowest scoring subjects.

Syllabus Tracking:
- Tracks progress for college syllabus and self-study topics separately.

---

### Utility Modules

To-Do Management:
- Stores tasks using Pandas.
- Supports keyword-based searching using regular expressions.

Expense Tracking:
- Uses dictionaries to categorize and summarize expenses.
- Tracks income sources such as parental support or self-earned money.

Calculator:
- Supports basic arithmetic operations.
- Performs NumPy-based array and matrix computations.

---

## Concepts Implemented

- Object-Oriented Programming (OOP) using classes for modular design.
- Pandas for structured data handling and analysis.
- NumPy for numerical computations and matrix operations.
- Regular Expressions for validation and searching.
- File Handling for persistent data storage.
- Dictionaries for structured data representation.
- Datetime module for deadline tracking.

---

## How to Run

1. Install required libraries:
   pip install numpy pandas
2. Run the application:
   python main.py
   
---

## Future Enhancements

- Graphical User Interface using Tkinter or PyQt.
- Database integration using SQLite or MySQL.
- Web-based interface using Flask or Django.
- Integration of intelligent recommendation systems.

---

## Author

Student Name: Subhasmita Swain  
SAP ID: 590022427  
Faculty Guidance: Virender Lkadyan