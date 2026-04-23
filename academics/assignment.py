"""
program summary:
* re-engineered the assignmentmanager class to use pandas for better visualization and deadline tracking.
* time logic: uses the 'datetime' module to compare the system clock with assignment deadlines.
* dynamic tracking: uses a custom function with '.apply()' to label tasks as 'overdue' automatically.
* pandas display: replaces standard loops with dataframe views for a professional look.
* persistence: saves data back to 'data/assignments.txt' using '.to_csv()' while keeping the original format.
"""

import pandas as pd
from datetime import datetime

class assignmentmanager:
    def __init__(self):
        # path to our assignment data file
        self.file = "data/assignments.txt"

    # function to add a new task
    def add_assignment(self):
        try:
            sub = input("enter subject: ")
            task = input("enter task name: ")
            date = input("enter deadline (dd-mm-yy): ")

            # every new assignment starts as pending
            row = f"{sub},{task},{date},pending\n"

            # opening file in append mode
            f = open(self.file, "a")
            f.write(row)
            f.close()
            print("assignment added to list")

        except:
            print("error: could not save assignment")

    # viewing tasks with automatic overdue check
    def view_assignments(self):
        try:
            # loading data into a pandas table
            df = pd.read_csv(self.file, names=["subject", "name", "deadline", "status"])
            
            if df.empty:
                print("no tasks found")
                return

            # getting today's date for comparison
            now = datetime.now()
            
            # helper function to check dates row by row
            def check_status(r):
                if r["status"] == "done":
                    return "completed"
                
                try:
                    # strptime converts text into a date object
                    target = datetime.strptime(r["deadline"], "%d-%m-%y")
                    if target < now:
                        return "overdue"
                    return "pending"
                except:
                    return "date error"

            # applying the date logic to the whole table
            df["live_status"] = df.apply(check_status, axis=1)

            print("\n--- assignment list ---")
            # displaying specific columns in a clean way
            print(df[["subject", "name", "deadline", "live_status"]].to_string(index=False))

        except FileNotFoundError:
            print("database file not found")
        except:
            print("error loading assignments")

    # function to mark a task as finished
    def mark_complete(self):
        try:
            df = pd.read_csv(self.file, names=["subject", "name", "deadline", "status"])
            
            if df.empty:
                print("nothing to update")
                return

            print("\ncurrent list:")
            print(df)
            
            idx = int(input("\nenter index number to finish: "))

            if 0 <= idx < len(df):
                # .at helps change a specific value in the table
                df.at[idx, "status"] = "done"
                # saving without headers to keep the file clean
                df.to_csv(self.file, index=False, header=False)
                print("task marked as done")
            else:
                print("invalid index")

        except:
            print("error updating status")