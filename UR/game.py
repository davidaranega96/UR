from board import *
from player import *
from dice import *
from piece import *
import random

class Game():
	def __init__(self):
		self.player1 = Player("A", "Player 1")
		self.player2 = player("B", "Player 2")
		self.board = Board()
		self.dices = Dices(4)
		self.max_turns = 100

	def __str__(self):
		print("The current board:")
		print(self.board)
		print("Player 1 has ", self.player1.score, " points.")
		print("Player 2 has ", self.player2.score, " points.")

	def turn(self, player):
		dices_result = self.dices.roll()											#rolling dices
		player_possible_moves = player.possible_moves(board, dice_result)			#Selecting move
		if not player_possible_moves:
			return False
		player_move = random.choice(player_possible_moves)
		player.move_piece(player_move, dice_result, self.board)

		#------Checking if the player has won------------
		result = []
		for piece in player.pieces:
			result.append(piece.completed)
		if all(result):
			return True
		return False

	def run(self):
		turn = 0
		player = self.player1
		while turn<=self.max_turns:
			over = self.turn(player)
			if over:
				return player
			if player.player=='A':
				player = self.player2
			elif player.player=='B':
				player = self.player1
			turn += 1
		return "ERROR!"


	def reset(self):
		self.board = self.board.reset()
		self.player1 = self.player1.reset()
		self.player2 = self.player2.reset()

	partida = Game()
	ganador = partida.run()
	print(partida)
