file = "data/expenses.txt"


# add expense
def add_expense():
    try:
        category = input("Enter category (food/travel/etc): ")
        amount = float(input("Enter amount: "))
        date = input("Enter date: ")

        #dictinary
        expense = {
            "category": category,
            "amount": amount,
            "date": date
        }

        f = open(file, "a")
        f.write(expense["category"] + "," + str(expense["amount"]) + "," + expense["date"] + "\n")
        f.close()

        print("Expense added")

    except:
        print("Invalid input")


# view all expenses
def view_expenses():
    try:
        f = open(file, "r")
        data = f.readlines()
        f.close()

        if len(data) == 0:
            print("No expenses found")
            return

        print("\nExpenses:")
        total = 0

      
        summary = {}

        for line in data:
            parts = line.strip().split(",")

            if len(parts) == 3:
                expense = {
                    "category": parts[0],
                    "amount": float(parts[1]),
                    "date": parts[2]
                }

                total += expense["amount"]

                print("Category:", expense["category"],
                      "| Amount:", expense["amount"],
                      "| Date:", expense["date"])

                
                if expense["category"] in summary:
                    summary[expense["category"]] += expense["amount"]
                else:
                    summary[expense["category"]] = expense["amount"]

        print("Total Expense:", total)

        print("\nCategory-wise Summary:")
        for cat in summary:
            print(cat, ":", summary[cat])

    except:
        print("Error reading expenses")