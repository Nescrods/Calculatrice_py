##
## EPITECH PROJECT, 2025
## evaluator_py
## File description:
## lexer
##

import tokens as t
import utils


class Lexer:
    def __init__(self, usr_input: str) -> None:
        self.list_of_tokens: list[str] = []

        print(f"Lexer call -- reçu: {usr_input}\n")
        self.list_of_tokens = self.tokeniser(usr_input)
        self.print_list_of_tokens(tuple(self.list_of_tokens))
        self.return_list()

    def get_number(self, to_found: list | tuple) -> tuple[float | int, int] | None:
        iteration: int = 0
        number: int | float = 0
        i: int = 10

        for char in to_found:
            if char.isdigit() and type(number) is int:
                number = number * 10 + int(char)
            elif char.isdigit() and type(number) is float:
                number += int(char) / i
                i *= 10
            elif char in t.decimal_ponctuation and type(number) is not float:
                number = float(number)
            else:
                break
            iteration += 1
        return (number, iteration)  # return du nbr et du nbr d'iterations de i pour sauter le nbr précedement créé

    def tokeniser(self, usr_input: str) -> list:
        # suppretion tout les espaces pour avoir une str clean (évite de traiter des t.tokens inutiles)
        usr_input = usr_input.replace(" ", "")
        list_of_tokens: list = []
        tmp_tuple: tuple | None = (float | int, int)
        i: int = 0

        while i < len(usr_input):
            # ajoute à ma liste tout les t.tokens qui se trouvent dans la liste ligne 11 (t.tokens)
            if (usr_input[i] in t.tokens and usr_input[i] not in t.decimal_ponctuation):
                list_of_tokens.append(usr_input[i])
            elif (
                usr_input[i] in t.decimal_ponctuation
            ):  # evite les erreurs du à la ponctuation des chiffres à virgules
                continue
            elif (
                usr_input[i].isdigit() or usr_input[i] in t.decimal_ponctuation
            ):  # get les chiffres
                tmp_tuple = self.get_number(usr_input[i:])
                list_of_tokens.append(tmp_tuple[0])
                i = i + tmp_tuple[1]
                continue
            elif usr_input[i].islower() or usr_input[i].isupper():  # get les chars
                list_of_tokens.append(usr_input[i])
                t.list_of_unknows.append(usr_input[i])
                i = i + 1
                continue
            else:
                utils.close_program_because_of_error(
                    f"Idk what is: {usr_input[i]}", 84
                )  # si n'est pas rentré dans les cas précédants arrete l'execution
            i += 1
        return list_of_tokens

    def print_list_of_tokens(self, list_of_tokens: tuple) -> None:
        for elements in list_of_tokens:
            print(f"Lexer get: {elements}")
        if not list_of_tokens:
            print("no list content")

    def return_list(self):
        return self.list_of_tokens
