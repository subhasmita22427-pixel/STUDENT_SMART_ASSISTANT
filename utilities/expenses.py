"""
program summary:
* manages financial tracking through the 'expensemanager' class for spending and investments.
* data expansion: captures 'type' and 'source' to provide better financial insights.
* dictionary usage: uses python dictionaries to structure input before saving to the file.
* file handling: saves data in 'data/expenses.txt' using a simple comma-separated format.
* analytics: calculates grand totals and creates a category-wise summary using dictionaries.
* oop design: wraps all logic inside a class so it can be called easily from the main menu.
"""

class expensemanager:
    def __init__(self):
        # setting the path for data storage
        self.file = "data/expenses.txt"

    # function to add new records
    def add_expense(self):
        try:
            category = input("enter category (food/travel/etc): ")
            amount = float(input("enter amount: "))
            date = input("enter date (dd-mm-yyyy): ")
            
            # asking for spending type
            print("type: 1. spend | 2. investment")
            t_choice = input("choice: ")
            e_type = "investment" if t_choice == "2" else "spend"
            
            # asking for money source
            print("source: 1. parents | 2. self-earned")
            s_choice = input("choice: ")
            source = "self-earned" if s_choice == "2" else "parents"

            # temporary dictionary to organize data
            expense = {
                "cat": category,
                "amt": amount,
                "date": date,
                "type": e_type,
                "src": source
            }

            # opening file to append data
            f = open(self.file, "a")
            # writing as comma separated values
            f.write(f"{expense['cat']},{expense['amt']},{expense['date']},{expense['type']},{expense['src']}\n")
            f.close()

            print("expense recorded successfully")

        except ValueError:
            print("error: please enter a number")
        except:
            print("something went wrong")

    # function to see all history
    def view_expenses(self):
        try:
            # reading the full text file
            f = open(self.file, "r")
            data = f.readlines()
            f.close()

            if not data:
                print("no data found")
                return

            print("\n--- expense log ---")
            total = 0
            # dictionary for group-wise totals
            summary = {}

            for line in data:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    cat, amt, dt, etype, src = parts[0], float(parts[1]), parts[2], parts[3], parts[4]
                    
                    # adding to the grand total
                    total += amt
                    print(f"[{dt}] {cat}: {amt} ({etype})")

                    # adding to category specific total
                    summary[cat] = summary.get(cat, 0) + amt

            print("-" * 25)
            print(f"total spent: {total}")
            
            print("\nbreakdown by category:")
            for cat, amt in summary.items():
                print(f"- {cat}: {amt}")

        except FileNotFoundError:
            print("no file exists yet")
        except:
            print("error loading the data")