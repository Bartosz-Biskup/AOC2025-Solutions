from day10_part1 import load_input, parse_input
import z3


def minimum_clicks_for_machine(machine_buttons: list[tuple[int, ...]],
                               machine_joltages: list[int]) -> int:
    """
    Uses z3 Optimizer to determine the minimum amount of button clicks needed to configure the machine.
    Checks for 2 conditions:
        - Each button must be clicked at least 0 times.
        - the sum of all button clicks referring to a particular joltage requirement must be equal to it.

    Returns the minimum amount of clicks needed to properly configure the machine's joltage.
    """
    o: z3.Optimize = z3.Optimize()
    variables: list[z3.ArithRef] = z3.Ints(f'n{i}' for i in range((len(machine_buttons))))

    for variable in variables:
        o.add(variable >= 0)

    for i, joltage in enumerate(machine_joltages):
        equation: z3.ArithRef = z3.IntVal(0)
        for b, button in enumerate(machine_buttons):
            if i in button: equation += variables[b]
        o.add(equation == joltage)

    o.minimize(sum(variables))

    if o.check() != z3.sat:
        raise ValueError('No solution found for this machine.')

    return o.model().eval(sum(variables)).as_long()


def solution(machines: list[tuple[list[bool], list[tuple[int, ...]], list[int]]]) -> int:
    """
    Returns the minimum amount of clicks needed to properly configure all the machines' joltage.
    """
    return sum(minimum_clicks_for_machine(buttons, joltages) for _, buttons, joltages in machines)

if __name__ == '__main__':
    loaded_input: str = load_input('input.txt')
    parsed_input: list[tuple[list[bool], list[tuple[int, ...]], list[int]]] = parse_input(loaded_input)

    print(solution(parsed_input))
