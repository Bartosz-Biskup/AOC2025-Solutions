from itertools import chain, combinations
from typing import Iterable, Any


def get_all_subsets(iterable: Iterable[Any]) -> list[tuple[Any]]:
    """
        Generate all possible subsets of the given iterable.

        Includes the empty subset and the full set.
        Subsets are returned as tuples to ensure immutability.
    """
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))


def get_all_combinations_of_buttons(amount_of_buttons: int) -> list[tuple[int, ...]]:
    """
        Generate all possible combinations of button indices.

        Each combination represents a set of buttons pressed exactly once.
    """
    return get_all_subsets(range(amount_of_buttons))


def load_input(input_file: str) -> str:
    """Load the puzzle input from the input file and return it as a string."""
    with open(input_file, 'r') as f:
        return f.read()


def get_turn_lights_after_clicking_buttons(buttons_to_be_clicked: tuple[int, ...],
                                           all_buttons: list[tuple[int, ...]],
                                           amount_of_lights: int) -> list[bool]:
    """
        Simulate the effect of pressing a given set of buttons.

        All lights start turned off. Each button toggles the state of the lights
        it is wired to. Returns the final light configuration.
    """
    lights: list[bool] = [False] * amount_of_lights

    for index, button in enumerate(all_buttons):
        if index in buttons_to_be_clicked:
            for i in button:
                lights[i] = not lights[i]

    return lights


def parse_input(puzzle_input: str) -> list[tuple[list[bool], list[tuple[int, ...]], list[int]]]:
    """
        Parse the raw puzzle input into a structured machine descriptions.

        Each is machine is represented as:
        - expected light configuration [list[bool]]
        - button wiring [list[tuple[int, ...]]]
        - joltage requirements [list[int]] (In the first part of solution it is not used)

        Returns the list of tuples. Each tuple contains machine's configuration.

        Since the input is simple we don't use regex expressions.
    """
    def parse_single_line(line: str) -> tuple[list[bool], list[tuple[int, ...]], list[int]]:
        """
            Parses single machine's raw input into a tuple containing machine's info.
        """
        lights_str: str = line[1:line.index(']')]
        buttons_str: str = line[line.index('('):line.index('{')-1]
        joltage_requirements_str: str = line[line.index('{'):]

        lights: list[bool] = [light=='#' for light in lights_str]

        buttons_list: list[str] = buttons_str.split()
        buttons_list = [i.replace('(', '').replace(')', '') for i in buttons_list]
        buttons: list[tuple[int, ...]] = [tuple(map(int, i.split(','))) for i in buttons_list]

        joltage_requirements: list[int] = list(map(int, joltage_requirements_str.replace('{', '').
                                                  replace('}', '').
                                                  split(',')))

        return lights, buttons, joltage_requirements

    return list(map(parse_single_line, puzzle_input.split('\n')))


# NOTE:
# Each machine has a very small number of buttons (<= ~7),
# so enumerating all 2^n button combinations is feasible here.
# This trades optimal asymptotic complexity for clarity and correctness.
def solution(puzzle_input: list[tuple[list[bool], list[tuple[int, ...]], list[int]]]) -> int:
    """
    Takes in the puzzle parsed input and returns sum of minimum amounts of clicks required to configure all the machines.
    """
    def min_presses_for_machine(expected_lights_to_be_turned_on: list[bool],
                                                 buttons: list[tuple[int, ...]]) -> int:
        """
        Takes in machines' expected lights to be turned on and the list of machine's buttons and returns minimum
        amount of clicks needed to configure the machine as an integer.
        """
        minimum_amount_of_clicks_needed: int = -1
        for combination in get_all_combinations_of_buttons(len(buttons)):
            clicking_combination_result: list[bool] = get_turn_lights_after_clicking_buttons(combination,
                                                                                             buttons,
                                                                                             len(expected_lights_to_be_turned_on))
            if clicking_combination_result != expected_lights_to_be_turned_on:
                continue

            if minimum_amount_of_clicks_needed == -1 or len(combination) < minimum_amount_of_clicks_needed:
                minimum_amount_of_clicks_needed = len(combination)

        return minimum_amount_of_clicks_needed

    return sum(min_presses_for_machine(lights, buttons) for lights, buttons, _ in puzzle_input)


if __name__ == '__main__':
    loaded_input: str = load_input('input.txt')
    parsed_input: list[tuple[list[bool], list[tuple[int, ...]], list[int]]] = parse_input(loaded_input)

    print(solution(parsed_input))