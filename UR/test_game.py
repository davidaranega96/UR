from board import *
from piece import *
from dice import *
from player import *
import random

dices = Dices(4)
board = Board()

player1 = Player('A','David')
player2 = Player('B','Albert')	

dice_result = dices.roll()
player1_moves = player1.possible_moves(board, dice_result)
print(player1_moves)
player1_move = random.choice(player1_moves)

dice_result = dices.roll()
player2_moves = player2.possible_moves(board, dice_result)
player2_move = random.choice(player2_moves)
"""
for piece in player1.pieces:
	print(piece)

result = dices.roll()
print("Player 1 moving the piece")
player1.pieces[0].move_piece(5, board.squares)

for piece in player1.pieces:
	print(piece)
print("Player 2 moving the piece")
player2.pieces[0].move_piece(5, board.squares)

for piece in player2.pieces:
	print(piece)

for piece in player1.pieces:
	print(piece)

"""