"""
program summary:
* manages tasks within a 'todomanager' class using pandas for data storage.
* classification: allows users to group tasks by category (health, habits, etc.) and frequency (daily vs specific).
* data filtering: uses boolean indexing to split the main dataframe into separate routine and task views.
* regex implementation: uses the re.search method within a lambda function to find keywords across multiple columns.
* file integrity: handles missing files by initializing an empty dataframe and ensures data persistence via csv.
"""

import pandas as pd
import re

class todomanager:
    def __init__(self):
        # set the file path
        self.file = "data/todo.csv"

    def add_task(self):
        try:
            task_name = input("enter task name: ")
            
            print("select category: 1. health | 2. habits | 3. studies | 4. other")
            choice = input("choice: ")
            
            # simple dictionary for mapping
            cats = {"1": "health", "2": "habits", "3": "studies"}
            category = cats.get(choice, "other")

            print("frequency: 1. daily | 2. specific task")
            f_choice = input("choice: ")
            freq = "daily" if f_choice == "1" else "specific"

            date = input("enter date/time (or everyday): ")

            # dictionary to hold new data
            new_row = {
                "task": task_name,
                "category": category,
                "frequency": freq,
                "date": date,
                "status": "pending"
            }

            try:
                df = pd.read_csv(self.file)
            except:
                # create new dataframe if file is missing
                df = pd.DataFrame(columns=["task", "category", "frequency", "date", "status"])

            # adding the new row to the main dataframe
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv(self.file, index=False)
            print("task saved to your list")

        except Exception as e:
            print("error adding task:", e)

    def view_tasks(self):
        try:
            df = pd.read_csv(self.file)
            if df.empty:
                print("no tasks found")
                return

            # filtering daily tasks
            print("\n--- daily routine ---")
            daily_list = df[df["frequency"] == "daily"]
            if daily_list.empty:
                print("no daily tasks added")
            else:
                print(daily_list[["category", "task", "status"]].to_string(index=False))

            # filtering specific tasks
            print("\n--- specific tasks ---")
            spec_list = df[df["frequency"] == "specific"]
            if spec_list.empty:
                print("no specific tasks added")
            else:
                print(spec_list[["category", "task", "date", "status"]].to_string(index=False))

        except:
            print("error loading tasks")

    def mark_done(self):
        try:
            df = pd.read_csv(self.file)
            print("\ncurrent tasks:")
            print(df)
            
            idx = int(input("\nenter index number to mark as done: "))
            
            if 0 <= idx < len(df):
                # updating status using .at
                df.at[idx, "status"] = "done"
                df.to_csv(self.file, index=False)
                print("status updated successfully")
            else:
                print("invalid index number")
        except:
            print("error updating the task")

    def search_task(self):
        try:
            word = input("enter keyword to search (task or category): ")
            df = pd.read_csv(self.file)
            
            # using regex to search through both columns
            # axis=1 checks row by row
            match = df.apply(lambda r: re.search(word, str(r['task']), re.IGNORECASE) or 
                                       re.search(word, str(r['category']), re.IGNORECASE), axis=1)
            results = df[match]

            if not results.empty:
                print("\nsearch results:")
                print(results.to_string(index=False))
            else:
                print("no matches found")
        except:
            print("error during search")