from enum import Enum
from typing import Iterable, Generator


class RPC(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


OPPONENT_CODES = {
    "A": RPC.ROCK,
    "B": RPC.PAPER,
    "C": RPC.SCISSORS,
}

PLAYER_CODES = {
    "X": RPC.ROCK,
    "Y": RPC.PAPER,
    "Z": RPC.SCISSORS,
}

LOSE, DRAW, WIN = [0, 3, 6]


def _rpc_score_outcome(op_move: RPC, move: RPC) -> int:
    if op_move == move:
        return DRAW
    if move.value == (op_move.value + 1) % len(RPC):
        return WIN
    return LOSE


def rpc_scores(move_pairs: Iterable[str]) -> Generator[int, None, None]:
    for turn in move_pairs:
        match turn.split(" "):
            case [op_move, move]:
                op_move = OPPONENT_CODES[op_move]
                move = PLAYER_CODES[move]
                yield _rpc_score_outcome(op_move, move) + move.value + 1
            case _:
                raise RuntimeError("Invalid move pair")


def rpc_score(move_pairs: Iterable[str]) -> int:
    return sum(rpc_scores(move_pairs))
