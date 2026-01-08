from day2_part1 import load_input, parse_input, final_solution, split_string


def get_divisors(number: int) -> list[int]:
    """
        Return all positive divisors of a number except the number itself.
    """
    return [i for i in range(1, number) if number % i == 0]


def is_invalid_number(number: int) -> bool:
    """
        Return True if the number consists of a repeating sequence of digits.

        All possible sequence lengths are checked based on the length
        of the number.
    """
    num_str: str = str(number)

    for factor in get_divisors(len(num_str)):
        chunks: list[str] = split_string(num_str, factor)

        if all(chunks[0] == i for i in chunks):
            return True

    return False


if __name__ == '__main__':
    loaded_input: str = load_input('input.txt')
    parsed_input: list[tuple[int, int]] = parse_input(loaded_input)

    print(final_solution(parsed_input, is_invalid_number))