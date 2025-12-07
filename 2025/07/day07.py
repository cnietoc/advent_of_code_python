import os
from functools import lru_cache

from dotenv import load_dotenv

from utils.aoc_utils import AOCDay, Input


class Day07(AOCDay):
    expected_example_part1_result = 21
    expected_example_part2_result = 40

    def part1(self, data: Input) -> int:
        diagram = [list(line) for line in data.lines]

        def _print_diagram(title, diagram):
            diagram_str = "\n".join("".join(line) for line in diagram)
            print(f"\n{title}\n{diagram_str}\n")

        _print_diagram("Initial diagram:", diagram)
        split_count = 0
        for line_index, line in enumerate(diagram):
            for char_index, char in enumerate(line):
                if char in ("|", "S"):
                    if line_index + 1 < len(diagram):
                        if diagram[line_index + 1][char_index] == ".":
                            diagram[line_index + 1][char_index] = "|"
                        if diagram[line_index + 1][char_index] == "^":
                            split_count += 1
                            diagram[line_index + 1][char_index - 1] = "|"
                            diagram[line_index + 1][char_index + 1] = "|"

        _print_diagram("Final diagram:", diagram)
        return split_count

    def part2(self, data: Input) -> int:
        diagram = tuple(line for line in data.lines)
        tachyon_index = diagram[0].index("S")

        @lru_cache(maxsize=None)
        def _process_diagram(line_index, current_tachyon_index) -> int:
            realities = 1
            diagram_len = len(diagram)

            for current_line in range(line_index, diagram_len):
                cell = diagram[current_line][current_tachyon_index]
                if cell == "^":
                    realities += _process_diagram(current_line + 1, current_tachyon_index + 1)
                    current_tachyon_index -= 1

            return realities

        return _process_diagram(1, tachyon_index)


if __name__ == "__main__":
    load_dotenv()
    year = os.getenv('AOC_YEAR')
    session_token = os.getenv('AOC_SESSION_COOKIE')
    day_number = "07"
    day = Day07(year, day_number, session_token)
    day.run()
