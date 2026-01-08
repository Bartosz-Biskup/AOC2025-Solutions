from typing import Optional


def load_input(input_file: str) -> str:
    """Load the puzzle input from the input file and return it as a string."""
    with open(input_file, 'r') as f:
        return f.read()


class Map:
    """
    Class responsible for mapping beam's and splitters' positions and finding ways for the beam to get to the bottom
    """
    def __init__(self, puzzle_input: str) -> None:
        self.puzzle_input = puzzle_input
        self.size: tuple[int, int] = (len(puzzle_input.split('\n')[0]),
                                      len(puzzle_input.split('\n')))
        self._map: list[list[str]] = [list(i) for i in puzzle_input.split('\n')]
        self.visited: list[tuple[int, int]] = []

    @property
    def x_size(self) -> int:
        return self.size[0]

    @property
    def y_size(self) -> int:
        return self.size[1]

    @property
    def starting_point(self) -> tuple[int, int]:
        for index, row in enumerate(self._map, start=0):
            if "S" in row:
                return row.index("S"), index

        raise ValueError("S not found.")

    def has_splitter(self, x: int, y: int) -> bool:
        """
        Returns True if the given point (x, y) is a splitter, otherwise False
        """
        if not 0 <= x <= self.x_size-1 or not 0 <= y <= self.y_size-1:
            raise ValueError('Invalid index.')

        return self._map[y][x] == '^'

    def is_in_bounds(self, x: int, y: int) -> bool:
        """Return True if (x, y) is inside the grid."""
        return 0 <= x < self.x_size and 0 <= y < self.y_size

    def after_split(self, x: int, y: int) -> list[tuple[int, int]]:
        """Return left and right positions if they are within bounds."""
        return [(nx, y) for nx in (x - 1, x + 1) if self.is_in_bounds(nx, y)]

    def simulate(self, starting: Optional[tuple[int, int]]  = None) -> int:
        """
        Solution for the first part of the problem, returns all splits that occur during beam's way to the bottom.
        """
        if starting is None:
            starting: tuple[int, int] = self.starting_point

        while not self.has_splitter(*starting) and not starting[1] == self.y_size-1:
            starting = (starting[0], starting[1]+1)

        if starting[1] == self.y_size - 1 or starting in self.visited:
            return 0

        self.visited.append(starting)
        result: int = 1
        for i in self.after_split(*starting):
            result += self.simulate(i)

        return result

    def amount_of_ways(self) -> int:
        """
        Part 2: Compute total quantum timelines using dynamic programming.

        Returns: Total number of distinct timelines after all splits.
        """
        dp = [0] * self.x_size
        dp[self.starting_point[0]] = 1

        for y in range(self.y_size):
            next_dp = [0] * self.x_size
            for x in range(self.x_size):
                if dp[x] == 0:
                    continue
                if self.has_splitter(x, y):
                    for nx, _ in self.after_split(x, y):
                        next_dp[nx] += dp[x]
                else:
                    next_dp[x] += dp[x]
            dp = next_dp

        return sum(dp)


if __name__ == '__main__':
    loaded_puzzle: str = load_input('input.txt')

    beam_map: Map = Map(loaded_puzzle)

    print(f'Solution for the first part is {beam_map.simulate()}')
    print(f'Solution for the second part is {beam_map.amount_of_ways()}')
