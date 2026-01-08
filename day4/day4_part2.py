from day4_part1 import load_input, Grid


def remove_all_accessible_papers(grid: Grid) -> int:
    """
        Remove all rolls of paper accessible to forklifts in iterative rounds.

        A roll of paper is accessible if it has fewer than 4 neighboring rolls.
        After each removal, the grid is updated, possibly unlocking new accessible rolls.

        Returns the total number of rolls removed.
    """
    result: int = 0
    removed_this_round: bool = True

    while removed_this_round:
        removed_this_round = False
        papers: list[tuple[int, int]] = grid.get_all_paper_positions()
        for paper_position in papers:
            if grid.get_neighbours(paper_position[0], paper_position[1]) < 4:
                grid.set_element(paper_position[0], paper_position[1], '.')
                result += 1
                removed_this_round = True

    return result


if __name__ == '__main__':
    loaded_input: str = load_input('input.txt')
    grid: Grid = Grid(loaded_input)

    print(remove_all_accessible_papers(grid))
