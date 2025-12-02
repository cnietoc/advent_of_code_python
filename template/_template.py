import os

from utils.aoc_utils import AOCDay, Input
from dotenv import load_dotenv

class DayTemplate(AOCDay):
    expected_example_part1_result = 0
    expected_example_part2_result = 0

    def part1(self, data: Input) -> int:
        return 0

    def part2(self, data: Input) -> int:
        return 0

if __name__ == "__main__":
    load_dotenv()
    year = os.getenv('AOC_YEAR')
    session_token = os.getenv('AOC_SESSION_COOKIE')
    day_number = "{day_number}"
    day = DayTemplate(year, day_number, session_token)
    day.run()
