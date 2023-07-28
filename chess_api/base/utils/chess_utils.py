from abc import ABC, abstractmethod

def pos_to_row_col(pos):
	print(pos,"------------------")
	column_letter = pos[0]
	row_number = int(pos[1:]) - 1
	column = ord(column_letter) - ord('A')
	return row_number, column

def row_col_to_pos(row, col):
	column_letter = chr(col + ord('A'))
	return f"{column_letter}{row + 1}"

def remove_common_moves(piece1_moves,piece2_moves):
	# print(piece2_moves)
	new_moves = set(piece1_moves) - set(piece2_moves)
	new_moves = list(new_moves)
	return sorted(new_moves)

class Board():
	def __init__(self):
		self.board = [[None for _ in range(8)] for _ in range(8)]

	def is_empty(self, row, col):
		return self.board[row][col] is None    

	def add_piece(self, piece, row, col):
		self.board[row][col] = piece    

	def add_pieces_from_input(self, positions):    
		for piece_name, position in positions.items():
			row, col = pos_to_row_col(position)
			if piece_name == "Pawn":
				piece = Pawn()
			elif piece_name == "Rook":
				piece = Rook()
			elif piece_name == "Bishop":
				piece = Bishop()
			elif piece_name == "Knight":
				piece = Knight()
			elif piece_name == "Queen":
				piece = Queen()
			elif piece_name == "King":
				piece = King()
			else:
				print("Not valid piece name\n")

			self.add_piece(piece, row, col) 

	def is_valid_position(self, row, col):
		return 0 <= row < 8 and 0 <= col < 8              

class Piece():
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return f"{self.name}"

	def get_valid_moves_in_direction(self,move_offsets,row,col,board,is_extend=False):
		moves = []
		if is_extend:
			for dr, dc in move_offsets:
				new_row, new_col = row, col
				while True:
					new_row += dr
					new_col += dc
					if not board.is_valid_position(new_row, new_col):
						break
					if not board.is_empty(new_row, new_col):
						moves.append(row_col_to_pos(new_row,new_col))
						break
					else:
						moves.append(row_col_to_pos(new_row,new_col))
		else:
			for dr, dc in move_offsets:
				new_row = row + dr
				new_col = col + dc
				if board.is_valid_position(new_row, new_col):
					# moves.append((new_row, new_col))
					moves.append(row_col_to_pos(new_row,new_col))
		return moves    


	@abstractmethod
	def get_all_possible_moves(self, row, col, board):
		pass

class Pawn(Piece):
	def __init__(self):
		super().__init__("Pawn")

	#NOT USING AS PER TEST CASES - Reason not specified direction of pawn       
	def get_all_possible_moves(self,row,col,board):
		moves = []
		direction = -1  

		# One square forward
		new_row = row + direction
		new_col = col
		if board.is_valid_position(new_row, new_col) and board.is_empty(new_row, new_col):
			moves.append(row_col_to_pos(new_row, new_col))

		if row == 6 or row == 1:
			new_row = row + 2 * direction
			new_col = col
			if board.is_valid_position(new_row, new_col) and board.is_empty(new_row, new_col):
				moves.append(row_col_to_pos(new_row, new_col))

		
		return moves

class Rook(Piece):
	def __init__(self):
		super().__init__("Rook")

	def get_all_possible_moves(self,row,col,board):
		moves = []
		move_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
		moves = super().get_valid_moves_in_direction(move_offsets,row,col,board,True)
		return moves

class Knight(Piece):
	def __init__(self):
		super().__init__("Knight")
	def get_all_possible_moves(self,row,col,board):
		move_offsets = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
		moves = super().get_valid_moves_in_direction(move_offsets,row,col,board)
		return moves

class Bishop(Piece):
	def __init__(self):
		super().__init__("Bishop")

	def get_all_possible_moves(self,row,col,board):    
		moves = []
		move_offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
		moves = super().get_valid_moves_in_direction(move_offsets,row,col,board,True)
		return moves                


class Queen(Piece):
	def __init__(self):
		super().__init__("Queen")

	def get_all_possible_moves(self,row,col,board):
		# moves = []
		move_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
		moves = super().get_valid_moves_in_direction(move_offsets,row,col,board,True)
		return moves


class King(Piece):
	def __init__(self):
		super().__init__("King")

	def get_all_possible_moves(self,row,col,board):
		# moves = []
		move_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
		moves = super().get_valid_moves_in_direction(move_offsets,row,col,board)
		return moves


