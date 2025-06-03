from src.lexer import Lexer
from src.parser import Parser

class Translator:
    def __init__(self):
        self.lexer = Lexer().get_lexer()
        self.parser = Parser().get_parser()

    def translate(self, code):
        # Parse the code
        tokens = self.lexer.lex(code)
        ast = self.parser.parse(tokens)

        # Generate Python code
        python_code = ""
        for node in ast:
            python_code += node.eval() + "\n"

        return python_code 