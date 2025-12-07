import os
import sys
import time

import requests


class AOCDay:
    year = 2020
    day_number = "00"
    session_token = ""
    expected_example_part1_result = 0
    expected_example_part2_result = 0

    def __init__(self, year, day_number, session_token):
        self.year = int(year)
        self.day_number = str(day_number).zfill(2)
        self.session_token = session_token

    def run(self):
        print("\n" + "=" * 50)
        print(f"\033[96m🎄 Day {self.day_number} of Advent of Code {self.year} 🎄\033[0m")
        print("=" * 50)

        # Getting input
        input_data = self.read_input()
        test_data = self.read_example()

        # Part 1
        print(f"\n\033[93m{'─' * 50}\033[0m")
        print(f"\033[1;93m⭐ PART 1\033[0m")
        print(f"\033[93m{'─' * 50}\033[0m")

        print(f"\n\033[94m📝 Executing example...\033[0m")
        start_time = time.time()
        part1_example_result = self.part1(test_data)
        part1_example_time = (time.time() - start_time) * 1000
        if part1_example_result == self.expected_example_part1_result:
            print(f"   Result: {part1_example_result} \033[92m✓ OK\033[0m")
        else:
            print(f"   Result: {part1_example_result} \033[91m✗ Expected {self.expected_example_part1_result}\033[0m")
        print(f"   ⏱️  Time: \033[95m{part1_example_time:.2f} ms\033[0m")

        print(f"\n\033[94m🚀 Executing input...\033[0m")
        start_time = time.time()
        part1_result = self.part1(input_data)
        part1_time = (time.time() - start_time) * 1000
        print(f"   \033[1mResult: {part1_result}\033[0m")
        print(f"   ⏱️  Time: \033[95m{part1_time:.2f} ms\033[0m")

        # Part 2
        print(f"\n\033[93m{'─' * 50}\033[0m")
        print(f"\033[1;93m⭐⭐ PART 2\033[0m")
        print(f"\033[93m{'─' * 50}\033[0m")

        print(f"\n\033[94m📝 Executing example...\033[0m")
        start_time = time.time()
        part2_example_result = self.part2(test_data)
        part2_example_time = (time.time() - start_time) * 1000
        if part2_example_result == self.expected_example_part2_result:
            print(f"   Result: {part2_example_result} \033[92m✓ OK\033[0m")
        else:
            print(f"   Result: {part2_example_result} \033[91m✗ Expected {self.expected_example_part2_result}\033[0m")
        print(f"   ⏱️  Time: \033[95m{part2_example_time:.2f} ms\033[0m")

        print(f"\n\033[94m🚀 Executing input...\033[0m")
        start_time = time.time()
        part2_result = self.part2(input_data)
        part2_time = (time.time() - start_time) * 1000
        print(f"   \033[1mResult: {part2_result}\033[0m")
        print(f"   ⏱️  Time: \033[95m{part2_time:.2f} ms\033[0m")

        print("\n" + "=" * 50)
        print(f"\033[92m✨ Completed! Total time: {(part1_time + part2_time):.2f} ms ✨\033[0m")
        print("=" * 50 + "\n")

    def read_input(self) -> Input:
        input_path = os.path.join(self.get_path(), "input.txt")
        if not os.path.exists(input_path):
            self.download_input(input_path)

        return Input(input_path)

    def download_input(self, input_path):
        day_num = int(self.day_number)
        url = "https://adventofcode.com/" + \
              str(self.year) + "/day/" + str(day_num) + "/input"
        result = requests.get(url, cookies={'session': self.session_token})
        if result.status_code == 200:
            with open(input_path, 'w') as f:
                f.write(result.text)
        else:
            raise ConnectionError("Could not connect to AoC website to download input data, "
                                  "maybe the day is not yet available? "
                                  "Error code {}: {}".format(result.status_code, result.text))

    def read_example(self) -> Input:
        example_path = os.path.join(self.get_path(), "example.txt")
        if not os.path.exists(example_path):
            with open(example_path, "w") as file:
                file.write("")

        return Input(example_path)

    def get_path(self) -> str:
        return os.path.dirname(os.path.abspath(sys.modules[self.__class__.__module__].__file__))

    def part1(self, data: Input) -> int:
        pass

    def part2(self, data: Input) -> int:
        pass


class Input:
    lines = []
    raw = ""

    def __init__(self, file_path):
        self.read_input(file_path)

    def read_input(self, file_path):
        with open(file_path, 'r') as file:
            self.raw = file.read()
        self.lines = self.raw.splitlines()
