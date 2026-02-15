from menu import Menu, run_bash_cmd


def main():
    menu = Menu()

    menu.addOption("Show Available Memory")
    menu.addOption("Show Current Network Connections")
    menu.addOption("Show Available File Space")

    running = True

    while running:
        choice = menu.getInput()

        if choice == 4:
            print("Exiting program...")
            running = False
        else:
            run_bash_cmd(choice)


if __name__ == "__main__":
    main()
