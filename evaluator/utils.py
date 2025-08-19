##
## EPITECH PROJECT, 2025
## evaluator_py
## File description:
## utils
##

import sys


class in_colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def some_info():
    if len(sys.argv) > 1:
        try:
            if sys.argv[1] == "--show-steps":
                more_steps = True
            if not more_steps or "-h" in sys.argv:
                print(
                    "here some help:",
                    "You can launch the calculator with --show-steps for more explanation how it thinks",
                    file=sys.stdout,
                )
        except Exception as error:
            print(error, file=sys.stderr)
            exit(84)


def close_program_because_of_error(error_msg: str, error_value: int) -> None:
    print(f"{in_colors.FAIL}ERROR: [{error_msg}]", file=sys.stderr)
    if not error_value:
        exit(84)
    exit(error_value)
