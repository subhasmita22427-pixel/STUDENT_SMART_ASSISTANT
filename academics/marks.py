"""
program summary:
* re-engineered the marksmanager class to utilize pandas for automated academic performance analytics.
* vectorized operations: replaces manual loops with pandas column-wise addition to calculate 'total marks' instantly.
* performance insight: employs '.idxmax()' and '.idxmin()' methods to identify the highest and lowest scoring subjects.
* boolean indexing: uses conditional filtering (df[df['total'] < 35]) to isolate subjects requiring a re-test.
* data visualization: leverages the pandas dataframe structure to print a clean, aligned mark sheet.
"""

import pandas as pd

class marksmanager:
    def __init__(self):
        # path to our marks text file
        self.file = "data/marks.txt"

    # function to add marks manually
    def add_marks(self): 
        try:
            subject = input("enter subject name: ")
            internal = int(input("internal marks: "))
            mid = int(input("mid marks: "))
            end = int(input("end marks: "))

            # saving data in a simple csv format
            with open(self.file, "a") as f:
                f.write(f"{subject},{internal},{mid},{end}\n")
            print("marks saved successfully")
            
        except ValueError:
            print("error: please enter numbers for marks")
        except:
            print("something went wrong")

    # function to view marks and check performance
    def view_marks(self): 
        try:
            # reading the file using pandas
            df = pd.read_csv(self.file, names=["subject", "internal", "mid", "end"])

            if df.empty:
                print("no data found")
                return

            # calculating totals for all subjects at once
            df["total"] = df["internal"] + df["mid"] + df["end"]

            print("\n--- your marksheet ---")
            # printing the table without index numbers
            print(df[["subject", "total"]].to_string(index=False))

            # performance logic: finding max and min totals
            # idxmax and idxmin find the top and bottom rows
            top_sub = df.loc[df["total"].idxmax()]
            low_sub = df.loc[df["total"].idxmin()]

            print(f"\nbest subject: {top_sub['subject']} ({top_sub['total']} marks)")
            print(f"weakest subject: {low_sub['subject']} ({low_sub['total']} marks)")

        except FileNotFoundError:
            print("no marks file found yet")
        except:
            print("error reading the file")

    # function to find subjects with marks below 35
    def check_fail(self): 
        try:
            df = pd.read_csv(self.file, names=["subject", "internal", "mid", "end"])
            df["total"] = df["internal"] + df["mid"] + df["end"]

            # filtering: keeping only rows where total is less than 35
            failed_list = df[df["total"] < 35]

            print("\n--- fail check ---")
            if failed_list.empty:
                print("congratulations! you passed everything")
            else:
                print("you scored below 35 in these subjects:")
                print(failed_list[["subject", "total"]].to_string(index=False))

        except:
            print("error checking for failures")