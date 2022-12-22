from enum import Enum
from typing import Iterable, Generator


class RPC(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class Outcome(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6


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

OUTCOME_CODES = {
    "X": Outcome.LOSE,
    "Y": Outcome.DRAW,
    "Z": Outcome.WIN,
}


def _rpc_score_outcome(op_move: RPC, move: RPC) -> int:
    if op_move == move:
        return Outcome.DRAW.value
    if move.value == (op_move.value + 1) % len(RPC):
        return Outcome.WIN.value
    return Outcome.LOSE.value


def _rpc_move_forced_outcome(op_move: RPC, forced_outcome: Outcome) -> RPC:
    if forced_outcome == Outcome.DRAW:
        return op_move
    if forced_outcome == Outcome.WIN:
        return RPC((op_move.value + 1) % len(RPC))
    else:
        return RPC((op_move.value - 1) % len(RPC))


def rpc_scores(
    move_pairs: Iterable[str], play_for_outcome: bool = False
) -> Generator[int, None, None]:
    for turn in move_pairs:
        match turn.strip().split(" "):
            case [op_move_str, move_str]:
                op_move = OPPONENT_CODES[op_move_str]
                forced_outcome = OUTCOME_CODES[move_str]
                move = (
                    _rpc_move_forced_outcome(op_move, forced_outcome)
                    if play_for_outcome
                    else PLAYER_CODES[move_str]
                )
                yield (
                    forced_outcome.value
                    if play_for_outcome
                    else _rpc_score_outcome(op_move, move)
                ) + move.value + 1
            case _:
                raise RuntimeError("Invalid move pair")


def rpc_score(move_pairs: Iterable[str], play_for_outcome: bool = False) -> int:
    return sum(rpc_scores(move_pairs, play_for_outcome=play_for_outcome))


if __name__ == "__main__":
    print(f"Total score: {rpc_score(open('2/input.txt'))}")

    print(
        f"Total score playing for outcome: {rpc_score(open('2/input.txt'), play_for_outcome=True)}"
    )
