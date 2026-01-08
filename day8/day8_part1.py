from math import hypot


def load_input(input_file: str) -> str:
    """Load the puzzle input from the input file and return it as a string."""
    with open(input_file, 'r') as f:
        return f.read()


def parse_input(puzzle_input: str) -> list[tuple[int, int, int]]:
    split_input: list[str] = puzzle_input.split('\n')
    return [tuple(map(int, i.split(','))) for i in split_input]


def all_edges(n: int) -> list[tuple[int, int]]:
    """
    Takes in amount of points, assumes that they're indexed from 0 to n-1.
    Returns all possible combinations of circuit connections as a list of tuples containing indexes of points.
    """
    return [(i, j) for i in range(n) for j in range(i+1, n)]


def distance(a: int,
             b: int,
             points: list[tuple[int, int, int]]) -> float:
    """
    Return the Euclidean distance between points[a] and points[b].
    """
    return hypot(*[x - y for x, y in zip(points[a], points[b])])


def get_sorted_connections(connections: list[tuple[int, int]],
                           points: list[tuple[int, int, int]]) -> list[tuple[int, int]]:
    """
    Takes in connections as a list of tuples containing indexes of points and a list of points. Sorts it by the Euclidean
    distance in ascending order.
    """
    return sorted(connections, key=lambda connection: distance(connection[0], connection[1], points))


class UnionFind:
    """
    Uses path compression in `find` for efficient connectivity checks.
    Union-by-size was avoided to simplify size tracking for the puzzle requirement.
    """
    def __init__(self, n: int) -> None:
        self.parent: list[int] = list(range(n))

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> None:
        root_a: int = self.find(a)
        root_b: int = self.find(b)

        if root_a != root_b:
            self.parent[root_b] = root_a

    @property
    def sizes(self) -> list[int]:
        sizes: list[int] = [0] * len(self.parent)
        for i in self.parent:
            sizes[self.find(i)] += 1

        return sizes


def solution(puzzle_input: list[tuple[int, int, int]]) -> int:
    """
    Takes in list of the points and return the product of the sizes of three biggest trees after connecting every single
    point using union find algorithm.
    """
    connections: list[tuple[int, int]] = get_sorted_connections(all_edges(len(puzzle_input)), puzzle_input)
    union_find: UnionFind = UnionFind(len(puzzle_input))

    for a, b in connections[:len(puzzle_input)]:
        union_find.union(a, b)

    sizes: list[int] = sorted(union_find.sizes, reverse=True)

    return sizes[0] * sizes[1] * sizes[2]


if __name__ == '__main__':
    loaded_input: str = load_input('input.txt')
    parsed_input: list[tuple[int, int, int]] = parse_input(loaded_input)

    print(solution(parsed_input))