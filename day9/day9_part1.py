def load_input(input_file: str) -> str:
    """Load the puzzle input from the input file and return it as a string."""
    with open(input_file, 'r') as f:
        return f.read()


def parse_input(puzzle_input: str) -> list[tuple[int, int]]:
    """
    Takes input as a string. Returns the list with points as tuple[int, int]
    :param puzzle_input:
    :return:
    """
    split_input: list[str] = puzzle_input.split('\n')

    return list(tuple(map(int, points.split(','))) for points in split_input)


def area_of_rectangle(point1: tuple[int, int], point2: tuple[int, int]) -> int:
    """
        Compute the area of a rectangle defined by two points as opposite corners.
        Includes both corners in width and height calculations.
    """
    return (abs(point2[0] - point1[0]) + 1) * (abs(point2[1] - point1[1]) + 1)


def solution(points: list[tuple[int, int]]) -> int:
    """
    Compute the area of the largest rectangle that can be formed using any two points as opposite corners.
    Each rectangle includes both corner points, so width and height are calculated inclusively.
    """
    maximum_area: int = 0
    n: int = len(points)
    for i in range(n):
        for j in range(i+1,  n):
            maximum_area = max(maximum_area, area_of_rectangle(points[i], points[j]))

    return maximum_area


if __name__ == '__main__':
    loaded_input: str = load_input('input.txt')
    parsed_input: list[tuple[int, int]] = parse_input(loaded_input)

    print(solution(parsed_input))
