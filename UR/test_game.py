from board import *
from piece import *
from dice import *
from player import *
import random

dices = Dices(4)
board = Board()

player1 = Player('A', 'David')
player2 = Player('B', 'Albert')


def new_game():
	board.reset()
	player1.reset()
	player2.reset()

	game_over = False
	max_num_turns = 100
	num_turns = 0

	while num_turns < max_num_turns:
		game_over = turn(player1)
		
		if game_over:
			"""
			print(board.get_board_state())
			print("Player 1 state", player1.get_player_state())
			print("Player 2 state", player2.get_player_state())
			"""
			return player1.player

		game_over = turn(player2)
		if game_over:
			"""
			print(board.get_board_state())
			print("Player 1 state", player1.get_player_state())
			print("Player 2 state", player2.get_player_state())
			"""
			return player2.player
		num_turns+=1

	return None


def turn(player):
	dice_result = dices.roll()
	player_possible_moves = player.possible_moves(board, dice_result)
	if not player_possible_moves:
		return False

	player_move = random.choice(player_possible_moves)
	player.score += player.move_piece(player_move, dice_result, board)

	result = []
	for piece in player.pieces:
		result.append(piece.completed)

	if all(result):
		return True

	return False

num_turns = 5
num_games = 100
num_turns_counter = 0
avg_num_turns = 0

for game in range(num_games):
	winner = new_game()
	if winner==player1.player:
		player1.wins+=1
		print(winner)
	elif winner==player2.player:
		player2.wins+=1
		print(winner)

print("Player A won ",player1.wins," games")
print("Player B won ",player2.wins," games")

print(board)





