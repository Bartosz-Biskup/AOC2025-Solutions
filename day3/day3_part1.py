from typing import Callable


def load_input(input_file: str) -> str:
    """Load the puzzle input from the input file and return it as a string."""
    with open(input_file, 'r') as f:
        return f.read()


def parse_input(input_content: str) -> list[str]:
    """Split the puzzle input into lines."""
    return input_content.split('\n')


def count_line(line: str) -> int:
    """
        Return the maximum two-digit number formed by any two digits in the line.
        The first digit must come before the second one.
    """
    max_joltage = 0
    # i and j are indexes of batteries
    for i in range(0, len(line)-1):
        for j in range(i+1, len(line)):
            value = int(line[i])*10 + int(line[j])
            max_joltage = max(max_joltage, value)

    return max_joltage


def final_solution(puzzle_input: list[str], counting_method: Callable[[str], int]) -> int:
    """Return the sum of the counts obtained from applying counting_method to each line."""
    return sum(counting_method(line) for line in puzzle_input)


if __name__ == '__main__':
    loaded_input: str = load_input('input.txt')
    parsed_input: list[str] = parse_input(loaded_input)

    print(final_solution(parsed_input, count_line))
