import random

class Board:

    def __init__(self):
        self._piles = []
        self._prepare()

    def apply(self,move):
        pile = move.get_pile()
        stones = move.get_stones()
        self._piles[pile] -= stones

    def is_empty(self):
        return sum(self._piles) == 0

    def to_string(self):
        width_of_board = 30
        board = "\n" + ("-" * width_of_board) + "\n"
        for i in range(len(self._piles)):
            board += (f"{i}:" + (" 0 " * self._piles[i]) + "\n")
        board += ("-" * width_of_board)
        return board        

    def _prepare(self):
        num_piles = random.randint(2,5)
        for i in range(num_piles):
            self._piles.append(random.randint(1,9))