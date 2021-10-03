from piece import *
import configparser
import json

parser = configparser.ConfigParser()
parser.read("config.ini")
list_shared_squares = parser.get("ur_squares", "shared_squares")
list_shared_squares = json.loads(list_shared_squares)

class Player():
	def __init__(self, player, name):
		self.player = player #Either player 1 or player 2
		self.name = name
		self.score = 0
		self.pieces = [Piece(player) for i in range(6)]

	def possible_moves(self, board, dice_result):
		pieces = [i for i in self.pieces if i.completed == False]
		possible_moves = []
		for piece in pieces:
			if self.check_move_possible(board, piece, dice_result):
				possible_moves.append(piece)
		return possible_moves

	def check_move_possible(self, board, piece, dice_result):
		squares = board.squares
		if dice_result == 0:
			return False
		if piece.square+dice_result>14:
			return True
		square_id = str(piece.square+dice_result)+self.player if piece.square+dice_result not in list_shared_squares else str(piece.square+dice_result)+'S'

		if squares[square_id].piece == None:
			return True
		elif squares[square_id].piece.player != self.player:
			if squares[square_id].is_safe:
				return False
			else:
				return True
		else:
			return False