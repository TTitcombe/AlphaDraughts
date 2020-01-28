import numpy as np
from alphadraughts.draughts.piece import EmptyPiece, Piece

new_board = np.array(
    [
        [
            EmptyPiece(),
            Piece("black", 1),
            EmptyPiece(),
            Piece("black", 2),
            EmptyPiece(),
            Piece("black", 3),
            EmptyPiece(),
            Piece("black", 4),
        ],
        [
            Piece("black", 5),
            EmptyPiece(),
            Piece("black", 6),
            EmptyPiece(),
            Piece("black", 7),
            EmptyPiece(),
            Piece("black", 8),
            EmptyPiece(),
        ],
        [
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
        ],
        [
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
        ],
        [
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
        ],
        [
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
            EmptyPiece(),
        ],
        [
            EmptyPiece(),
            Piece("white", 25),
            EmptyPiece(),
            Piece("white", 26),
            EmptyPiece(),
            Piece("white", 27),
            EmptyPiece(),
            Piece("white", 28),
        ],
        [
            Piece("white", 29),
            EmptyPiece(),
            Piece("white", 30),
            EmptyPiece(),
            Piece("white", 31),
            EmptyPiece(),
            Piece("white", 32),
            EmptyPiece(),
        ],
    ],
    dtype=object,
)
