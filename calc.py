##
## PERSONNAL PROJECT, 2025
## calculatrice
## File description:
## just a project to learn more about py and classes
##

import sys
import time

tokens_priorities: tuple = ('(', ')')
tokens_operators:tuple = ('+', '-', '*', '/', ':', '=')
tokens:tuple = tokens_priorities + tokens_operators

decimal_ponctuation:tuple = (',', '.')

class Lexer:
    def __init__ (self, usr_input:str)->None:
        self.list_of_tokens:list = []

        print("Lexer call --\n")
        self.list_of_tokens = self.tokeniser(usr_input)
        # self.print_list_of_tokens(tuple(self.list_of_tokens))
        self.return_list()


    def __list__ (self)->list:
        return self.list_of_tokens


    def get_number(self, to_found:list|tuple)->tuple[float|int, int]|None:
        iteration:int = 0
        number:int = 0
        i:int = 10

        for char in to_found:
            if (char.isdigit() and type(number) is int):
                number = number * 10 + int(char)    # ajout au chiffre
            elif (char.isdigit() and type(number) is float):
                number += (int(char) / i)           # ajout au float
                i *= 10
            elif (char in decimal_ponctuation and type(number) is not float):
                number = float(number)              # transformation de mon nombre en float
            else:
                break                               # fin de boucle rien à get
            iteration += 1
        return (number, iteration)                  # return du nbr et du nbr d'iterations de i pour sauter le nbr précedement créé


    def tokeniser(self, usr_input:str)->list:
        usr_input = usr_input.replace(' ', '')      # suppretion tout les espaces pour avoir une str clean (évite de traiter des tokens inutiles)
        list_of_tokens:list = []
        tmp_tuple:tuple = (float|int, int)
        i:int = 0

        while i < len(usr_input):
            if (usr_input[i] in tokens and usr_input[i] not in decimal_ponctuation):    # ajoute à ma liste tout les tokens qui se trouvent dans la liste ligne 11 (tokens)
                list_of_tokens.append(usr_input[i])
            elif (usr_input[i] in decimal_ponctuation):                                 # evite les erreurs du à la ponctuation des chiffres à virgules 
                continue
            elif (usr_input[i].isdigit() or usr_input[i] in decimal_ponctuation):       # get les chiffres
                tmp_tuple = self.get_number(usr_input[i:])
                list_of_tokens.append(tmp_tuple[0])
                i = i + tmp_tuple[1]
                continue
            elif (usr_input[i].islower() or usr_input[i].isupper()):                    # get les chars
                list_of_tokens.append(usr_input[i])
                i = i + 1
                continue
            else:
                raise Exception(f"IDK what this is... : {usr_input[i]}")                 # si n'est pas rentré dans les cas précédants arrete l'execution
            i += 1
        return list_of_tokens


    def print_list_of_tokens(self, list_of_tokens:tuple)->None:
        for elements in list_of_tokens:
            print(elements)
        if (not list_of_tokens):
            print("no list content")


    def return_list(self):
        return self.list_of_tokens


class Parser:
    def __init__(self, lexer_work:list)->tuple:
        error_msg = ""

        print(f"Parser called -- reçu: {lexer_work}\n")
        error_msg = self.basic_verifications(lexer_work)
        if (error_msg != ""):
            print(error_msg)
            exit(84)
        print(error_msg)


    def basic_verifications(self, lexer_work:list)->str:
        if (not lexer_work or lexer_work == ()):
            return "Tu te fous de moi ? Il n'y à rien qui parvient au Parser"

        if (lexer_work[0] in tokens_operators):
            print(f"commence par une mauvaise opération: {lexer_work[0]}")
            return "Sus"
        for i in range(0, len(lexer_work)):
            if ((i + 1) < len(lexer_work) and (lexer_work[i] in tokens and lexer_work[i + 1] in tokens)):
                print(f"error : [{lexer_work[i:i+2]}] : deux tokens d'affilés, c'est suspect...")
                return "Sus"
        return ""


class Ast:
    def __init__(self):
        print("Ast called --\n")
    # if (steps > 0):
    #     print("More steps in the printing !")
    pass


def some_info():
    if (len(sys.argv) > 1):
        try:
            if (sys.argv[1] == "--show-steps"):
                more_steps = True
            if (not more_steps or "-h" in sys.argv):
                print("here some help:", "You can launch the calculator with --show-steps for more explanation how it thinks", file=sys.stdout)
        except Exception as error:
            print(error, file=sys.stderr)
            exit(84)


if (__name__ == "__main__"):
    usr_input = input("Enter your calculation: ")
    program_time = time.time()

    lexer_work = Lexer(usr_input)
    # print(lexer_work)
    parser_assembly:tuple = Parser(lexer_work=lexer_work.return_list())

    print(f"\n\nmon temmps = {round(time.time() - program_time, 3)}")
