##
## EPITECH PROJECT, 2025
## evaluator_py
## File description:
## main_evaluator
##

import sys
import time

usr_input = input("Enter your calculation: ")
program_time = time.time()

lexer_work = Lexer(usr_input)
parser_assembly: tuple = Parser(lexer_work=lexer_work.return_list())

print(f"\n\nmon temmps = {round(time.time() - program_time, 3)}")
