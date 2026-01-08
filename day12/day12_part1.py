import re


def load_input(input_file: str) -> str:
    """Load the puzzle input from the input file and return it as a string."""
    with open(input_file, 'r') as f:
        return f.read()


def parse_input(puzzle_input: str) -> ...:
    split_input: list[str] = puzzle_input.split('\n\n')
    grids: str = split_input[-1]

    grids_and_presents: list[tuple[tuple[int, int], int]] = []
    for grid in grids.splitlines():
        numbers_in_grid: list[int] = list(map(int, re.findall(r'\d+', grid)))

        grid_size: tuple[int, int] = tuple(numbers_in_grid[:2])
        amount_of_presents: int = sum(numbers_in_grid[2:])

        grids_and_presents.append((grid_size, amount_of_presents))

    return grids_and_presents


def max_amount_of_presents_that_can_fit_in_grid(grid_x_size: int, grid_y_size: int) -> int:
    return (grid_x_size // 3) * (grid_y_size // 3)


def solution(grids_and_presents: list[tuple[tuple[int, int], int]]) -> int:
    result: int = 0
    for grid, amount_of_presents in grids_and_presents:
        if max_amount_of_presents_that_can_fit_in_grid(*grid) >= amount_of_presents:
            result += 1

    return result


if __name__ == '__main__':
    loaded_input: str = load_input('input.txt')
    grids_and_presents: list[tuple[tuple[int, int], int]] = parse_input(loaded_input)

    print(solution(grids_and_presents))
