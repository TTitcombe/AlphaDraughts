from alphadraughts.draughts.enums import Direction


class BasePiece:
    BOARD_REPRESENTATION = None
    PRINT_REPRESENTATION = None

    def move(self, _):
        raise NotImplementedError


class EmptyPiece(BasePiece):
    BOARD_REPRESENTATION = 0
    PRINT_REPRESENTATION = "-"

    def __init__(self, square):
        self.square = square

    def move(self, _):
        return False

    def __str__(self):
        return "-"


class Piece(BasePiece):
    def __init__(self, player, square):
        assert player in ("white", "black")
        self.player = player
        self.square = square

    def move(self, direction: Direction) -> bool:
        if self.player == "white":
            if direction == Direction.SE or direction == Direction.SW:
                return False
            elif direction == Direction.NE or direction == Direction.NW:
                return True
        elif self.player == "black":
            if direction == Direction.SE or direction == Direction.SW:
                return True
            elif direction == Direction.NE or direction == Direction.NW:
                return False
        # Catch any remainder cases e.g. Direction.Invalid
        return False

    def promote(self):
        return King(self.player, self.square)

    def __str__(self):
        if self.player == "white":
            return "O"
        elif self.player == "black":
            return "X"


class King(Piece):
    def move(self, move: str) -> bool:
        return True

    def __str__(self):
        return "K" + super(King, self).__str__()
