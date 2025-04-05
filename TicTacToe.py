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
            for move in 


#if __name__ == "__main__":
#    game = TicTacToe()
#    game.make_move(5, "John")
#    game.print_board()
#    print(game.available_moves())
