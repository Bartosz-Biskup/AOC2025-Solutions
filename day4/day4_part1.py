def load_input(input_file: str) -> str:
    """Load the puzzle input from the input file and return it as a string."""
    with open(input_file, 'r') as f:
        return f.read()


PAPER: str = "@"
EMPTY: str = "."


class Grid:
    def __init__(self, grid: str) -> None:
        self.grid: list[list[str]] = [list(i) for i in grid.split("\n")]
        self.size_x: int = len(self.grid[0])
        self.size_y: int = len(self.grid)

    def get_element(self, x: int, y: int) -> bool:
        """
        returns if with index (x, y) is equal to '@' symbol. If an element is out of grid's range returns False.
        """
        if  not (0 <= x < self.size_x and 0 <= y < self.size_y):
            return False

        return self.grid[x][y] == PAPER

    def set_element(self, x: int, y: int, value: str = EMPTY) -> None:
        """
        sets an element at specified index (x, y) to be a specified string, '.' on default.
        """
        if  not (0 <= x < self.size_x and 0 <= y < self.size_y):
            return

        self.grid[x][y] = value

    def get_all_paper_positions(self) -> list[tuple[int, int]]:
        """
        returns all indexes(tuple[int, int]) for which get_element method returns True.
        :return:
        """
        result: list[tuple[int, int]] = []
        for x in range(0, self.size_x):
            for y in range(0, self.size_y):
                if self.get_element(x, y):
                    result.append((x, y))
        return result

    def get_neighbours(self, x: int, y: int) -> int:
        """
        returns amount of specified element's (x, y) neighbours for which get_element returns True
        """
        result: int = 0

        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if (i, j) == (x, y):
                    continue

                if self.get_element(i, j):
                    result += 1

        return result


def count_accessible_paper(grid: Grid) -> int:
    """
    returns all accessible rolls of paper. 'Accessible' meaning here: 'https://adventofcode.com/2025/day/4'
    :param grid:
    :return:
    """
    all_true: list[tuple[int, int]] = grid.get_all_paper_positions()
    result: int = 0

    for i in all_true:
        if grid.get_neighbours(i[0], i[1]) < 4:
            result += 1

    return result


if __name__ == '__main__':
    loaded_input: str = load_input('input.txt')
    grid: Grid = Grid(loaded_input)

    print(count_accessible_paper(grid))
