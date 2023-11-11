import os,time

def login(x=0):
    if x == 0:
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username == "TechItAll949" and password == "TSC_INCORP":
                return True
            else:
                print("Invalid username or password. Please try again.")

def main():
    if login(0):
        while True:
            # Ask the user for the command to execute
            command = input("Enter a command (file, database) or 'exit' to quit: ")
            
            # Exit the program if the user types 'exit'
            if command == 'exit':
                break
            
            # Execute the appropriate command based on user input
            if command == 'file':
                while True:
                    file_command = input("Enter a command (dir, create, open, delete) or 'back' to go back: ")
                    if file_command == 'back':
                        break
                    elif file_command == 'dir':
                        directory = input("Enter the directory to list: ")
                        os.system(f"dir {directory}")
                    elif file_command == 'create':
                        filename = input("Enter the filename to create: ")
                        with open(filename, 'w') as f:
                            pass
                    elif file_command == 'open':
                        filename = input("Enter the filename to open: ")
                        os.system(f"start {filename}")
                    elif file_command == 'delete':
                        filename = input("Enter the filename to delete: ")
                        os.remove(filename)
                    else:
                        print("Invalid command. Please try again.")
            elif command == 'database':
                maindatabase = input("Enter the data id locater: ")
                import random

                if maindatabase == "1":
                    from DataBase import CurrentLoggedTVPasswords
                    print("--------------------")
                    print("Current Logged TV Passwords")
                    print("--------------------")
                    print(f"""                 {CurrentLoggedTVPasswords.TVPassword1}
                {CurrentLoggedTVPasswords.TVPassword2}
                {CurrentLoggedTVPasswords.TVPassword3}
                {CurrentLoggedTVPasswords.TVPassword4}
                {CurrentLoggedTVPasswords.TVPassword5}
                {CurrentLoggedTVPasswords.TVPassword6}
                {CurrentLoggedTVPasswords.TVPassword7}
                {CurrentLoggedTVPasswords.TVPassword8}
                {CurrentLoggedTVPasswords.TVPassword9}
                {CurrentLoggedTVPasswords.TVPassword10}
                {CurrentLoggedTVPasswords.TVPassword11}
                {CurrentLoggedTVPasswords.TVPassword12}
                {CurrentLoggedTVPasswords.TVPassword13}
                {CurrentLoggedTVPasswords.TVPassword14}
                {CurrentLoggedTVPasswords.TVPassword15}
                {CurrentLoggedTVPasswords.TVPassword16}
                {CurrentLoggedTVPasswords.TVPassword17}
                {CurrentLoggedTVPasswords.TVPassword18}
                {CurrentLoggedTVPasswords.TVPassword19}
                {CurrentLoggedTVPasswords.TVPassword20}
                """)
                    print("--------------------")
                elif maindatabase == "2":
                    print("--------------------")
                    print(f"""IDENTS""")
                    print("--------------------")
                    print("""Parker: 85jf8v435u34985nbwui23904
                Parker_Old_PC: 08ojgf098id09f9
                Parker_Laptop: 08ojgf098id3224""")
                elif maindatabase == "3":
                    print("--------------------")
                    print(f"""DATABASE 3""")
                    print("--------------------")
                    print(f"""Newly Updated Data VAR 1: {random.randint(1, 100)}
                Newly Updated Data VAR 2: {random.randint(1, 100)}
                Newly Updated Data VAR 3: {random.randint(1, 100)}
                Newly Updated Data VAR 4: {random.randint(1, 100)}
                Newly Updated Data VAR 5: {random.randint(1, 100)}""")
                elif maindatabase == "4":
                    print("--------------------")
                    print(f"""DATABASE 4""")
                    print("--------------------")
                    print(f"""Last Updated Data VAR 1: {random.randint(1, 100)}
                Last Updated Data VAR 2: {random.randint(1, 100)}
                Last Updated Data VAR 3: {random.randint(1, 100)}
                Last Updated Data VAR 4: {random.randint(1, 100)}
                Last Updated Data VAR 5: {random.randint(1, 100)}""")
                else:
                    print("Invalid command. Please try again.")

if __name__ == '__main__':
    main()
