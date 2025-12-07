import os

from dotenv import load_dotenv

from utils.aoc_utils import AOCDay, Input


class Day06(AOCDay):
    expected_example_part1_result = 4277556
    expected_example_part2_result = 3263827

    def part1(self, data: Input) -> int:
        input_matrix = [list(map(str, line.split())) for line in data.lines]
        total_result = 0
        for column_index, column in enumerate(input_matrix[-1]):
            column_result = 1 if column == "*" else 0
            for row in input_matrix[:-1]:
                if column == "*":
                    column_result *= int(row[column_index])
                if column == "+":
                    column_result += int(row[column_index])
            total_result += column_result
        return total_result

    def part2(self, data: Input) -> int:
        input_matrix = data.lines
        max_length = max(len(line) for line in input_matrix)
        total_result = 0
        operation_result = 0
        operation = ""
        for column_index in range(max_length):
            column = input_matrix[-1][column_index] if column_index < len(input_matrix[-1]) else " "
            if column in ("*", "+"):
                total_result += operation_result
                operation = column
                operation_result = 1 if column == "*" else 0
            current_number_list = []
            for row in input_matrix[:-1]:
                if len(row) <= column_index or row[column_index] == " ":
                    continue
                current_number_list.append(row[column_index])
            if current_number_list:
                current_number: int = int("".join(current_number_list))
                if operation == "*":
                    operation_result *= current_number
                elif operation == "+":
                    operation_result += current_number
        total_result += operation_result

        return total_result


if __name__ == "__main__":
    load_dotenv()
    year = os.getenv('AOC_YEAR')
    session_token = os.getenv('AOC_SESSION_COOKIE')
    day_number = "06"
    day = Day06(year, day_number, session_token)
    day.run()
