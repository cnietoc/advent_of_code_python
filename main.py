import importlib
import os
import shutil
import sys

from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()  # take environment variables from .env.

    year = os.getenv('AOC_YEAR')
    session_token = os.getenv('AOC_SESSION_COOKIE')
    if year is None or session_token is None or year == "" or session_token == "":
        print("Please set the environment variables AOC_YEAR and AOC_SESSION_COOKIE")
        sys.exit(1)

    # Getting parameters
    runAll = False
    dayNumber = "01"
    if len(sys.argv) >= 2:
        try:
            if sys.argv[1] == "all":
                runAll = True
            else:
                dayNumber = sys.argv[1] if len(sys.argv[1]) == 2 else f"{int(sys.argv[1]):02d}"
        except Exception:
            print("{} - Run aoc solutions".format(sys.argv[0]))
            print("Usage: {} [day]".format(sys.argv[0]))
            sys.exit(1)
    else:
        print("{} - Run aoc solutions".format(sys.argv[0]))
        print("Usage: {} [day]".format(sys.argv[0]))
        sys.exit(1)

    # Create year dir if not existing
    yearDir = os.path.join(os.getcwd(), year)
    os.makedirs(yearDir, exist_ok=True)

    # Validation
    dayPath = os.path.join(yearDir, dayNumber)
    dayFilePath = os.path.join(yearDir, dayNumber, f"day{dayNumber}.py")
    intDayNumber = int(dayNumber)
    if intDayNumber <= 0 or intDayNumber > 25:
        print("Day must be between 0 and 25")
        sys.exit(1)
    # If day file does not exist, create it
    elif not os.path.exists(dayFilePath):
        # Copying template file
        templateFile = os.path.join(os.getcwd(), "template", "_template.py")
        os.makedirs(dayPath, exist_ok=True)
        shutil.copy(templateFile, dayFilePath)

        # Replacing template values
        with open(dayFilePath, "rt") as f:
            data = f.read()

        data = (data
                .replace("@day(0)", f"@day({dayNumber})")
                .replace("DayTemplate", f"Day{dayNumber}")
                .replace("{day_number}", f"{dayNumber}"))

        with open(dayFilePath, "wt") as f:
            f.write(data)

        print("Day " + str(dayNumber) + " created! glhf")

    # Running the day
    if runAll:
        daysRun = ["{:02d}".format(x+1) for x in range(25)]
    else:
        daysRun = [dayNumber]

    for dayNum in daysRun:
        # Getting the good days instance
        try :
            module = importlib.import_module(f"{year}.{dayNum}.day{dayNum}")
            DayClass = getattr(module, f"Day{dayNum}")
            inst = DayClass(year, dayNum, session_token)
            inst.run()
        except ModuleNotFoundError:
            if not runAll:
                print(f"Day {dayNum} not found, exiting...")
                sys.exit(1)
        except Exception as e:
            raise e
