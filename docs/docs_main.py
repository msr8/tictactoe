import time as t
import random as r

import json


class TicTacToe:
    def __init__(self, turn, cache:dict={}):
        self.board = [None] * 9
        self.turn  = turn
        self.cache = cache.copy()


    def val(self, value):
        return value if value else ' '

    def get_board_string(self, board:list=None, turn:str=None):
        board = self.board if not board else board
        turn  = self.turn  if not turn  else turn
        # print(f'Inside the func, {board}')
        string  = ''.join([str(i) for i in board])
        string  = string.replace('None','-')
        string += turn
        return string

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



    def minimax(self, board=None, turn=None, return_all:bool=False):
        """
        Returns the minimax score of a given board state
        -1: O wins
        0:  Tie
        1:  X wins

        :param return_all: A boolean parameter that determines whether the function should return all
        the minimax values of the possible moves or just the best one. If set to True, the function
        returns a dictionary of all the minimax values with the corresponding cell as the key. If set to
        False, the function returns only the best, defaults to False
        :type return_all: bool (optional)
        """
        board = self.board if not board else board
        turn  = self.turn  if not turn  else turn
        cache = self.cache

        # Checks cache
        if not return_all:
            string = self.get_board_string(board, turn)
            val    = cache.get(string)
            # print(f'{string} | {turn} | {val}')
            if val!=None:   return val
            # print(f'Cache not found for {string} | {board} {turn} cache.get("{string}"): {val} ({cache.get(string)})')
            # with open('cache2.json','w') as f:
            #     json.dump(cache, f, indent=4)
        
        # Checks if the game has ended. If it has, return its value
        state = self.get_state(board)
        if state!=None:
            return state


        # Gets all empty cells in a board
        cells = self.get_empty_cells(board)
        # Simulates all possible moves and notes the minimax values of the boards resulting from said move
        values = {}
        for cell in cells:
            # Makes a copy of the current board and simulates the move
            b2 = board.copy()
            b2[cell] = turn
            # Swaps the turn/player
            new_turn = 'O' if turn=='X' else 'X'
            # print(f'[A] {b2} {new_turn} {cell} {cells}')
            # Notes the minimax value of board resulting from that move
            minimax_score = self.minimax(b2, new_turn)
            values[cell] = minimax_score
        
        # If the user wants all the values of the possible moves
        if return_all:
            # print(f'{board} ({turn}) | {values}')
            return values

        # X is max, O is min
        func          = max if turn=='X' else min
        minimax_score = func(values.values())

        # # Gets a string format of the board
        # string = self.get_board_string()
        # # Adds the result to cache
        # cache[string] = minimax_score

        return minimax_score
    

    def get_best_move(self):
        turn = self.turn

        # Gets the minimax score that all the moves result in
        all_moves:dict = self.minimax(return_all=True)
        # Gets the best possible score
        func       = max if turn=='X' else min
        best_score = func(all_moves.values())
        # Gets the moves that result in that value
        best_moves = [key for key in all_moves if all_moves[key]==best_score]
        # Selects a random move from that and returns it
        return r.choice(best_moves)

    def play_best_move(self):
        # Plays the best move
        self.play(self.get_best_move())



    def print_board(self):
        board = self.board
        val   = self.val
        print(f'{val(board[0])} | {val(board[1])} | {val(board[2])}')
        print('---------')
        print(f'{val(board[3])} | {val(board[4])} | {val(board[5])}')
        print('---------')
        print(f'{val(board[6])} | {val(board[7])} | {val(board[8])}')
        # print(f'({self.get_state()}) | {self.get_empty_cells()} | {self.minimax(self.board)}')
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



