from typing import Literal, Final


STARTING_POINT: Final[int] = 50
DIAL_SIZE: Final[int] = 100
Directions = Literal['left', 'right']


def load_input() -> str:
    """Load the puzzle input from the input file and return it as a string."""
    with open('input.txt') as input_content:
        return input_content.read()


def parse_input(input_content: str) -> list[tuple[Directions, int]]:
    """
        Parse the input content[str] and returns list of moves.

        Each move is represented as a tuple:
        (direction, value).
    """
    split_input: list[str] = input_content.split()

    final_input: list[tuple[Directions, int]] = []
    for element in split_input:
        rotation_direction: Directions = 'right' if element[:1] == 'R' else 'left'
        rotation_value: int = int(element[1:])
        final_input.append((rotation_direction, rotation_value))

    return final_input


def value_after_rotation(current_point: int,
                         rotation_direction: Directions,
                         rotation_value: int) -> int:
    """
        Calculate the dial position after applying a single rotation.
    """
    value_after: int = current_point + rotation_value * (1 if rotation_direction == 'right' else -1)

    return value_after % DIAL_SIZE


def count_zeros(starting_point: int, moves: list[tuple[Directions, int]]) -> int:
    """
        Count how many times the dial ends at position 0 after each move.
    """
    amount_of_zeros: int = 0

    for move in moves:
        starting_point = value_after_rotation(starting_point, move[0], move[1])
        if starting_point == 0:
            amount_of_zeros += 1

    return amount_of_zeros


if __name__ == '__main__':
    loaded_input: str = load_input()
    parsed_input: list[tuple[Directions, int]] = parse_input(loaded_input)

    print(count_zeros(STARTING_POINT, parsed_input))
