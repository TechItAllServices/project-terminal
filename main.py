import os

def main():
    while True:
        # Ask the user for the command to execute
        command = input("Enter a command (dir, create, open, delete) or 'exit' to quit: ")
        
        # Exit the program if the user types 'exit'
        if command == 'exit':
            break
        
        # Execute the appropriate command based on user input
        if command == 'dir':
            directory = input("Enter the directory to list: ")
            os.system(f"dir {directory}")
        elif command == 'create':
            filename = input("Enter the filename to create: ")
            with open(filename, 'w') as f:
                pass
        elif command == 'open':
            filename = input("Enter the filename to open: ")
            os.system(f"start {filename}")
        elif command == 'delete':
            filename = input("Enter the filename to delete: ")
            os.remove(filename)
        else:
            print("Invalid command. Please try again.")

if __name__ == '__main__':
    main()
