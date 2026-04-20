import pandas as pd
import re

file = "data/todo.csv"


# add task
def add_task():
    try:
        task = input("Enter task: ")
        date = input("Enter deadline (dd-mm-yyyy): ")

        #Pandas Series
        
        task_series = pd.Series([task, date, "Pending"],
                                index=["Task", "Date", "Status"])

        try:
            df = pd.read_csv(file)
        except:
            df = pd.DataFrame(columns=["Task", "Date", "Status"])

        df = pd.concat([df, task_series.to_frame().T], ignore_index=True)

        df.to_csv(file, index=False)

        print("Task added")

    except:
        print("Error adding task")


# view tasks
def view_tasks():
    try:
        df = pd.read_csv(file)

        if df.empty:
            print("No tasks found")
            return

        print("\nTasks:")
        for i, row in df.iterrows():
            print(i+1, "|", row["Task"], "|", row["Date"], "|", row["Status"])

    except:
        print("Error reading tasks")


# mark task complete
def mark_done():
    try:
        df = pd.read_csv(file)

        if df.empty:
            print("No tasks found")
            return

        print(df)

        n = int(input("Enter task number: "))

        if n < 1 or n > len(df):
            print("Invalid choice")
            return

        df.at[n-1, "Status"] = "Done"

        df.to_csv(file, index=False)

        print("Task marked as done")

    except:
        print("Error updating task")


# search task using regex
def search_task():
    try:
        keyword = input("Enter keyword: ")

        df = pd.read_csv(file)

        found = False

        for i, row in df.iterrows():

            if re.search(keyword, str(row["Task"]), re.IGNORECASE):
                print(row["Task"], "|", row["Date"], "|", row["Status"])
                found = True

        if not found:
            print("No matching task found")

    except:
        print("Error searching task")