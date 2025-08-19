##
## EPITECH PROJECT, 2025
## evaluator_py
## File description:
## tokens
##

list_of_unknows: list[str] = []

tokens_positivity: tuple = ("+", "-")
tokens_priorities: tuple = ("(", ")")
tokens_comparaison: tuple = ("=", ">", "<", "!", "[", "]")
tokens_operators: tuple = ("+", "-", "*", "/", ":", "!", "^")

tokens: tuple = (
    tokens_positivity + tokens_priorities + tokens_comparaison + tokens_operators
)

decimal_ponctuation: tuple = (",", ".")
