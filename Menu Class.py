class Menu:
    def display_main_menu(self):
        while True:
            print("welcome to X&0 Game:")
            print("1. start the game")
            print("2. quit the game")
            choice = input("please enter your choice (1 or 2) : ")
            if choice == "1" or choice == "2":
                break
            else:
                print("please enter 1 or 2")
        return choice

    def display_endgame_menu(self):
        while True:
            menu_text = """Game over  :
        1.restart the game
        2.quit the game     
        """
            print(menu_text)
            choice = input("please enter your choice (1 or 2):")
            if choice == "1" or choice == "2":
                break
            print("please enter 1 or 2 :")
        return choice
