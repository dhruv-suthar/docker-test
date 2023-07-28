from fastapi import APIRouter
from typing import Dict
from base.schemas import ChessPositionsSchema
from base.utils.chess_utils import *

router = APIRouter()

@router.post("/chess/{slug}")
def get_valid_moves_for_piece_api(slug:str,positions: ChessPositionsSchema):
    slug = slug.capitalize()
    piece_positions = dict(positions)
    piece_positions = piece_positions.get("positions")
    if slug in piece_positions:
        board = Board()
        board.add_pieces_from_input(piece_positions)
        enemy_moves = []
        user_possible_moves = []
        piece_obj = None
        for key in piece_positions:
            if key == "King":
                piece_obj = King()
            elif key == "Queen":
                piece_obj = Queen()
            elif key == "Pawn":
                piece_obj = Pawn()
            elif key == "Knight":
                print("true")
                piece_obj = Knight()
            elif key == "Bishop":
                piece_obj = Bishop()
            elif key == "Rook":
                piece_obj = Rook()

            row, col = pos_to_row_col(piece_positions.get(key))
            if slug == key:
                user_possible_moves = piece_obj.get_all_possible_moves(row,col,board)
            else:
                enemy_moves.extend(piece_obj.get_all_possible_moves(row,col,board))
        return {"valid_moves": remove_common_moves(user_possible_moves,enemy_moves)}
    else:
        return {"message": f"{slug} does not exist in positions list"}

        
        