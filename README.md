# Python Advent Of Code

## Table of Contents
- [What is Advent Of Code?](#what-is-advent-of-code)
- [Installation](#installation)
- [Start a day](#start-a-day)
- [How to implement](#how-to-implement)
- [Run a day](#run-a-day)
- [Run all days](#run-all-days)
- [Run from IDE](#run-from-ide)
- [Acknowledgments](#acknowledgments)

## What is Advent Of Code?
Advent of code is a series of coding challenges in the form of an advent calendar : One challenge divided in two parts per day from December 1rst up until December 25th [https://adventofcode.com/](https://adventofcode.com/)

## Installation
1. Clone the repository
2. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) if you haven't already
3. Install dependencies: ```uv sync```
4. Create a ```.env``` file at the root of the repository
5. In the ```.env``` file, add the following variables:
```
AOC_SESSION_COOKIE=your_session_cookie
AOC_YEAR=2025
```
*Note: You can get your session cookie by logging into the AoC website and looking at the cookies in one of your requests using browser dev tools. This cookie is needed to automatically download your input.*

## Start a day
To start a day, use this command: ```uv run main.py <dayNumber>```

If the day file doesn't exist, it will be automatically created from the template.

Your day file will be located at: ```./<year>/<dayNumber>/day<dayNumber>.py``` (This is where you program!)

## How to implement
Once the day file is created, you can implement your solution by filling in the `part1` and `part2` methods of the `DayTemplate` class.

### day\<dayNumber\>.py
```python
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
    day_number = "{day_number}"  # Replaced when generating a new day from template
    day = DayTemplate(year, day_number, session_token)
    day.run()
```

The template includes:
- A class inheriting from `AOCDay` where you implement `part1` and `part2` methods.
- Expected results for the example input (you must fill these manually after solving the example).
- Execution block to run the day (useful when running directly from IDE).


Each day directory contains the following files:

### Input object
Use the `Input` object provided to `part1` and `part2` to parse your puzzle input efficiently.

Input fields:
- `lines` (list[str]) — one line per input row, with newline characters removed (via `splitlines()`).
- `raw` (str) — the entire input as a single string, exactly as read (including newlines).

### Common patterns

```python
# Parse integers per line
numbers = [int(x) for x in data.lines if x]

# Split by blank lines (very common in AoC)
blocks = data.raw.strip().split("\n\n")

# Parse a grid of characters
grid = [list(row) for row in data.lines]

# Parse coordinates of the form x,y
points = [tuple(map(int, line.split(","))) for line in data.lines]
```

### Input files
- ```./<year>/<dayNumber>/input.txt``` - Your puzzle input (automatically downloaded)
- ```./<year>/<dayNumber>/example.txt``` - Example input (you must fill it with the problem's example)

## Run a day
To run a day, use the same command: ```uv run main.py <dayNumber>```

The framework will execute your solution and:
1. Automatically download `input.txt` if it doesn't exist (requires AOC_SESSION_COOKIE)
2. Create an empty `example.txt` if it doesn't exist (you must fill it with the problem's example)
3. Run both parts with the example and validate against expected values (showing ✓ in green or ✗ in red)
4. Run both parts with the real input
5. Display the results and execution time for each part

## Run all days
To run all days (1-25): ```uv run main.py all```

## Run from IDE
Each day file can be executed directly from your IDE without using `main.py`. Simply open the day file (e.g., `./2025/01/day01.py`) and run it directly. The `if __name__ == "__main__"` block will handle loading the environment variables and executing the solution.

**Note:** Make sure your `.env` file is properly configured with `AOC_YEAR` and `AOC_SESSION_COOKIE` before running from the IDE.

## Acknowledgments
This repository structure was inspired by the [Advent Of Code Python Framework](https://github.com/william-fecteau/AdventOfCodePythonFramework) by William Fecteau.
