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
    def __init__(self, type: PieceType, team: PieceTeam) -> None:
        self.type = type
        self.team = team

        self.sprite_path = self._get_sprite_path()

    def _get_sprite_path(self) -> str:
        return f"./images/pieces/{self.team.value}_{self.type.value}_shadow_{DEFAULT_PIECE_SIZE}.png"
