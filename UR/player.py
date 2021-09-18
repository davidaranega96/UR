from piece import *

class Player():
	def __init__(self, player, name):
		self.player = player #Either player 1 or player 2
		self.name = name
		self.score = 0
		self.pieces = [Piece(player) for i in range(6)]
