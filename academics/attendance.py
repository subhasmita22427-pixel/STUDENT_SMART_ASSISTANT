import numpy as np
import pandas as pd

file = "data/attendance.csv"


# add attendenve
def add_attendance():
    try:
        subject = input("Enter subject: ")
        attended = int(input("Enter classes attended: "))
        total = int(input("Enter total classes: "))

        new_data = {
            "Subject": subject,
            "Attended": attended,
            "Total": total
        }

        try:
            df = pd.read_csv(file)
        except:
            df = pd.DataFrame(columns=["Subject", "Attended", "Total"])

        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

        df.to_csv(file, index=False)

        print("Attendance added")

    except:
        print("Error adding attendance")


#view attendence
def view_attendance():
    try:
        df = pd.read_csv(file)

        if df.empty:
            print("No attendance data found")
            return

        print("\nAttendance Record:")

        for i, row in df.iterrows():
            percent = (row["Attended"] / row["Total"]) * 100
            print(i+1, "|", row["Subject"],
                  "|", row["Attended"], "/", row["Total"],
                  "| {:.2f}%".format(percent))

    except:
        print("Error reading attendance")


#check shortage 
def check_shortage():
    try:
        attended = int(input("Enter classes attended: "))
        total = int(input("Enter total classes till now: "))
        remaining = int(input("Enter remaining classes in semester: "))

        if total <= 0:
            print("No classes conducted yet")
            return

        # tuple

        data = (attended, total, remaining)

        # numpy

        arr = np.array(data)

        attended = arr[0]
        total = arr[1]
        remaining = arr[2]

        current_percent = (attended / total) * 100
        print("Current Attendance: {:.2f}%".format(current_percent))

        final_total = total + remaining
        min_required = 0.75 * final_total

        needed = min_required - attended

        if needed <= 0:
            print("You are already safe above 75%")
            print("You can skip all remaining classes:", remaining)
        else:
            max_bunk = remaining - needed

            if max_bunk < 0:
                print("Warning: You are below 75%")
                print("You must attend all remaining classes")
            else:
                print("You can skip", int(max_bunk), "classes safely")
                print("If you skip more than this, you may get debarred")

        # pandas display

        df = pd.DataFrame({
            "Attended": [attended],
            "Total": [total],
            "Remaining": [remaining],
            "Current %": [round(current_percent, 2)]
        })

        print("\nAttendance Analysis:")
        print(df)

    except ValueError:
        print("Please enter valid numbers")
    except:
        print("Something went wrong")