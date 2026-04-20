import pandas as pd

file = "data/syllabus.csv"


# add topic
def add_topic():
    try:
        subject = input("Enter subject: ")
        topic = input("Enter topic: ")

        new_data = {
            "Subject": subject,
            "Topic": topic,
            "Status": "Pending"
        }

        try:
            df = pd.read_csv(file)
        except:
            df = pd.DataFrame(columns=["Subject", "Topic", "Status"])

        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

        df.to_csv(file, index=False)

        print("Topic added")

    except:
        print("Error adding topic")


# mark topic complete
def mark_done():
    try:
        df = pd.read_csv(file)

        if df.empty:
            print("No topics found")
            return

        print(df)

        n = int(input("Enter topic number to mark complete: "))

        if n < 1 or n > len(df):
            print("Invalid choice")
            return

        df.at[n-1, "Status"] = "Done"

        df.to_csv(file, index=False)

        print("Topic marked as complete")

    except Exception as e:
        print("Error updating topic:", e)


# view progress
def view_progress():
    try:
        df = pd.read_csv(file)

        if df.empty:
            print("No topics found")
            return

        print("\nSyllabus:")
        print(df)

       
        subjects = set(df["Subject"])    #set

        total = len(df)
        done = len(df[df["Status"] == "Done"])

        percent = (done / total) * 100

        print("\nUnique Subjects:", subjects)

        print("Progress: {:.2f}%".format(percent))

    except:
        print("Error reading syllabus")