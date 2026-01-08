from typing import Final
from functools import cache


def load_input(input_file: str) -> str:
    """Load the puzzle input from the input file and return it as a string."""
    with open(input_file, 'r') as f:
        return f.read()


def parse_input(puzzle_input: str) -> dict[str, list[str]]:
    """
        Takes in the raw input. Returns the graph as a dict where the key is the edge and the value is list of all other
        edges it is connected to.
    """
    def parse_single_device(device: str) -> tuple[str, list[str]]:
        input_device: str = device.split(':', 1)[0]
        output_devices: list[str] = device.split(':')[1].split()

        return input_device, output_devices

    graph: dict[str, list[str]] = {src: dests for src, dests in map(parse_single_device, puzzle_input.split('\n'))}
    return graph


devices: dict[str, list[str]] = parse_input(load_input('input.txt'))


@cache
def solution(source: str, destination: str) -> int:
    """
    Recursively finds and returns all the paths from the source to the destination. Doesn't check for cycles because
    AOC input doesn't contain them.
    """
    if source == destination:
        return 1
    return sum(solution(src, destination) for src in devices.get(source, []))


if __name__ == '__main__':
    SOURCE: Final[str] = 'you'
    DESTINATION: Final[str] = 'out'

    print(solution(SOURCE, DESTINATION))