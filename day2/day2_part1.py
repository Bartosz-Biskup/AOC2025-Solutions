from typing import Callable


def load_input(input_file: str) -> str:
    """Load the puzzle input from the input file and return it as a string."""
    with open(input_file, 'r') as f:
        return f.read()


def parse_input(puzzle_input: str) -> list[tuple[int, int]]:
    """
        Parse the puzzle input and return a list of numeric ranges.
    """
    result: list[tuple[int, int]] = []

    split_input: list[str] = puzzle_input.split(',')
    for element in split_input:
        result.append(tuple(map(int, element.split('-'))))

    return result


# used for splitting number into chunks to check if they repeat themselves
def split_string(s : str, chunk_size: int) -> list[str]:
    """
        Split a string into chunks of a given size.
    """
    return [s[i:i + chunk_size] for i in range(0, len(s), chunk_size)]


def is_number_invalid(number: int) -> bool:
    """
        Return True if the number consists of two identical halves.

        Example:
            1212 -> 12 | 12 -> True
            1213 -> 12 | 13 -> False
    """
    str_num: str = str(number)
    if len(str_num) % 2 == 1:
        return False

    return str_num[:len(str_num) // 2] == str_num[len(str_num) // 2:]


def sum_invalid_numbers(range_: tuple[int, int],
                        validation_function: Callable[[int], bool]) -> int:
    """
        Return the sum of all numbers in the given range
        that satisfy the validation function.
    """
    amount_of_invalid_numbers: int = 0
    for number in range(range_[0], range_[1]+1):
        if validation_function(number):
            amount_of_invalid_numbers += number

    return amount_of_invalid_numbers


def final_solution(puzzle_input: list[tuple[int, int]], validation_function: Callable[[int], bool]) -> int:
    """
        Return the final puzzle solution by summing all invalid numbers
        across all input ranges.
    """
    result: int = sum(sum_invalid_numbers(i, validation_function) for i in puzzle_input)

    return result


if __name__ == '__main__':
    loaded_input: str = load_input('input.txt')
    parsed_input: list[tuple[int, int]] = parse_input(loaded_input)

    print(final_solution(parsed_input, is_number_invalid))
