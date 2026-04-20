import re

file = "data/users.txt"

# password check
def check_password(p):
    if len(p) < 6:
        return False
    if not re.search("[A-Z]", p):
        return False
    if not re.search("[a-z]", p):
        return False
    if not re.search("[0-9]", p):
        return False
    if not re.search("[@#$%]", p):
        return False
    return True


# signup
def signup():
    try:
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")

        # email check
        if not re.search("@", email):
            print("Invalid email")
            return

        # password check
        if not check_password(password):
            print("Password should have capital, small, number and special char")
            return

        f = open(file, "a")
        f.write(name + "," + email + "," + password + "\n")
        f.close()

        print("Signup done")

    except:
        print("Error in signup")


# login
def login():
    try:
        email = input("Enter email: ")
        password = input("Enter password: ")

        f = open(file, "r")
        data = f.readlines()
        f.close()

        for line in data:
            parts = line.strip().split(",")
            if len(parts) == 3:
                name = parts[0]
                em = parts[1]
                pw = parts[2]

                if em == email and pw == password:
                    print("Login success, Welcome", name)
                    return True
                elif email == "" or password == "":
                    print("Fields cannot be empty")
                else:
                    print("Wrong email or password")

        return False

    except FileNotFoundError:
        print("No user found, please signup first")
        return False

    except:
        print("Error in login")
        return False
    
#I used file handling to store users and regex to check password strength.
#Then I used loop to match login credentials.”
# used try execption , function , if else 

