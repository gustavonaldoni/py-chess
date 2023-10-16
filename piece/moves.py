from piece.piece import PieceType, PieceTeam
from board.board import Board


def piece_exists_on_position(
    x: int, y: int, piece_team: PieceTeam, board: Board
) -> bool:
    piece = board.board.get((x, y))

    return (piece is not None) and (piece.team == piece_team)


def valid_moves_king(
    x: int, y: int, piece_team: PieceTeam, board: Board
) -> list[tuple]:
    if not piece_exists_on_position(x, y, piece_team, board):
        raise ValueError(
            f"The piece on position ({x}, {y}) does not exist or it is not a king"
        )


def valid_moves_queen(
    x: int, y: int, piece_team: PieceTeam, board: Board
) -> list[tuple]:
    if not piece_exists_on_position(x, y, piece_team, board):
        raise ValueError(
            f"The piece on position ({x}, {y}) does not exist or it is not a queen"
        )


def valid_moves_rook(
    x: int, y: int, piece_team: PieceTeam, board: Board
) -> list[tuple]:
    if not piece_exists_on_position(x, y, piece_team, board):
        raise ValueError(
            f"The piece on position ({x}, {y}) does not exist or it is not a rook"
        )


def valid_moves_bishop(
    x: int, y: int, piece_team: PieceTeam, board: Board
) -> list[tuple]:
    if not piece_exists_on_position(x, y, piece_team, board):
        raise ValueError(
            f"The piece on position ({x}, {y}) does not exist or it is not a bishop"
        )


def valid_moves_knight(
    x: int, y: int, piece_team: PieceTeam, board: Board
) -> list[tuple]:
    if not piece_exists_on_position(x, y, piece_team, board):
        raise ValueError(
            f"The piece on position ({x}, {y}) does not exist or it is not a knight"
        )


def valid_moves_pawn(
    x: int, y: int, piece_team: PieceTeam, board: Board
) -> list[tuple]:
    if not piece_exists_on_position(x, y, piece_team, board):
        raise ValueError(
            f"The piece on position ({x}, {y}) does not exist or it is not a pawn"
        )

    valid_moves = []

    # Check the front square
    front_square_piece = board.board.get((x, y + 1))

    if front_square_piece is None:
        valid_moves.append((x, y))

    # Check the left diagonal square
    left_diagonal_square_piece = board.board.get((x - 1, y + 1))

    if left_diagonal_square_piece is not None:
        if left_diagonal_square_piece.team != piece_team:
            valid_moves.append((x - 1, y + 1))

    # Check the right diagonal square
    right_diagonal_square_piece = board.board.get((x + 1, y + 1))

    if right_diagonal_square_piece is not None:
        if right_diagonal_square_piece.team != piece_team:
            valid_moves.append((x + 1, y + 1))

    return valid_moves


VALID_MOVES_MAP = {
    PieceType.KING: valid_moves_king,
    PieceType.QUEEN: valid_moves_queen,
    PieceType.ROOK: valid_moves_rook,
    PieceType.BISHOP: valid_moves_bishop,
    PieceType.KNIGHT: valid_moves_knight,
    PieceType.PAWN: valid_moves_pawn,
}
