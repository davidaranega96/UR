import numpy as np

list_shared_squares = [5,6,7,8,9,10,11,12]

class Piece():
	def __init__(self, player):
		self.player = player
		self.square = 0
		self.alive = False		#If it is False, the piece has been eaten or has not left the square 0
		self.completed = False	#If it is False, the piece still has to complete the circuit

	def move_piece(self, dice_result, squares):
		if dice_result == 0:
			return 0
		self.alive = True
		#If the piece finishes the circuit
		if self.square+dice_result>14:
			self.completed = True
			self.alive = False
			return 1

		square_id = str(self.square+dice_result)+self.player if self.square+dice_result not in list_shared_squares else str(self.square+dice_result)+'S'
		
		if squares[square_id].piece == None:
			self.square += dice_result
			squares[square_id].piece = self
			return 0
		elif squares[square_id].piece.player != self.player:
			if squares[square_id].is_safe:
				print("HEREEE")
				return -1
			else:
				print("heree2")
				squares[square_id].piece.death()
				print(squares[square_id].piece.square)
				squares[square_id].piece = self
				self.square += dice_result
				return 0
		else:
			return -1

	def death(self):
		self.square = 0
		self.alive = False
		self.completed = False

	def __str__(self):
		return "Piece from player "+str(self.player)+". Currently at square "+str(self.square)
