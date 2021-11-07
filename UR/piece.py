import numpy as np
import configparser
import json

parser = configparser.ConfigParser()
parser.read("config.ini")
list_shared_squares = parser.get("ur_squares", "shared_squares")
list_shared_squares = json.loads(list_shared_squares)

class Piece():
	def __init__(self, player, piece_id):
		self.player = player
		self.square = 0
		self.square_id = None
		self.alive = False		#If it is False, the piece has been eaten or has not left the square 0
		self.completed = False	#If it is False, the piece still has to complete the circuit
		self.piece_id = piece_id

	def move_piece(self, dice_result, squares):
		if self.completed == True:
			return 0
		if dice_result == 0:
			return 0
		self.alive = True
		#If the piece finishes the circuit
		if self.square+dice_result>14:
			squares[self.square_id].piece = None
			self.square = 15
			self.completed = True
			self.alive = False
			return 1

		prev_square_id = str(self.square)+self.player if self.square not in list_shared_squares else str(self.square)+'S'
		square_id = str(self.square+dice_result)+self.player if self.square+dice_result not in list_shared_squares else str(self.square+dice_result)+'S'
		
		if squares[square_id].piece == None:
			self.update_piece_and_square(square_id, dice_result, squares)
			return 0
		elif squares[square_id].piece.player != self.player:
			if squares[square_id].is_safe:
				return 0
			else:
				self.update_piece_and_square(square_id, dice_result, squares, killing=True)
				return 0
		else:
			return 0

	def update_piece_and_square(self, new_square_id, dice_result, squares, killing=False):
		try:
			squares[self.square_id].piece = None
		except:
			pass

		self.square += dice_result
		self.square_id = new_square_id
		if killing:
			squares[new_square_id].piece.death()
		squares[new_square_id].piece = self

	def death(self):
		self.square = 0
		self.alive = False
		self.completed = False

	def __str__(self):
		return "Piece from player "+str(self.player)+". Currently at square "+str(self.square)
