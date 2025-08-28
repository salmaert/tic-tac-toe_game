from Player import Player
from Menu import Menu
from Board import Board
import os

class Game():
    def __init__(self):
        self.players=[Player(),Player()]
        self.board=Board()
        self.menu=Menu()
        self.current_player_index=0

    def start_game(self):
        choice=self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
             self.quit_game()

    def setup_players(self):
        for num,player in enumerate(self.players,start=1):
            print(f"player {num} ,enter your details:")
            player.choose_name()
            player.choose_symbol()
            print("-"*40)

    def play_game(self):
        while True:
            self.play_turn()
            if self.win_check() or self.draw_check():
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def play_turn(self):
        player=self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn {player.symbol}")
        while True:
            try:
                cell = int(input("choose a cell (1-9) : "))
                if 1<=cell<=9 and self.board.update_board(cell,player.symbol):
                    break
                else :
                    print("invalid move,please try again")
            except ValueError:
                print("please enter a number between 1 and 9.")
        self.switch_player()

    def switch_player(self):
        self.current_player_index= 1 - self.current_player_index

    def win_check(self):
        combinations=[
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]

        for combo in combinations :
            if (self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]] ) :
             return True

        return False

    def draw_check(self):
         return all(not cell.isdigit() for cell in self.board.board )

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index()
        self.play_game()

    def quit_game(self):
        print("thank you for playing")

    def clear_screen(self):
        if os.name == "nt":
          os.system("cls")
        else :
          os.system("clear")

