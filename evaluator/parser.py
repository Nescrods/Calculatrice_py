##
## EPITECH PROJECT, 2025
## evaluator_py
## File description:
## parser
##


class Parser:
    def __init__(self, lexer_work: list) -> tuple:
        self.error_msg: str = ""
        self.verification_return: tuple = (str, list)
        self.parser_correction: list = lexer_work

        print(f"Parser called -- reçu: {lexer_work}\n")
        verification_return = self.basic_verifications(lexer_work)
        if verification_return[0] != "" or verification_return[1] is None:
            close_program_because_of_error(verification_return[0], 84)

        self.parser_correction = verification_return[1]
        self.return_parser_work()

    def basic_verifications(self, lexer_work: list) -> tuple:
        if not lexer_work:
            return ("Tu te fous de moi ? Il n'y à rien qui parvient au Parser", None)
        if (
            (
                lexer_work[0]
                not in (tokens_positivity + tokens_priorities + tuple(list_of_unknows))
            )
        ) and (type(lexer_work[0]) not in (int, float)):
            return (
                f"Le calcul ne commence pas avec un charactère acceptable: {lexer_work[0]}",
                None,
            )
        for i in range(0, len(lexer_work)):
            lexer_work[i] = self.try_to_number_get_transformed(lexer_work[i:])
        print(f"La liste produite après la transformation en négatif == {lexer_work}")
        return ("", lexer_work)

    def try_to_number_get_transformed(self, rest_of_list: list) -> int | str:
        return "testing the nbr transformation"

    def return_parser_work(self) -> tuple:
        return self.parser_correction
