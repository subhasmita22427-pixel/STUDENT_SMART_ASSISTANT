"""
program summary:
* managed dual-track academic progress for 'college' and 'self-study' courses within the 'syllabusmanager' class.
* data categorization: introduces a 'type' attribute to distinguish between institutional coursework and personal learning.
* add_topic(): uses conditional logic (if/else) to tag new entries based on user selection.
* view_progress(): 
    - implements pandas boolean indexing (filtering) to split the master dataframe into two distinct tables.
    - calculates independent progress percentages for both categories.
* user interface: organizes output using visual separators to clarify the distinction between different course types.
"""

import pandas as pd

class syllabusmanager:
    def __init__(self):
        # path to our syllabus csv file
        self.file = "data/syllabus.csv"

    # function to add new topics
    def add_topic(self):
        try:
            print("\nselect type: 1. college | 2. self-study")
            choice = input("choice: ")
            # simple if/else for course type
            course_type = "self" if choice == "2" else "college"
            
            subject = input("subject name: ")
            topic = input("topic name: ")

            # dictionary to structure new data
            new_row = {
                "type": course_type,
                "subject": subject,
                "topic": topic,
                "status": "pending"
            }

            try:
                # opening the existing data file
                df = pd.read_csv(self.file)
            except:
                # creating headers if file missing
                df = pd.DataFrame(columns=["type", "subject", "topic", "status"])

            # combining new row with existing table
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv(self.file, index=False)

            print(f"saved to {course_type} list")

        except:
            print("error: could not save topic")

    # function to finish a topic
    def mark_done(self):
        try:
            df = pd.read_csv(self.file)
            if df.empty:
                print("list is empty")
                return

            print("\n--- current syllabus ---")
            print(df[["type", "subject", "topic", "status"]])
            
            idx = int(input("\nenter index number to finish: "))

            if 0 <= idx < len(df):
                # .at updates a single cell
                df.at[idx, "status"] = "done"
                df.to_csv(self.file, index=False)
                print("topic marked as completed")
            else:
                print("invalid index number")

        except:
            print("error updating the topic")

    # viewing progress with two tables
    def view_progress(self):
        try:
            df = pd.read_csv(self.file)
            if df.empty:
                print("no data found")
                return

            # filtering: splitting table by type
            college_df = df[df["type"] == "college"]
            self_df = df[df["type"] == "self"]

            print("\n--- college syllabus ---")
            if college_df.empty:
                print("no college topics found")
            else:
                print(college_df[["subject", "topic", "status"]].to_string(index=False))
                # calculating progress percentage manually
                done = len(college_df[college_df["status"] == "done"])
                print(f"college progress: {(done/len(college_df))*100:.2f}%")

            print("\n--- self-study syllabus ---")
            if self_df.empty:
                print("no self-study topics found")
            else:
                print(self_df[["subject", "topic", "status"]].to_string(index=False))
                # using len for percentage math
                s_done = len(self_df[self_df["status"] == "done"])
                print(f"self-study progress: {(s_done/len(self_df))*100:.2f}%")

        except:
            print("error loading the progress")