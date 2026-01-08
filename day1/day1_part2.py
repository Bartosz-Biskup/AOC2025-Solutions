from day1_part1 import STARTING_POINT, DIAL_SIZE,  Directions, load_input, parse_input, value_after_rotation


def count_all_zeros_between(starting_point: int,
                            direction: Directions,
                            rotation_value: int) -> int:
    """
        Return how many times the dial crosses position 0 during a single rotation.

        Example:
            start_position=10, direction='right', rotation_value=220 -> returns 2
    """
    after_move: int = starting_point + rotation_value * (1 if direction == 'right' else -1)

    if direction == 'right':
        zeros: int = after_move // DIAL_SIZE
    elif direction == 'left' and after_move > 0:
        zeros: int = 0
    elif direction == 'left' and after_move == 0:
        zeros: int = 1
    else:
        zeros: int = abs(after_move) // DIAL_SIZE + 1
        if starting_point == 0:
            zeros -= 1

    return zeros


def sum_all_zeros_between_rotations(starting_point: int,
                                    moves: list[tuple[Directions, int]]) -> int:
    """
        Return the total number of times the dial crosses position 0
        while applying all rotations.
    """
    total_zero_crossed: int = 0

    for move in moves:
        zeros_crossed_during_move: int = count_all_zeros_between(starting_point, move[0], move[1])
        starting_point = value_after_rotation(starting_point, move[0], move[1])

        total_zero_crossed += zeros_crossed_during_move

    return total_zero_crossed


if __name__ == '__main__':
    loaded_input: str = load_input()
    parsed_input: list[tuple[Directions, int]] = parse_input(loaded_input)

    print(sum_all_zeros_between_rotations(STARTING_POINT, parsed_input))
