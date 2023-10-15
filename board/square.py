from enum import Enum

DEFAULT_SQUARE_SIZE = "128px"


class SquareColor(Enum):
    DARK_BROWN = "darkbrown"
    LIGHT_BROWN = "lightbrown"

    DARK_GRAY = "darkgray"
    LIGHT_GRAY = "lightgray"


class Square:
    def __init__(self, x: int, y: int, color: SquareColor) -> None:
        self.x = x
        self.y = y
        self.color = color

        self.sprite_path = self._get_sprite_path(type)

    def _get_sprite_path(self, color: SquareColor) -> str:
        return f"./images/square_{color.value}_shadow_{DEFAULT_SQUARE_SIZE}.png"
