# FILE TO DEAL WITH CACHING STUFF
from main import TicTacToe
import json
from itertools import product
from tqdm import tqdm


# with open('cache.json', r) as f:
#     cache = json.load(f)


cache = {}
combinations = product(['X','O',None], repeat=9)
combinations = [list(i) for i in combinations]
# print(len(combinations))
# print(type(combinations))



valid_combinations = []
for board in tqdm(combinations):
    board:list = board

    # Checks if the difference between number of X's and O's is not 2 or more
    no_x = board.count('X')
    no_o = board.count('O')
    if abs(no_x - no_o) >= 2:
        continue

    # Calculates whose turn it can be
    if   no_x == no_o:   turns = ['X','O']
    elif no_x > no_o:    turns = ['O']
    elif no_o > no_x:    turns = ['X']

    # For every move, checks its minimax score
    for turn in turns:
        game          = TicTacToe(turn)
        game.board    = board.copy()
        minimax_score = game.minimax()
        string        = game.get_board_string()
        # print(f'{string} | {board} | {turn} | {minimax_score}')
        cache[string] = minimax_score
        # print(string)

# game = TicTacToe('O')
# game.board = [None, 'X', 'X', None, None, None, None, 'O', None]
# print(f'{game.minimax(return_all=True)} |  {game.get_board_string()} | {game.minimax()} | {game.minimax(return_all=True)}')

# game.print_board()
# game.play_best_move()
# game.print_board()

with open('cache.json', 'w') as f:
    json.dump(cache, f, indent=4)

'''
 - X X
 - - -
 - O -

O
'''

# game = TicTacToe('X', cache)
# game.play_best_move()
# game.board = [None] * 9
# game.turn  = 'O'
# game.play_best_move()




    









'''
The limits are:

-> 3 possible values at the first 9 characters (0,X,-), and two combinations in the last character (X,O)
-> Max difference between number of X's and O's is 1
-> if   n(x) == n(O):   player can be X or O
   elif n(x) > n(O):    player = O
   else:                player = X
-> The board cannot be at a terminal state (is handled by the internal minimax function, but still be careful)



X-X--O--OX SHOULD BE 1, not -1!!
 X - X
 - - O
 - - O
X
'''



