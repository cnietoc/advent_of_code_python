# Python Framework for Advent Of Code

## What is Advent Of Code?
Advent of code is a series of coding challenges in the form of an advent calendar : One challenge divided in two parts per day from December 1rst up until December 25th [https://adventofcode.com/](https://adventofcode.com/)

## Why this framework?
I created this python AoC framework to handle every basic action that you need to do every single day like :

- Creating your daily solution file that can be ran automatically (from a template)
- Downloading your inputs if its not already there
- Automatically reading the current day input and putting it into a variable that you can use everyday withtout touching your file system
- Executing your solution by part one day at a time or all days at the same time
- Timing the execution of your program to compare run times

## Example usage
- https://github.com/william-fecteau/AdventOfCode

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

## Framework flow
A day file is created with this template :
```python
import os
from utils.aoc_utils import AOCDay, Input
from dotenv import load_dotenv

class DayTemplate(AOCDay):
    expected_example_part1_result = 0
    expected_example_part2_result = 0

    def part1(self, input_data: Input) -> int:
        # input_data.data contains the list of every line from your input (split on '\n')
        # input_data.raw_data contains all the data in a single string (including all '\n')
        return 0

    def part2(self, input_data: Input) -> int:
        return 0

if __name__ == "__main__":
    load_dotenv()
    year = os.getenv('AOC_YEAR')
    session_token = os.getenv('AOC_SESSION_COOKIE')
    day_number = "01"  # This will be replaced with the actual day number
    day = DayTemplate(year, day_number, session_token)
    day.run()
```

**Features:**
- `input_data.data` - List of lines from the input file (without '\n')
- `input_data.raw_data` - Complete string with all content (including '\n')
- `expected_example_part1_result` and `expected_example_part2_result` - Expected values to automatically validate examples
- The framework automatically runs both parts with `example.txt` and `input.txt`, showing results and execution times
- Each day file can be run independently from the IDE thanks to the `if __name__ == "__main__"` block


## How to use it
### Start a day
To start a day, use this command: ```uv run main.py <dayNumber>```

If the day file doesn't exist, it will be automatically created from the template.

Your day file will be located at: ```./<year>/<dayNumber>/day<dayNumber>.py``` (This is where you program!)

### Run a day
To run a day, use the same command: ```uv run main.py <dayNumber>```

The framework will execute your solution and:
1. Automatically download `input.txt` if it doesn't exist (requires AOC_SESSION_COOKIE)
2. Create an empty `example.txt` if it doesn't exist (you must fill it with the problem's example)
3. Run both parts with the example and validate against expected values (showing ✓ in green or ✗ in red)
4. Run both parts with the real input
5. Display execution times for each part
6. Save the output to ```./<year>/<dayNumber>/output.txt```

**Generated files:**
- ```./<year>/<dayNumber>/day<dayNumber>.py``` - Your code
- ```./<year>/<dayNumber>/input.txt``` - Automatic input from AoC
- ```./<year>/<dayNumber>/example.txt``` - Example (you fill this manually)
- ```./<year>/<dayNumber>/output.txt``` - Execution results

### Run all days
To run all days (1-25): ```uv run main.py all```

### Run from IDE
Each day file can be executed directly from your IDE without using `main.py`. Simply open the day file (e.g., `./2025/01/day01.py`) and run it directly. The `if __name__ == "__main__"` block will handle loading the environment variables and executing the solution.

**Note:** Make sure your `.env` file is properly configured with `AOC_YEAR` and `AOC_SESSION_COOKIE` before running from the IDE.

