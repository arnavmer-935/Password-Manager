import csv
import os

code = input("Create a passkey to access all other passwords: ")

def changepasskey(code):
    changecount = 0
    while True:
        old = input("Enter your previous passkey: ")
        if old == code:
            new_passkey = input("Enter your new passkey: ")
            code = new_passkey
            print("Passkey changed successfully.")
            return code  # Return the updated passkey
        else:
            print("Previous code does not match entered passkey.")
            changecount += 1
            if changecount <= 10:
                continue
            else:
                break

def insertpasswords():
    with open("passwords.csv", "a", newline='') as f:  # Use append mode 'a'
        w = csv.writer(f)
        while True:
            email = input("Enter the email: ")
            site_usage = input("Enter the site of usage of this password: ")
            psw = input("Enter the password linked to this email: ")
            
            row = [email, psw, site_usage]
            w.writerow(row)
            
            print("Password added successfully.")
            print()
            opt = input("Add another password? (yes/no): ")
            if opt.lower() == "yes" or opt.lower() == "y":
                continue
            else:
                break

def view_all(password, code):
    attempt_count = 0
    while True:
        password = input("Enter password to access stored passwords: ")
        if password == code:
            try:
                with open("passwords.csv", "r") as f:
                    r = csv.reader(f)
                    print("\nStored Passwords:\n")
                    for row in r:
                        print(f"Email: {row[0]}\nPassword: {row[1]}\nSite Usage: {row[2]}\n")
                    print()
            except FileNotFoundError:
                print("No passwords stored yet.")
            return
        else:
            print("Invalid password.")
            attempt_count += 1
            if attempt_count > 5:
                print("Too many failed attempts.")
                break

def edit_psw():
    em = input("Enter the email of the password to edit: ")
    su = input("Enter the site usage: ")
    
    found = False
    updated_rows = []
    
    try:
        with open("passwords.csv", "r") as f:
            r = csv.reader(f)
            for row in r:
                if row[0] == em and row[2] == su:
                    new_psw = input("Enter the new password: ")
                    row[1] = new_psw
                    found = True
                    print("Password updated successfully.")
                updated_rows.append(row)
        
        if not found:
            print("No matching password found.")
        
        with open("passwords.csv", "w", newline='') as f:
            w = csv.writer(f)
            w.writerows(updated_rows)
    except FileNotFoundError:
        print("No passwords stored yet.")

def remove_psw():
    em = input("Enter the email of the password to be removed: ")
    su = input("Enter the site usage: ")
    
    found = False
    updated_rows = []
    
    try:
        with open("passwords.csv", "r") as f:
            r = csv.reader(f)
            for row in r:
                if row[0] != em or row[2] != su:
                    updated_rows.append(row)
                else:
                    found = True
                    print("Password removed successfully.")
        
        if not found:
            print("No matching password found.")
        
        with open("passwords.csv", "w", newline='') as f:
            w = csv.writer(f)
            w.writerows(updated_rows)
            
    except FileNotFoundError:
        print("No passwords stored yet.")

while True:
    print("Press 1 to change your passkey.")
    print("Press 2 to add any password(s).")
    print("Press 3 to view all stored passwords.")
    print("Press 4 to edit any password.")
    print("Press 5 to remove any password's details.")
    print("Press 6 to exit.")
    print()
    
    try:
        ch = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please enter a number.")
        continue
    
    if ch == 1:
        code = changepasskey(code)
    elif ch == 2:
        insertpasswords()
    elif ch == 3:
        view_all(code, code)
    elif ch == 4:
        edit_psw()
    elif ch == 5:
        remove_psw()
    elif ch == 6:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
