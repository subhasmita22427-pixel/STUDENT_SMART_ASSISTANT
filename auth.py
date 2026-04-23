"""
program summary:
* handles user security through the 'authmanager' class for signup and login.
* custom validation: uses a helper method with regex to enforce specific password rules (length and character types).
* data storage: uses standard python file handling to append new user strings to a text file.
* authentication: implements a simple loop to read the database and compare input credentials against stored records.
* error handling: manages missing file errors and generic exceptions to keep the program running smoothly.
"""

import re

class AuthManager:
    def __init__(self):
        # Centralizing the user database file path
        self.file = "data/users.txt"

    # password check (Internal helper method)
    def check_password(self, p):
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
    def signup(self):
        try:
            name = input("Enter name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")

            # email check using regex
            if not re.search("@", email):
                print("Invalid email")
                return

            # password complexity check
            if not self.check_password(password):
                print("Password should have capital, small, number and special char")
                return

            f = open(self.file, "a")
            f.write(name + "," + email + "," + password + "\n")
            f.close()

            print("Signup done")

        except:
            print("Error in signup")


    # login
    def login(self):
        try:
            email = input("Enter email: ")
            password = input("Enter password: ")

            f = open(self.file, "r")
            data = f.readlines()
            f.close()

            for line in data:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    u_name, u_email, u_pw = parts[0], parts[1], parts[2]

                    if u_email == email and u_pw == password:
                        print("Login success, Welcome", u_name)
                        return True
            
            # If loop finishes without returning True
            print("Invalid email or password")
            return False

        except FileNotFoundError:
            print("No user found, please signup first")
            return False
        except:
            print("Error in login")
            return False
