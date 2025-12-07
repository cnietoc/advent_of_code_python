import os

from dotenv import load_dotenv

from utils.aoc_utils import AOCDay, Input


def remove_rolls(lines: list[str]) -> tuple[int, list[str]]:
    final_lines = []
    count_total = 0
    for line_number, line in enumerate(lines):
        final_line = ""
        for char_index, char in enumerate(line):
            if char == "@":
                count_rolls = 0
                # check W
                if char_index > 0 and line[char_index - 1] == "@":
                    count_rolls += 1
                # check E
                if char_index < len(line) - 1 and line[char_index + 1] == "@":
                    count_rolls += 1
                # check NW
                if line_number > 0 and char_index > 0 and lines[line_number - 1][char_index - 1] == "@":
                    count_rolls += 1
                # check N
                if line_number > 0 and lines[line_number - 1][char_index] == "@":
                    count_rolls += 1
                # check NE
                if line_number > 0 and char_index < len(line) - 1 and lines[line_number - 1][char_index + 1] == "@":
                    count_rolls += 1
                # check SW
                if line_number < len(lines) - 1 and char_index > 0 and lines[line_number + 1][
                    char_index - 1] == "@":
                    count_rolls += 1
                # check S
                if line_number < len(lines) - 1 and lines[line_number + 1][char_index] == "@":
                    count_rolls += 1
                # check SE
                if line_number < len(lines) - 1 and char_index < len(line) - 1 and lines[line_number + 1][
                    char_index + 1] == "@":
                    count_rolls += 1
                if count_rolls < 4:
                    count_total += 1
                    char = "x"
            final_line += char
        final_lines.append(final_line)

    print(f"Final processed string (removed {count_total} rolls):")
    for line in final_lines:
        print(line)
    return count_total, final_lines


class Day04(AOCDay):
    expected_example_part1_result = 13
    expected_example_part2_result = 43

    def part1(self, data: Input) -> int:
        count, lines = remove_rolls(data.lines)
        return count

    def part2(self, data: Input) -> int:
        removed_total = 0
        lines = data.lines
        while True:
            removed, lines = remove_rolls(lines)
            removed_total += removed
            if removed == 0:
                break
        return removed_total


if __name__ == "__main__":
    load_dotenv()
    year = os.getenv('AOC_YEAR')
    session_token = os.getenv('AOC_SESSION_COOKIE')
    day_number = "04"
    day = Day04(year, day_number, session_token)
    day.run()
