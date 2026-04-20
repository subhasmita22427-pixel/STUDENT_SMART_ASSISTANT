file = "data/marks.txt"


# ---------------- ADD MARKS ----------------
def add_marks():
    try:
        subject = input("Enter subject: ")
        internal = int(input("Enter internal marks: "))
        mid = int(input("Enter mid marks: "))
        end = int(input("Enter end marks: "))

        # tuple used
        marks = (internal, mid, end)

        f = open(file, "a")
        f.write(subject + "," + str(marks[0]) + "," + str(marks[1]) + "," + str(marks[2]) + "\n")
        f.close()

        print("Marks added")

    except:
        print("Invalid input")


# ---------------- VIEW MARKS ----------------
def view_marks():
    try:
        f = open(file, "r")
        data = f.readlines()
        f.close()

        if len(data) == 0:
            print("No marks found")
            return

        print("\nMarks:")

        for line in data:
            parts = line.strip().split(",")

            if len(parts) == 4:
                subject = parts[0]
                internal = int(parts[1])
                mid = int(parts[2])
                end = int(parts[3])

                total = internal + mid + end

                print("Subject:", subject,
                      "| Total:", total)

    except:
        print("Error reading marks")


# ---------------- CHECK FAIL ----------------
def check_fail():
    try:
        f = open(file, "r")
        data = f.readlines()
        f.close()

        if len(data) == 0:
            print("No marks data found")
            return

        failed_subjects = set()   # set used

        for line in data:
            parts = line.strip().split(",")

            if len(parts) == 4:
                subject = parts[0]
                internal = int(parts[1])
                mid = int(parts[2])
                end = int(parts[3])

                total = internal + mid + end

                if total < 35:
                    failed_subjects.add(subject)

        print("\nFailed Subjects:")

        if len(failed_subjects) == 0:
            print("None")
        else:
            for sub in failed_subjects:
                print(sub)

    except:
        print("Error checking results")


# ---------------- ANALYZE MARKS ----------------
def analyze_marks():
    try:
        f = open(file, "r")
        data = f.readlines()
        f.close()

        if len(data) == 0:
            print("No marks data found")
            return

        total_marks = 0
        count = 0

        for line in data:
            parts = line.strip().split(",")

            if len(parts) == 4:
                internal = int(parts[1])
                mid = int(parts[2])
                end = int(parts[3])

                total = internal + mid + end

                total_marks += total
                count += 1

        avg = total_marks / count

        print("\nAverage Marks:", avg)

    except:
        print("Error analyzing marks")