def load_input() -> str:
    """Load the puzzle input from the input file and return it as a string."""
    with open('input.txt') as input_content:
        return input_content.read()


def parse_input(puzzle_input: str,
                ignore_whitespaces: bool = True) -> list[list[str]]:
    input_lines: list[str] = puzzle_input.split('\n')

    # Pad every line to make sure every line has the same length.
    max_length: int = max(len(line) for line in input_lines)
    input_lines = [line.ljust(max_length) for line in input_lines]

    columns = list(zip(*input_lines))
    temp: list[str] = [''] * len(input_lines)
    result: list[list[str]] = []

    for column in columns:
        if all(i ==' ' for i in column):
            result.append(temp)
            temp = [''] * len(input_lines)
            continue

        for i in range(len(input_lines)):
            if ignore_whitespaces:
                temp[i] += column[i] if column[i] != ' ' else ''
            else:
                temp[i] += column[i]

    result.append(temp)
    return result


def solve_single_list(puzzle: list[str]) -> int:
    """
    Takes list of numbers as strings and expects last element of the list to be an operator - either '+' or '*'.
    If operator isn't one of them, ValueError is thrown. Returns the sum or the product of all the numbers depending
    on last character.
    """
    operator: str = puzzle[-1]
    if operator not in {'+', '*'}:
        raise ValueError("The operator must be either '+' or '*'.")
    result: int = 1 if operator == '*' else 0

    for number in list(map(int, puzzle[:-1])):
        if operator == '*':
            result *= number
        else:
            result += number

    return result


def solution(puzzle_input: list[list[str]]) -> int:
    """
    The sum of all single lists solutions in puzzle_input
    """
    return sum(map(solve_single_list, puzzle_input))


if __name__ == '__main__':
    loaded_input: str = load_input()
    parsed_input: list[list[str]] = parse_input(loaded_input)

    print(solution(parsed_input))
