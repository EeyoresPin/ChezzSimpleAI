### ChezzSimpleAI
This is a simple AI, that plays A modified version of Chess Called Chezz in Object Oriented Python

To Run:
./run < board.txt

This code takes from the standard input and expects a board file as seen in board.txt
After deciding what move to follow, it will output a board to standard out.

Description:

This Code has two main sections, the first half of Chezz.py creates a repersentation of all possible board states, as seen by the rules below, that can be made from anyy board state.
The second half runs a MinMax algorithm on those possible moves, using alpha-beta Pruning.

minimax.py is simply a file to run the Chezz Class in Chezz.py


Chezz Specfic Rules:

The following pieces are different from chess:

• The Flinger (a.k.a. catapult) (F) – is a piece that moves like a king but
cannot capture (I.e. it can never move onto an occupied square). In
addition, it can Sling a friendly adjacent (8-neighbourhood) piece from
the piece’s starting position to a location that is in the same direction
as the direction from the adjacent piece to the catapult (I.e. the “Slung”
piece goes over the catapult and keeps going in the same direction).
The “Slung” piece can move any distance. It can land on an empty
square or on an opposing piece (in which case the opposing piece is
captured, and the Slung piece is also destroyed). There is one
exception: a “Slung” piece cannot capture a King. A catapulted piece
can Sly over top of any pieces. A piece cannot be Slung off the board.

• The Peon (P) – moves and captures like a regular chess pawn (except
that it can only move 1 square forward on its Sirst move, and the en
passant capture move is not allowed).

• The Knight (N) - moves and captures like a regular chess knight.

• The Cannon (C) - can move one square forwards, backwards, left or
right only (like a one-step rook). It cannot capture an opposing piece
(I.e. it cannot move to an occupied square). Instead of moving it can
Sire a cannonball in one of the four diagonal directions (sort of like a
bishop). If it Sires the cannonball, then all pieces (friend or foe) on the
diagonal are removed from the diagonal square next to the cannon to
the edge of the board. The Cannon cannot Sire a cannonball that
doesn’t hit any pieces (i.e. it cannot make a null move).

• Queen (Q) - moves and captures like a regular chess queen.

• King (K) - moves and captures like in regular chess (excl. castling
move).

• Zombie (Z) – can move one square forwards, backwards, left or right
only (like a one-step rook or like the cannon). It can move onto an
enemy piece, capturing that piece (and removing it from the board).

• Bishop (B) – moves and captures like in regular chess.

• Rook (R) – moves and captures like in regular chess.
The parenthesized letters after the piece name indicate how the piece is
represented in the code and board file.

The original rules for chess can be found here http://www.uschess.org/content/view/7324
