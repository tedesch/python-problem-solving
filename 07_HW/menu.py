import os

# refactored run_bash_cmd
def run_bash_cmd(some_choice):

    print('-' * 80, '\n')
    print('You entered #', some_choice)

    commands = {
        1: ("The available memory is ",
            "free -tmh"),

        2: ("The current network connections include: ",
            "netstat -an | grep -i Estab | cut -d ':' -f 2,3 | gawk '{print $2}' | grep [0-9] | uniq"),

        3: ("Available file space is: ",
            'df -h | grep "Filesystem\\|root"')
    }

    selected = commands.get(some_choice)

    if selected:
        message, command = selected
        print(message)
        os.system(command)
    else:
        print("Invalid selection.")

# Menu system for Linux utilities.
class Menu:

    def __init__(self):
        self._options = []

    def addOption(self, option):
        self._options.append(option)

    def displayMenu(self):

        for i, option in enumerate(self._options, start=1):
            print(f"{i}. {option}")

        print("4. Quit")

    def getInput(self):
        while True:
            self.displayMenu()
            user_input = input("Enter choice (1-4 or Q to quit): ")

            if user_input.lower() == "q":
                return 4

            if user_input.isdigit():
                choice = int(user_input)
                if 1 <= choice <= 4:
                    return choice

            print("Invalid input. Please enter 1-4 or Q.")
