from day9_part1 import load_input, parse_input, area_of_rectangle
from collections import deque


def make_compressed_grid(points: list[tuple[int, int]]) -> tuple[list[list[int]], list[int], list[int]]:
    """
        Build a compressed grid representation of the red/green tile loop.

        The original coordinates may be very large and sparse. This function performs
        coordinate compression by:
        - Mapping each unique x and y value to a dense index
        - Expanding the grid so that connections between points can be represented

        The resulting grid marks:
        - Red tiles
        - Green tiles connecting consecutive red tiles in the input order

        Returns:
            grid: 2D grid where 1 represents red/green tiles, 0 represents empty space
            xs: Sorted unique x-coordinates used for compression
            ys: Sorted unique y-coordinates used for compression
    """
    xs = sorted({x for x, _ in points})
    ys = sorted({y for _, y in points})
    grid: list[list[int]] = [[0] * (len(ys) * 2 - 1) for _ in range(len(xs) * 2 -1)]

    for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1]):
        cx1, cx2 = sorted([xs.index(x1) * 2, xs.index(x2) * 2])
        cy1, cy2 = sorted([ys.index(y1) * 2, ys.index(y2) * 2])

        for cx in range(cx1, cx2 + 1):
            for cy in range(cy1, cy2 + 1):
                grid[cx][cy] = 1

    return grid, xs, ys


def determine_inside_outside_points(grid: list[list[int]]) -> None:
    """
        Identify interior cells of the loop and mark them as filled.

        A flood-fill (BFS) is performed starting from outside the grid. All reachable
        empty cells are considered "outside". Any cell not reachable from the outside
        is inside the loop and is therefore marked as filled.

        This function mutates the grid in place.
    """
    outside_points: set[tuple[int, int]] = {(-1, -1)}
    d: deque = deque(outside_points)
    while len(d) > 0:
        tx, ty = d.popleft()
        for nx, ny in [(tx+1, ty), (tx-1, ty), (tx, ty+1), (tx, ty-1)]:
            if nx < -1 or ny < -1 or nx > len(grid) or ny > len(grid):
                continue
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                continue

            if (nx, ny) in outside_points:
                continue

            outside_points.add((nx, ny))
            d.append((nx, ny))

    for x in range(len(grid)):
        for y in range(len(grid)):
            if (x, y) not in outside_points:
                grid[x][y] = 1


def construct_psa(grid: list[list[int]]) -> list[list[int]]:
    """
        Construct a 2D prefix sum array (partial sum array).

        The PSA allows querying the sum of any rectangular subgrid in O(1) time,
        which is later used to verify if a rectangle is fully filled with
        red/green tiles.
    """
    psa: list[list[int]] = [[0] * len(row) for row in grid]
    for x in range(len(psa)):
        for y in range(len(psa[0])):
            left: int = psa[x - 1][y] if x > 0 else 0
            top: int = psa[x][y - 1] if y > 0 else 0
            topleft: int = psa[x - 1][y - 1] if x > 0 < y else 0
            psa[x][y] = left + top - topleft + grid[x][y]

    return psa


def valid(psa: list[list[int]],
          x1: int,
          y1: int,
          x2: int,
          y2: int,
          xs: list[int],
          ys: list[int]) -> bool:
    """
        Check whether the rectangle defined by two corner points is fully filled
        with red or green tiles.

        The rectangle is mapped into compressed grid coordinates and validated
        using the prefix sum array.
    """
    cx1, cx2 = sorted([xs.index(x1) * 2, xs.index(x2) * 2])
    cy1, cy2 = sorted([ys.index(y1) * 2, ys.index(y2) * 2])

    left: int = psa[cx1 - 1][cy2] if cx1 > 0 else 0
    top: int = psa[cx2][cy1 -1] if cy1 > 0 else 0
    topleft: int = psa[cx1 - 1][cy1 - 1] if cx1 > 0 < cy1 else 0

    return psa[cx2][cy2] - top - left + topleft == (cx2 - cx1 + 1) * (cy2 - cy1 + 1)


def solution(points: list[tuple[int, int]],
                     psa: list[list[int]],
                     xs: list[int],
                     ys: list[int]) -> int:
    """
        Compute the maximum rectangle area that can be formed using two red tiles
        as opposite corners, such that all tiles inside the rectangle are either
        red or green.
    """
    return max(area_of_rectangle((x1, y1), (x2, y2))
               for i, (x1, y1) in enumerate(points)
               for x2, y2 in points[i:]
               if valid(psa, x1, y1, x2, y2, xs, ys))

if __name__ == '__main__':
    loaded_input: str = load_input('input.txt')
    points: list[tuple[int, int]] = parse_input(loaded_input)
    grid, xs, ys = make_compressed_grid(points)

    determine_inside_outside_points(grid)
    psa: list[list[int]] = construct_psa(grid)

    print(solution(points, psa, xs, ys))
