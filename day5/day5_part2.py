from day5_part1 import load_input, parse_input


def merge_single_range_with_multiple_ranges(single_range: tuple[int, int],
                                            multiple_ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Merges a single inclusive range with multiple inclusive ranges by iterating through sorted list of multiple ranges.
    Require sorted input by range[0] in ascending order.
    """
    result: list[tuple[int, int]] = []

    for i in range(len(multiple_ranges)):
        if single_range[1]+1 < multiple_ranges[i][0]:
            result.append(single_range)
            return result + multiple_ranges[i:]
        elif single_range[0] > multiple_ranges[i][1]+1:
            result.append(multiple_ranges[i])
        else:
            single_range = min(single_range[0], multiple_ranges[i][0]), max(single_range[1], multiple_ranges[i][1])

    result.append(single_range)
    return result


def solution(parsed_input: tuple[list[tuple[int, int]], list[int]]) -> int:
    """
    Tries to merge each of inclusive ranges if possible, then returns the amount of all natural numbers
    that fall into any of these ranges.
    """
    ranges: list[tuple[int, int]] = sorted(parsed_input[0], key=lambda x: x[0])
    final_range: list[tuple[int, int]] = [ranges[0]]

    for range_ in ranges[1:]:
        final_range = merge_single_range_with_multiple_ranges(range_, final_range)

    result: int = 0
    for start, end in final_range:
        result += end - start + 1

    return result


if __name__ == '__main__':
    loaded_input: str = load_input()
    parsed_input: tuple[list[tuple[int, int]], list[int]] = parse_input(loaded_input)

    print(solution(parsed_input))
