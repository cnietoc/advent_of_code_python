import os

from utils.aoc_utils import AOCDay, Input
from dotenv import load_dotenv


class Day05(AOCDay):
    expected_example_part1_result = 3
    expected_example_part2_result = 14

    def part1(self, data: Input) -> int:
        ranges = []
        numbers = []
        for line in data.lines:
            if line == "":
                break
            a, b = line.split("-")
            ranges.append((int(a), int(b)))
        for line in data.lines[len(ranges) + 1:]:
            if line == "":
                continue
            numbers.append(int(line))

        spoiled_number = 0
        fresh_number = 0
        for n in numbers:
            fresh = False
            for r in ranges:
                if r[0] <= n <= r[1]:
                    # print(f"Ingredient ID {n} is fresh because it falls into range {r[0]}-{r[1]}.")
                    fresh = True
                    break
            if fresh:
                fresh_number += 1
            else:
                # print(f"Ingredient ID {n} is spoiled.")
                spoiled_number += 1

        return fresh_number

    def part2(self, data: Input) -> int:
        ranges = []
        for line in data.lines:
            if line == "":
                break
            a, b = line.split("-")
            ranges.append((int(a), int(b)))

        merged_ranges = Ranges()
        for r in ranges:
            merged_ranges.add_range(r)
        return merged_ranges.total_covered()


class Ranges:
    def __init__(self):
        self.ranges = []

    def add_range(self, new_range: tuple[int, int]):
        self.ranges.append(new_range)
        self.merge_ranges()

    def merge_ranges(self):
        self.ranges.sort(key=lambda x: x[0])
        merged = []
        for current in self.ranges:
            if not merged or merged[-1][1] < current[0]:
                merged.append(current)
            else:
                merged[-1] = (merged[-1][0], max(merged[-1][1], current[1]))
        self.ranges = merged

    def total_covered(self) -> int:
        total = 0
        for r in self.ranges:
            total += r[1] - r[0] + 1
        return total


if __name__ == "__main__":
    load_dotenv()
    year = os.getenv('AOC_YEAR')
    session_token = os.getenv('AOC_SESSION_COOKIE')
    day_number = "05"
    day = Day05(year, day_number, session_token)
    day.run()
