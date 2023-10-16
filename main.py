import pyray as ray

from board.board import Board

SIZE_PX = 800


def main():
    ray.init_window(SIZE_PX, SIZE_PX, "PyChess")

    board = Board(SIZE_PX)

    while not ray.window_should_close():
        ray.begin_drawing()

        board.draw_background()

        ray.end_drawing()

    board.unload_textures()

    ray.close_window()

    print(board.board)


if __name__ == "__main__":
    main()
