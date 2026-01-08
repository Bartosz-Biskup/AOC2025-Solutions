def load_input() -> str:
    """Load the puzzle input from 'input.txt' and return it as a string."""
    with open('input.txt') as file:
        return file.read()


def parse_input(puzzle_content: str) -> tuple[list[tuple[int, int]], list[int]]:
    """
    Parse the puzzle input into a list of ranges and a list of numbers.

    Returns:
        - ranges: list of tuples (start, end)
        - numbers: list of integers
    """
    lines: list[str] = puzzle_content.split('\n')
    blank_line_index: int = lines.index('')

    range_lines, value_lines = lines[:blank_line_index], lines[blank_line_index + 1:]

    ranges: list[tuple[int, int]] = [
        tuple(map(int, line.split('-'))) for line in range_lines
    ]

    numbers: list[int] = list(map(int, value_lines))

    return ranges, numbers


def is_in_range(number: int, range_: tuple[int, int]) -> bool:
    """
    Return True if the number falls within the inclusive range.
    """
    return range_[0] <= number <= range_[1]


def solution(parsed_input: tuple[list[tuple[int, int]], list[int]]) -> int:
    """
    Count how many numbers fall within at least one of the given ranges.
    """
    ranges, numbers = parsed_input
    count: int = 0

    for number in numbers:
        if any(is_in_range(number, range_) for range_ in ranges):
            count += 1

    return count


if __name__ == '__main__':
    input_content: str = load_input()
    parsed_data: tuple[list[tuple[int, int]], list[int]] = parse_input(input_content)

    print(solution(parsed_data))
