from day3_part1 import load_input, parse_input, final_solution


def max_ordered_number(line: str) -> int:
    """
        Return the largest possible 12-digit number formed by selecting digits
        from the input string while preserving their order (indices must increase).

        Digits do not need to be adjacent, but rearranging them is not allowed.
        """
    digits: list[int] = [int(i) for i in line]
    current_first_index: int = 0
    result: int = 0

    for i in range(12, 0, -1):
        # We can only choose a digit from a range that still allows
        # picking the remaining (i - 1) digits later.
        shortened_list: list[int] = digits[current_first_index:len(digits) - i + 1]
        maximum: int = max(shortened_list)
        current_first_index = shortened_list.index(maximum)+1+current_first_index
        result += maximum * 10 ** (i-1)

    return result


if __name__ == '__main__':
    loaded_input: str = load_input('input.txt')
    parsed_input: list[str] = parse_input(loaded_input)

    print(final_solution(parsed_input, max_ordered_number))
