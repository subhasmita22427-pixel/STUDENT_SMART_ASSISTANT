"""
program summary:
* migrates the attendance module into the 'attendancetracker' class to implement oop principles.
* encapsulation: stores the 'data/attendance.csv' path as a class attribute (self.file) for centralized access.
* methods: converts standalone logic into class methods (add_attendance, view_attendance, check_shortage) using 'self'.
* data processing: uses pandas for csv operations and numpy arrays for calculating 75% attendance criteria and skip-limits.
* state access: employs 'self' to ensure that every method within the class targets the same file and configuration.
"""

import numpy as np
import pandas as pd

class attendancetracker:
    def __init__(self):
        # path for the csv file
        self.file = "data/attendance.csv"

    # function to add new subject records
    def add_attendance(self):
        try:
            subject = input("enter subject name: ")
            attended = int(input("classes attended: "))
            total = int(input("total classes held: "))

            new_row = {
                "subject": subject,
                "attended": attended,
                "total": total
            }

            try:
                # trying to open existing file
                df = pd.read_csv(self.file)
            except:
                # making a new table if file is missing
                df = pd.DataFrame(columns=["subject", "attended", "total"])

            # adding the row to our table
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv(self.file, index=False)

            print("attendance saved successfully")
        except:
            print("error: could not save data")

    # function to view subject wise percentage
    def view_attendance(self):
        try:
            df = pd.read_csv(self.file)
            if df.empty:
                print("no data available")
                return

            print("\n--- current records ---")
            for i, row in df.iterrows():
                # simple calculation for percentage
                perc = (row["attended"] / row["total"]) * 100
                print(f"{i+1} | {row['subject']} | {row['attended']}/{row['total']} | {perc:.2f}%")
        except:
            print("error loading attendance")

    # function to calculate bunk limits using numpy
    def check_shortage(self):
        try:
            att = int(input("classes attended: "))
            total = int(input("total classes till now: "))
            rem = int(input("remaining classes in semester: "))

            if total <= 0:
                print("invalid total classes")
                return

            # using numpy array for calculation
            stats = np.array([att, total, rem])
            
            # current attendance percentage
            curr_perc = (stats[0] / stats[1]) * 100
            print(f"current percentage: {curr_perc:.2f}%")

            # final total classes in semester
            final_total = stats[1] + stats[2]
            # classes needed to hit 75%
            needed = (0.75 * final_total) - stats[0]

            if needed <= 0:
                print("you are safe! you can skip all remaining classes")
            else:
                # finding how many we can skip safely
                bunk_limit = stats[2] - needed
                if bunk_limit < 0:
                    print("warning: attend every class to improve")
                else:
                    print(f"you can skip {int(bunk_limit)} classes safely")

            # summarizing in a pandas dataframe
            df = pd.DataFrame({
                "attended": [att],
                "total": [total],
                "remaining": [rem],
                "percentage": [round(curr_perc, 2)]
            })
            print("\nquick summary:\n", df)

        except:
            print("please enter numeric values")