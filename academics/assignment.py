file = "data/assignments.txt"


# add assignment
def add_assignment():
    try:
        subject = input("Enter subject: ")
        name = input("Enter assignment name: ")
        deadline = input("Enter deadline: ")

        #  list 
        assignment = [subject, name, deadline, "Pending"]

        f = open(file, "a")
        f.write(",".join(assignment) + "\n")
        f.close()

        print("Assignment added")

    except:
        print("Error adding assignment")


# view assignments
def view_assignments():
    try:
        f = open(file, "r")
        data = f.readlines()
        f.close()

        if len(data) == 0:
            print("No assignments found")
            return

        print("\nAssignments:")

        assignments_list = []   #  list of assignments

        for line in data:
            parts = line.strip().split(",")

            if len(parts) == 4:
                assignments_list.append(parts)

        for a in assignments_list:
            print("Subject:", a[0],
                  "| Name:", a[1],
                  "| Deadline:", a[2],
                  "| Status:", a[3])

    except:
        print("Error reading assignments")


# mark complete
def mark_complete():
    try:
        f = open(file, "r")
        data = f.readlines()
        f.close()

        if len(data) == 0:
            print("No assignments found")
            return

        assignments_list = []

        # convert file data to list
        for line in data:
            parts = line.strip().split(",")
            if len(parts) == 4:
                assignments_list.append(parts)

        # show list
        for i in range(len(assignments_list)):
            print(i+1, assignments_list[i])

        n = int(input("Enter assignment number to mark complete: "))

        if n < 1 or n > len(assignments_list):
            print("Invalid choice")
            return

        # update list
        assignments_list[n-1][3] = "Done"

        # rewrite file
        f = open(file, "w")
        for a in assignments_list:
            f.write(",".join(a) + "\n")
        f.close()

        print("Assignment marked as complete")

    except Exception as e:
        print("Error updating assignment:", e)