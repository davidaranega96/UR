from config import EMPTY_BOARD_CONFIGURATION


class Board:
	BOARD_CONFIGURATION = EMPTY_BOARD_CONFIGURATION

	def __init__(self, player_1, player_2):
		self.player_1 = player_1
		self.player_2 = player_2
		self.load_empty_board(player_1, player_2)

	def load_empty_board(self, player_1, player_2):
		# TODO: Working on this
		safe_squares = EMPTY_BOARD_CONFIGURATION['safe_squares']

	@staticmethod
	def create_shared_squares(board_configuration):
		shared_squares = []
		for square_number in board_configuration['shared_squares']:
			safe = square_number in board_configuration['safe_squares']
			square = Square(square_number, safe)
			shared_squares.append(square)

		return shared_squares


class Square:
	def __init__(self, square_number, safe=False):
		self.square_number = square_number
		self.piece = None
		self.is_safe = safe

	def __eq__(self, other):
		if isinstance(self, other.__class__):
			return self.square_number == other.square_number and self.piece == other.piece and self.is_safe is other.is_safe
		return False


class PrivateSquare(Square):
	def __init__(self, square_number, player, safe=False):
		super().__init__(square_number, safe)
		self.player = player

	def __eq__(self, other):
		if isinstance(self, other.__class__):
			return super().__eq__(other) and self.player == other.player
		return False
