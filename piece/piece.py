from enum import Enum

DEFAULT_PIECE_SIZE = "128px"


class PieceType(Enum):
    # Reference: https://www.chess.com/terms/chess-pieces

    KING = "king"
    QUEEN = "queen"
    ROOK = "rook"
    BISHOP = "bishop"
    KNIGHT = "knight"
    PAWN = "pawn"


class PieceTeam(Enum):
    # Reference: https://www.chess.com/terms/chess-pieces

    BLACK = "black"
    WHITE = "white"


class Piece:
    def __init__(self, x: int, y: int, type: PieceType, team: PieceTeam) -> None:
        self.x = x
        self.y = y
        self.type = type

        self.sprite_path = self._get_sprite_path(type)

    def _get_sprite_path(self, type: PieceType, team: PieceTeam) -> str:
        return f"./images/{team.value}_{type.value}_shadow_{DEFAULT_PIECE_SIZE}.png"
