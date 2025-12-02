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
        # Getting input
        input_data = self.read_input()
        test_data = self.read_example()

        part1_example_result = self.part1(test_data)

        startTime = time.time()
        part1_result = self.part1(input_data)
        part1_time = time.time() - startTime

        part2_example_result = self.part2(test_data)

        startTime = time.time()
        part2_result = self.part2(input_data)
        part2_time = time.time() - startTime

        # Writing output
        self.write_output(
            f"====================== Day {self.day_number} ======================",
            f"Part 1 Example Result: {part1_example_result} "+
            (f"\033[92m(OK)\033[0m" if part1_example_result == self.expected_example_part1_result else f"\033[91m(Expected {self.expected_example_part1_result})\033[0m"),
            f"Part 1 Result: {part1_result}",
            f"Time (ms): {part1_time}",
            f"---------------------------------------------------",
            f"Part 2 Example Result: {part2_example_result} "+
            (f"\033[92m(OK)\033[0m" if part2_example_result == self.expected_example_part2_result else f"\033[91m(Expected {self.expected_example_part2_result})\033[0m"),
            f"Part 2 Result: {part2_result}",
            f"Time (ms): {part2_time}",
        )

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
            raise ConnectionError("Could not connect to AoC website to download input data. "
                                  "Error code {}: {}".format(result.status_code, result.text))

    def read_example(self) -> Input:
        example_path = os.path.join(self.get_path(), "example.txt")
        if not os.path.exists(example_path):
            with open(example_path, "w") as file:
                file.write("")

        return Input(example_path)

    def get_path(self) -> str:
        return os.path.dirname(os.path.abspath(sys.modules[self.__class__.__module__].__file__))

    def write_output(self, *args):
        # Concats all the args into one string
        str_to_write = ""
        for arg in args:
            str_to_write += str(arg) + "\n"

        # Writes to console
        sys.stdout.write(str_to_write)
        output_path = os.path.join(self.get_path(), "output.txt")
        # Writes to file
        file = open(output_path, "w")
        file.write(str_to_write)
        file.close()

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
