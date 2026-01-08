from day11_part1 import load_input, parse_input, solution


# Since we're guaranteed that the graph doesn't contain any cycles the only orders of visiting these edges
# to get from 'svr' to 'out' through 'dac' and 'fft' are
# 'svr' -> 'dac' -> 'fft' -> 'out' or 'svr' -> 'fft' -> 'dac' -> 'out'.


def solution_for_second_part() -> int:
    return solution('svr', 'dac') * solution('dac', 'fft') * solution('fft', 'out') \
           + solution('svr', 'fft') * solution('fft', 'dac') * solution('dac', 'out')


if __name__ == '__main__':
    print(solution_for_second_part())