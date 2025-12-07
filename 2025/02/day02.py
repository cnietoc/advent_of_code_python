import os

from dotenv import load_dotenv

from utils.aoc_utils import AOCDay, Input


class Day02(AOCDay):
    expected_example_part1_result = 1227775554
    expected_example_part2_result = 4174379265

    def part1(self, data: Input) -> int:
        count = 0
        for range_str in data.raw.split(","):
            dash_index = range_str.index("-")
            first = int(range_str[0:dash_index])
            second = int(range_str[dash_index + 1:])
            for (i) in range(first, second + 1):
                number = str(i)
                if len(number) % 2 == 0:
                    half = len(number) // 2
                    left = number[0:half]
                    right = number[half:]
                    if left == right:
                        count += i

        return count

    def part2(self, data: Input) -> int:
        count = 0
        for range_str in data.raw.split(","):
            dash_index = range_str.index("-")
            first = int(range_str[0:dash_index])
            second = int(range_str[dash_index + 1:])
            for (number) in range(first, second + 1):
                number_str = str(number)
                half = len(number_str) // 2
                for number_of_digits in range(1, half + 1):
                    if (len(number_str) % number_of_digits) != 0:
                        continue
                    split_number = [number_str[i:i + number_of_digits] for i in
                                    range(0, len(number_str), number_of_digits)]
                    if all(x == split_number[0] for x in split_number):
                        count += number
                        break

        return count


if __name__ == "__main__":
    load_dotenv()
    year = os.getenv('AOC_YEAR')
    session_token = os.getenv('AOC_SESSION_COOKIE')
    day_number = "02"
    day = Day02(year, day_number, session_token)
    day.run()
