from day6_part1 import load_input, parse_input, solution


def transpose_and_reverse_columns(x: list[str]) -> list[str]:
    """
        Parses a single problem block for Part 2 of the cephalopod worksheet.

        Steps:
        - Takes a vertical block of digits with an operator at the bottom.
        - Transposes rows into columns to extract numbers.
        - Reverses each number to read digits top → bottom.
        - Appends the operator at the end.

        Returns:
            List of strings where each string is a number, and the last element is the operator.
        """
    operator: str = x[-1].strip()
    columns: list[tuple[str, ...]] = list(zip(*x[:-1]))

    numbers: list[str] = list((''.join(i).strip() for i in columns))
    numbers.append(operator)

    return numbers


if __name__ == '__main__':
    loaded_input: str = load_input()
    parsed_input: list[list[str]] = parse_input(loaded_input, ignore_whitespaces=False)

    print(solution(list(map(transpose_and_reverse_columns, parsed_input))))
