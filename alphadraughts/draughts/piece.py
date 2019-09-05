from alphadraughts.draughts.enums import Direction


class BasePiece:
    BOARD_REPRESENTATION = None
    PRINT_REPRESENTATION = None

    def move(self, _):
        raise NotImplementedError


class EmptyPiece(BasePiece):
    BOARD_REPRESENTATION = 0
    PRINT_REPRESENTATION = "-"

    def __init__(self, square=""):
        self.square = square

    def move(self, _):
        return False

    def __str__(self):
        return "-"

    def __eq__(self, other):
        if isinstance(other, EmptyPiece):
            return True
        elif isinstance(other, BasePiece):
            return False
        else:
            return super(EmptyPiece, self).__eq__(other)


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

    def __eq__(self, other):
        # Eq should only consider if pieces are the same side
        if isinstance(other, str):
            # Assume other is white or black
            return self.player == other
        elif isinstance(other, Piece):
            return self.player == other.player

        # Otherwise default behaviour
        return super(Piece, self).__eq__(other)


class King(Piece):
    def move(self, move: str) -> bool:
        return True

    def __str__(self):
        return "K" + super(King, self).__str__()
