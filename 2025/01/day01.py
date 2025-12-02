import os

from utils.aoc_utils import AOCDay, Input
from dotenv import load_dotenv

class Day01(AOCDay):
    expected_example_part1_result = 3
    expected_example_part2_result = 6

    def part1(self, data: Input):
        dial = 50
        count_of_zeros = 0
        for line in data.lines:
            if line.startswith("L"):
                dial -= int(line[1:])
            elif line.startswith("R"):
                dial += int(line[1:])
            dial = dial % 100
            if dial == 0:
                count_of_zeros = count_of_zeros + 1
        return count_of_zeros

    def part2(self, data: Input):
        dial = Dial()
        for line in data.lines:
            if line.startswith("L"):
                dial.turn_left(int(line[1:]))
            elif line.startswith("R"):
                dial.turn_right(int(line[1:]))
        return dial.count_of_zeros

class Dial:
    def __init__(self):
        self.position = 50
        self.count_of_zeros = 0

    def turn_left(self, steps):
        for _ in range(steps):
            self._turn_left_one()

    def turn_right(self, steps):
        for _ in range(steps):
            self._turn_right_one()

    def _turn_right_one(self):
        self.position += 1
        if self.position >= 100:
            self.position = 0
        if self.position == 0:
            self.count_of_zeros += 1

    def _turn_left_one(self):
        self.position -= 1
        if self.position < 0:
            self.position = 99
        if self.position == 0:
            self.count_of_zeros += 1

if __name__ == "__main__":
    load_dotenv()
    year = os.getenv('AOC_YEAR')
    session_token = os.getenv('AOC_SESSION_COOKIE')
    day_number = "01"
    day = Day01(year, day_number, session_token)
    day.run()
