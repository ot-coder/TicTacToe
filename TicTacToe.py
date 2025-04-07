class TicTacToe:
    def __init__(self) -> None:
        self.board = [" " for _ in range(9)]
        self.human = "O"
        self.ai = "X"

    def print_board(self) -> None:
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i +1]} | {self.board[i + 2]}")
            if i < 6:
                print("----------")

    def available_moves(self):
       return [i for i, spot in enumerate(self.board) if spot == " "]

    def make_move(self, position, player) -> None:
        if self.board[position] == " ":
            self.board[position] = player
            return True
        return False
    
    def isBoard_Full(self):
        return " " not in self.board
    
    def check_winner(self):
       # Check rows
       for i in range(0, 9, 3):
           if self.board[i] == self.board[i + 1] == self.board[i + 2] != " ":
               return self.board[i]

       # Check columns
       for i in range(3):
           if self.board[i] == self.board[i + 3] == self.board[i + 6] != " ":
               return self.board[i]

       # Check diagonals
       if self.board[0] == self.board[4] == self.board[8] != " ":
           return self.board[0]
       if self.board[2] == self.board[4] == self.board[6] != " ":
           return self.board[2]

       return None
    
    def game_over(self):
        if self.check_winner() or self.isBoard_Full():
            return True
        return False
    
    def minimax(self, depth, is_maximizing):
        winner = self.check_winner()

        if winner == self.ai:
            return 1
        if winner == self.human:
            return -1
        if self.isBoard_Full():
            return 0
        
        if is_maximizing:
            best_score = float("-inf")
            for move in self.available_moves():
                self.board[move] = self.ai

                score = self.minimax(depth + 1, False)
                self.board[move] = " "
                best_score = max(score, best_score)
            return best_score
        
        else:
            best_score = float("inf")
            for move in self.available_moves():
                self.board[move] = self.human

                score = self.minimax(depth + 1, True)
                self.board[move] = " "
                best_score = min(score, best_score)
            return best_score
        

    def best_move(self):
        best_score = float("-inf")
        best_move = None

        for move in self.available_moves():
            self.board[move] = self.ai
            score = self.minimax(0, False)
            self.board[move] = " "

            if score > best_score:
                best_score = score
                best_move = move
            
        return best_move
    
    def play_game(self):
        print("Hey, are you ready to lose TicTacToe!!!")
        print("You are O and the AI is X")
        print("Find below the marked positions")
        print("0 | 1 | 2")
        print("3 | 4 | 5")
        print("6 | 7 | 8")
        print("\n")

        import random

        ai_turn = random.choice([True, False])

        while not self.game_over():
            self.print_board()

            if ai_turn:
                print("\nThinking...")
                move = self.best_move()
                self.make_move(move, self.ai)
            else:
                while True:
                    try:
                        move = int(input("\nYour move: "))
                        if 0 <= move <= 8 and self.make_move(move, self.human):
                            break
                        else:
                            print("Invalid position")
                    except ValueError:
                        print("Enter a number position between 0 and 8!")
            
            ai_turn = not ai_turn

        self.print_board()
        winner = self.check_winner()
        if winner == self.ai:
            print("HAHA!!! I win")
        elif winner == self.human:
            print("You've succeeded... for now")
        else:
            print("Guess its just a tie")
            

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()