import numpy as np

class Board():
	def __init__(self):
		self.name = ''
		list_shared_squares = [[5,6,7,8,9,10,11,12],[False, False, False, True, False, False, False, False]]
		self.shared_squares = {str(x)+'S': Square(x,'S',y) for x,y in zip(*list_shared_squares)}
		list_private_squares = [[1,2,3,4,13,14,1,2,3,4,13,14],['A','A','A','A','A','A','B','B','B','B','B','B'],
						[False, False, False, True, True, False,False, False, False, True, True, False]]
		self.private_squares = {str(x)+y:Square(x,y,z) for x,y,z in zip(*list_private_squares)}
		self.squares = {}
		self.squares.update(self.shared_squares)
		self.squares.update(self.private_squares)

	def __str__(self):
		board_string = ' _____ _____ _____'+'\n'\
					   '|'+self.display_string('13A')+'|'+self.display_string('12S')+'|'+self.display_string('13B')+'|\n'\
					   '|'+self.display_string('14A')+'|'+self.display_string('11S')+'|'+self.display_string('14B')+'|\n'\
						+'      '+'|'+self.display_string('10S')+'|\n'\
						+' _____'+'|'+self.display_string('9S')+'|'+'_____\n'\
						'|'+self.display_string('1A')+'|'+self.display_string('8S')+'|'+self.display_string('1B')+'|\n'\
						'|'+self.display_string('2A')+'|'+self.display_string('7S')+'|'+self.display_string('2B')+'|\n'\
						'|'+self.display_string('3A')+'|'+self.display_string('6S')+'|'+self.display_string('3B')+'|\n'\
						'|'+self.display_string('4A')+'|'+self.display_string('5S')+'|'+self.display_string('4B')+'|'
		return board_string	

	def display_string(self, square_id):
		if self.squares[square_id].piece is None:
			#return '__'+str(self.squares[square_id].squarenumber)+'__'
			return '_____'
		else:
			#return '__'+str(self.squares[square_id].squarenumber)+'__'
			return '__'+str(self.squares[square_id].piece.player)+'__'

	def reset(self):
		list_shared_squares = [[5,6,7,8,9,10,11,12],[False, False, False, True, False, False, False, False]]
		self.shared_squares = {str(x)+'S': Square(x,'S',y) for x,y in zip(*list_shared_squares)}
		list_private_squares = [[1,2,3,4,13,14,1,2,3,4,13,14],['A','A','A','A','A','A','B','B','B','B','B','B'],
						[False, False, False, True, True, False,False, False, False, True, True, False]]
		self.private_squares = {str(x)+y:Square(x,y,z) for x,y,z in zip(*list_private_squares)}
		self.squares = {}
		self.squares.update(self.shared_squares)
		self.squares.update(self.private_squares)
		
class Square():
	def __init__(self, square_number, square_player, safe=False):
		self.squarenumber = square_number
		self.squareplayer = square_player	#S->shared suqare, A->Player1 square, B->Player2 square
		self.square_id = str(self.squarenumber)+self.squareplayer
		self.piece = None		
		self.is_safe = safe		#False if it is a square where a piece can be killed



"""
for key,square in board.squares.items():
	print(key, square.squarenumber, square.squareplayer, square.is_safe,"\n")
"""



