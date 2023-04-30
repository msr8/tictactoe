from rich import inspect
import time as t


class TicTacToe:
    def __init__(self, turn):
        self.board = [None] * 9
        self.turn  = turn


    def val(self, value):
        return value if value else ' '

    def get_empty_cells(self, board=None) -> list[dict]:
        board = self.board if not board else board
        cells = []
        for n,cell in enumerate(board):
            if not cell:
                cells.append(n)
        
        return cells

    def get_state(self, board=None):
        """
        None: Game isnt over
        0:    Tie
        1:    X won
        -1:   O won
        """
        win_states = [
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]
        ]
        b = self.board if not board else board

        # Check if someone won
        for c1,c2,c3 in win_states:
            if (b[c1]==b[c2] and b[c2]==b[c3] and b[c1]!=None):
                return 1 if b[c1]=='X' else -1
        # Else, check if its a tie
        if not None in b:
            return 0
        # Else, returns None
        return None



    def get_best_possible_move(self, board=None, turn=None):
        board = board
        turn  = self.turn  if not turn  else turn
        state = self.get_state(board)
        print(f'[B] {board} {turn}')
        # t.sleep(1)

        # Checks if the game has ended. If it has, return its value
        if state!=None:
            return state
        
        # If the game has not ended, it will try to get the states of child branches
        cells = self.get_empty_cells(board)
        # If it is X's (aka max) turn
        if turn == 'X':
            value = -2
            for cell in cells:
                # Simulate every possible move
                b2 = board.copy()
                b2[cell] = 'X'
                turn = 'O'
                print(f'[A] {b2} {turn} {cell} {cells}')
                value = max(value, self.get_best_possible_move(b2, turn))
        else:
            value = 2
            for cell in cells:
                # Simulate every possible move
                b2 = board.copy()
                b2[cell] = 'O'
                turn = 'X'
                print(f'[A] {b2} {turn} {cell} {cells}')
                value = min(value, self.get_best_possible_move(b2, turn))
        
        return value



            
            




    def print_board(self):
        board = self.board
        val   = self.val
        print(f'{val(board[0])} | {val(board[1])} | {val(board[2])}')
        print('---------')
        print(f'{val(board[3])} | {val(board[4])} | {val(board[5])}')
        print('---------')
        print(f'{val(board[6])} | {val(board[7])} | {val(board[8])}')
        print(f'({self.get_state()}) | {self.get_empty_cells()} | {self.get_best_possible_move(self.board)}')
        print('\n\n')

    def play(self, cell:int):
        player = self.turn
        # Checks if its a possible move
        if not cell in self.get_empty_cells():
            raise Exception('Move not possible')
        # If it is, plays it and gives the turn to the other player
        else:
            self.board[cell] = player
            self.turn = 'O' if self.turn=='X' else 'X'







board = TicTacToe('X')
board.board = ['X','O','X','O','O','X',None,None,None]
# board.board = [None] * 9
# board.board[0] = 'X'
print(board.turn)
board.print_board()

