import os

from dotenv import load_dotenv

from utils.aoc_utils import AOCDay, Input


class Day03(AOCDay):
    expected_example_part1_result = 357
    expected_example_part2_result = 3121910778619

    def part1(self, data: Input) -> int:
        count = 0
        for bank in data.lines:
            max_number = 0

            for first_number_index in range(0, len(bank)):
                first_number = bank[first_number_index]
                for second_number_index in range(first_number_index + 1, len(bank)):
                    second_number = bank[second_number_index]
                    number = int(str(first_number) + str(second_number))
                    if max_number < number:
                        max_number = number
            count += max_number

        return count

    def part2(self, data: Input) -> int:
        count = 0
        for bank in data.lines:
            number = self._process_bank_by_number(bank, 0, -1)
            # print(f"Max number for bank {bank}: {number}")
            count += number

        return count

    def _process_bank_by_number(self, bank, current_number: int, current_index):
        current_length = len(str(current_number))
        if current_length + (len(bank) - current_index - 1) < 12:
            return 0
        for target_number in range(9, -1, -1):
            new_index = bank.find(str(target_number), current_index + 1)
            if new_index != -1:
                new_number = (current_number * 10) + int(bank[new_index])
                if current_length + 1 == 12:
                    return new_number
                number = self._process_bank_by_number(bank, new_number, new_index)
                if number > 0:
                    return number
        return 0

    def part2_(self, data: Input) -> int:
        count = 0
        for bank in data.lines:
            index_array = []
            number = self._process_bank(bank, index_array)
            # print(f"Max number for bank {bank}: {number}")
            count += number

        return count

    def _process_bank(self, bank, index_array):
        max_number = 0
        current_index = index_array[len(index_array) - 1] if len(index_array) > 0 else - 1
        for new_index in range(current_index + 1, len(bank)):
            remaining = len(bank) - new_index
            needed = 12 - len(index_array) - 1
            if remaining < needed:
                break

            index_array.append(new_index)
            # sys.stdout.write(f"\rCurrent array: {index_array}\033[K")
            # sys.stdout.flush()
            if len(index_array) == 12:
                number = 0
                for idx in index_array:
                    number = number * 10 + int(bank[idx])
            else:
                number = self._process_bank(bank, index_array)
            if max_number < number:
                max_number = number
            index_array.pop()
        return max_number


if __name__ == "__main__":
    load_dotenv()
    year = os.getenv('AOC_YEAR')
    session_token = os.getenv('AOC_SESSION_COOKIE')
    day_number = "03"
    day = Day03(year, day_number, session_token)
    day.run()
