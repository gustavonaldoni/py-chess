import pyray as ray

from board.board import Board

SIZE_PX = 800


def main():
    ray.init_window(SIZE_PX, SIZE_PX, "PyChess")

    board = Board(SIZE_PX)

    while not ray.window_should_close():
        ray.begin_drawing()

        board.draw_background()
        board.draw_pieces()

        ray.end_drawing()

    board.unload_textures()

    ray.close_window()

    print()

    for position, piece in board.board.items():
        if piece is None:
            continue
        
        print(f'{position} : {piece.type.value} {piece.team.value}')

    print()


if __name__ == "__main__":
    main()
