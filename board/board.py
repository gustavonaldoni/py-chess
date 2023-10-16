import pyray as ray

from enum import Enum
from piece.piece import Piece, PieceType, PieceTeam

BOARD_SIZE = 8


class SquareColor(Enum):
    CREME = "creme"
    GREEN = "green"


class Board:
    def __init__(self, size_px: int) -> None:
        self.board = self._initialize_board()
        self.size_px = size_px

        self.load_textures()

    def load_textures(self):
        self.green_square_texture = ray.load_texture(
            "./images/board/square_green_128px.png"
        )
        self.creme_square_texture = ray.load_texture(
            "./images/board/square_creme_128px.png"
        )

    def unload_textures(self):
        ray.unload_texture(self.green_square_texture)
        ray.unload_texture(self.creme_square_texture)

    def _convert_x_to_text(self, x: int) -> str:
        if x < 1 or x > BOARD_SIZE:
            raise ValueError(f"Invalid x value {x} for text convertion")

        conversion = "abcdefgh"

        return conversion[x - 1]

    def _create_empty_board(self) -> dict[tuple:None]:
        board = dict()

        for x in range(1, BOARD_SIZE + 1):
            for y in range(1, BOARD_SIZE + 1):
                board.update({(x, y): None})

        return board

    def _populate_pawn_row(self, board: dict, row: int, piece_team: PieceTeam):
        if row != 2 and row != 7:
            raise ValueError(
                f"Invalid row value {row} for populating the board with pawn"
            )

        for column in range(1, BOARD_SIZE + 1):
            board[(row, column)] = Piece(PieceType.PAWN, piece_team)

    def _populate_normal_row(self, board: dict, row: int, piece_team: PieceTeam):
        if row != 1 and row != 8:
            raise ValueError(
                f"Invalid row value {row} for populating the board with pawn"
            )

        board[(row, 1)] = Piece(PieceType.ROOK, piece_team)
        board[(row, 2)] = Piece(PieceType.KNIGHT, piece_team)
        board[(row, 3)] = Piece(PieceType.BISHOP, piece_team)

        board[(row, 4)] = Piece(PieceType.QUEEN, piece_team)
        board[(row, 5)] = Piece(PieceType.KING, piece_team)

        board[(row, 6)] = Piece(PieceType.BISHOP, piece_team)
        board[(row, 7)] = Piece(PieceType.KNIGHT, piece_team)
        board[(row, 8)] = Piece(PieceType.ROOK, piece_team)

    def _initialize_board(self) -> dict[tuple:Piece]:
        board = self._create_empty_board()

        self._populate_pawn_row(board, 2, PieceTeam.WHITE)
        self._populate_normal_row(board, 1, PieceTeam.WHITE)

        self._populate_pawn_row(board, 7, PieceTeam.BLACK)
        self._populate_normal_row(board, 8, PieceTeam.BLACK)

        return board

    def _draw_background_row(self, row: int, last_color: SquareColor) -> SquareColor:
        texture_map = {
            SquareColor.CREME: self.creme_square_texture,
            SquareColor.GREEN: self.green_square_texture,
        }

        square_size = self.size_px // BOARD_SIZE

        y = row * square_size
        x = 0

        for i in range(BOARD_SIZE):
            texture = texture_map[last_color]
            ray.draw_texture(texture, x, y, ray.WHITE)

            if i == BOARD_SIZE - 1:
                return last_color

            if last_color == SquareColor.CREME:
                last_color = SquareColor.GREEN

            elif last_color == SquareColor.GREEN:
                last_color = SquareColor.CREME

            x += square_size

        return last_color

    def draw_background(self):
        last_color = SquareColor.CREME

        for i in range(BOARD_SIZE):
            last_color = self._draw_background_row(i, last_color)

    def draw_pieces(self):
        for position, piece in self.board.items():
            if len(piece) == 0:
                continue

            pass
