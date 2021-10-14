from board import *
from piece import *
from dice import *
from player import *
import random

dices = Dices(4)
board = Board()

player1 = Player('A','David')
player2 = Player('B','Albert')

def new_game():
	board.reset()
	player1.reset()
	player2.reset()

	game_over = False
	max_num_turns = 100
	num_turns = 0

	while num_turns<max_num_turns:
		game_over = turn(player1)
		if game_over:
			return player1.player
		game_over = turn(player2)
		if game_over:
			return player2.player
		num_turns+=1
	return None


def turn(player):
	dice_result = dices.roll()
	player_possible_moves = player.possible_moves(board, dice_result)
	"""
	print("------- PLAYER ",player.player, " TURN ------")
	print("Player possible moves",player_possible_moves)
	print(board)
	print("Dice result: ",dice_result, player.player," moving")
	"""
	if not player_possible_moves:
		return False

	player_move = random.choice(player_possible_moves)
	player.pieces[player_move].move_piece(dice_result, board.squares)

	result = []
	for piece in player.pieces:
		result.append(piece.completed)

	if all(result):
		return True

	return False

num_turns = 100
num_games = 10
num_turns_counter = 0
avg_num_turns = 0

for game in range(num_games):
	winner = new_game()
	print(winner)
	if winner==player1.player:
		player1.wins+=1
	elif winner==player2.player:
		player2.wins+=1

print("Player A won ",player1.wins," games")
print("Player B won ",player2.wins," games")

print(board)

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