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

        self.pieces_textures_map = dict()

        for piece in self.board.values():
            if isinstance(piece, type(None)):
                continue

            texture = ray.load_texture(piece.sprite_path)

            if texture in self.pieces_textures_map.values():
                continue

            self.pieces_textures_map.update({(piece.type, piece.team): texture})

    def unload_textures(self):
        ray.unload_texture(self.green_square_texture)
        ray.unload_texture(self.creme_square_texture)

        for texture in self.pieces_textures_map.values():
            ray.unload_texture(texture)

    def _convert_x_to_text(self, x: int) -> str:
        if x < 1 or x > BOARD_SIZE:
            raise ValueError(f"Invalid x value {x} for text convertion")

        conversion = "abcdefgh"

        return conversion[x - 1]

    def _convert_x_to_matrix_value(self, x: int) -> int:
        if x < 1 or x > BOARD_SIZE:
            raise ValueError(f"Invalid x value {x} for matrix value convertion")

        return x - 1
    
    def _convert_y_to_matrix_value(self, y: int) -> int:
        if y < 1 or y > BOARD_SIZE:
            raise ValueError(f"Invalid y value {y} for matrix value convertion")

        original_y_coordinates = list(range(1, BOARD_SIZE + 1))

        result_y_coordinates = original_y_coordinates[::-1]
        result_y_coordinates = [y - 1 for y in result_y_coordinates]

        result_map = dict(zip(original_y_coordinates, result_y_coordinates))

        return result_map[y]

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
            board[(column, row)] = Piece(PieceType.PAWN, piece_team)

    def _populate_normal_row(self, board: dict, row: int, piece_team: PieceTeam):
        if row != 1 and row != 8:
            raise ValueError(
                f"Invalid row value {row} for populating the board with pawn"
            )
        
        board[(1, row)] = Piece(PieceType.ROOK, piece_team)
        board[(2, row)] = Piece(PieceType.KNIGHT, piece_team)
        board[(3, row)] = Piece(PieceType.BISHOP, piece_team)

        board[(4, row)] = Piece(PieceType.QUEEN, piece_team)
        board[(5, row)] = Piece(PieceType.KING, piece_team)

        board[(6, row)] = Piece(PieceType.BISHOP, piece_team)
        board[(7, row)] = Piece(PieceType.KNIGHT, piece_team)
        board[(8, row)] = Piece(PieceType.ROOK, piece_team)

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
        square_size = self.size_px // BOARD_SIZE

        for position, piece in self.board.items():
            if piece is None:
                continue
            
            x, y = position

            x = self._convert_x_to_matrix_value(x) * square_size
            y = self._convert_y_to_matrix_value(y) * square_size

            texture = self.pieces_textures_map[(piece.type, piece.team)]

            texture.width = square_size
            texture.height = square_size

            ray.draw_texture(texture, x, y, ray.WHITE)

