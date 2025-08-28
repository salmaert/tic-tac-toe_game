class Player:
    def __init__(self):
        self.name=""
        self.symbol=""


    def choose_name(self):
        while True:
         name=input("Please enter your name :(only letters) : ")
         if name.isalpha():
            self.name=name
            break
         print("invalide name.please use letters only!")

    def choose_symbol(self):
        while True:
         symbol=input("Please enter your symbol :(a single letter) : ")
         if symbol.isalpha() & len(symbol) == 1:
            self.symbol=symbol
            break
         print("invalide symbol.please use letters only!")

