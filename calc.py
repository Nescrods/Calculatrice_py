##
## PERSONNAL PROJECT, 2025
## calculatrice
## File description:
## just a project to learn more about py and classes
##

import sys
import time
import enum

list_of_unknows:list[str] = []

tokens_positivity:tuple = ('+', '-')
tokens_priorities:tuple = ('(', ')')
tokens_comparaison:tuple = ('=', '>', '<', '!', '[', ']')
tokens_operators:tuple = ('+', '-', '*', '/', ':', '!', '^')

class Tokens(enum.Enum):
    POSITIVE_SIGN = enum.auto()
    NEGATIVE_SIGN = enum.auto()
    BRACKET_L = enum.auto()
    BRACKET_R = enum.auto()
    EQUAL = enum.auto()
    GREATER_THAN_R = enum.auto()
    GREATER_THAN_L = enum.auto()
    NOT = enum.auto()
    SQUARE_BRACKET_L = enum.auto()
    SQUARE_BRACKET_R = enum.auto()
    ADD = enum.auto()
    SUBSTRACT = enum.auto()
    MULTIPLY = enum.auto()
    DIVIDE = enum.auto()
    FACTORIAL = enum.auto()
    POWER = enum.auto()

tokens:tuple = tokens_positivity + tokens_priorities + tokens_comparaison + tokens_operators

decimal_ponctuation:tuple = (',', '.')


class in_colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Lexer:
    def __init__ (self, usr_input:str)->None:
        self.list_of_tokens:list[str] = []

        print(f"Lexer call -- reçu: {usr_input}\n")
        self.list_of_tokens = self.tokeniser(usr_input)
        self.print_list_of_tokens(tuple(self.list_of_tokens))
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
                list_of_unknows.append(usr_input[i])
                i = i + 1
                continue
            else:
                close_program_because_of_error(f"Idk what is: {usr_input[i]}", 84)      # si n'est pas rentré dans les cas précédants arrete l'execution
            i += 1
        return list_of_tokens

    def print_list_of_tokens(self, list_of_tokens:tuple)->None:
        for elements in list_of_tokens:
            print(f"Lexer get: {elements}")
        if (not list_of_tokens):
            print("no list content")

    def return_list(self):
        return self.list_of_tokens


class Parser:
    def __init__(self, lexer_work:list)->tuple:
        self.error_msg:str = ""
        self.verification_return:tuple = (str, list)
        self.parser_correction:list = lexer_work

        print(f"Parser called -- reçu: {lexer_work}\n")
        verification_return = self.basic_verifications(lexer_work)
        if (verification_return[0] != "" or verification_return[1] is None):
            close_program_because_of_error(verification_return[0], 84)

        self.parser_correction = verification_return[1]
        self.return_parser_work()

    def basic_verifications(self, lexer_work:list)->tuple:
        if (not lexer_work):
            return ("Tu te fous de moi ? Il n'y à rien qui parvient au Parser", None)
        if ((lexer_work[0] not in (tokens_positivity + tokens_priorities + tuple(list_of_unknows)))) and (type(lexer_work[0]) not in (int, float)):
            return (f"Le calcul ne commence pas avec un charactère acceptable: {lexer_work[0]}", None)
        for i in range(0, len(lexer_work)):
            lexer_work[i] = self.try_to_number_get_transformed(lexer_work[i:])
        print(f"La liste produite après la transformation en négatif == {lexer_work}")
        return ("", lexer_work)

    def try_to_number_get_transformed(self, rest_of_list:list)->int|str:
        return "testing the nbr transformation"

    def return_parser_work(self)->tuple:
        return self.parser_correction


class Ast:
    def __init__(self):
        print("Ast called --\n")
    # if (steps > 0):
    #     print("More steps in the printing !")
    # doit return un tuple avec un bool (si True ou False, si il i a un comparateur), la réponse du calcul lui meme, une valeur de retour d'erreur (0 par défault) ect ...(j'ai pas d'idées pour l'instant)
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

def close_program_because_of_error(error_msg:str, error_value:int)->None:
    print(f"{in_colors.FAIL}ERROR: [{error_msg}]", file=sys.stderr)
    if (not error_value):
        exit(84)
    exit(error_value)

if (__name__ == "__main__"):
    # usr_input = input("Enter your calculation: ")
    program_time = time.time()

    # lexer_work = Lexer(usr_input)
    # parser_assembly:tuple = Parser(lexer_work=lexer_work.return_list())

    print(Tokens)
    print(f"\n\nmon temmps = {round(time.time() - program_time, 3)}")
