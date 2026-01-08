from day8_part1 import load_input, parse_input, UnionFind, all_edges, get_sorted_connections


def solution(puzzle_input: list[tuple[int, int, int]]) -> int:
    """
    Takes in the list of all the points.
    Iterates through all the connection sorted in ascending order by their distance until every single point is connected
    and returns the product of X coordinates of 2 points that make final connection.
    """
    connections: list[tuple[int, int]] = get_sorted_connections(all_edges(1000), puzzle_input)
    union_find: UnionFind = UnionFind(len(puzzle_input))

    circuits: int = len(puzzle_input)
    for a, b in connections:
        if union_find.find(a) == union_find.find(b):
            continue

        union_find.union(a, b)
        circuits -= 1
        if circuits == 1:
            point1, point2 = puzzle_input[a], puzzle_input[b]
            return point1[0] * point2[0]

    return -1


if __name__ == '__main__':
    loaded_input: str = load_input('input.txt')
    parsed_input: list[tuple[int, int, int]] = parse_input(loaded_input)

    print(solution(parsed_input))
