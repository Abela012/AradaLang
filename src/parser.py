from rply import ParserGenerator
from src.ast_nodes import (Number, String, Print, BinaryOp, 
                      Assignment, Variable, If, Loop, While,
                      Function, Return, FunctionCall)

class Parser:
    def __init__(self):
        self.pg = ParserGenerator(
            ['NUMBER', 'STRING', 'PRINT', 'LPAREN', 'RPAREN',
             'PLUS', 'MINUS', 'MUL', 'DIV', 'ASSIGN',
             'IDENTIFIER', 'LET', 'IF', 'ELSE', 'GT', 'LT', 'EQ',
             'LBRACE', 'RBRACE', 'LOOP', 'WHILE', 'TIMES', 'FUNCTION',
             'RETURN', 'COMMA'
            ],
            precedence=[
                ('left', ['PLUS', 'MINUS']),
                ('left', ['MUL', 'DIV']),
                ('left', ['GT', 'LT', 'EQ'])
            ]
        )
        self._define_rules()

    def _define_rules(self):
        @self.pg.production('program : statements')
        def program(p):
            return p[0]

        @self.pg.production('statements : statement')
        def statements_single(p):
            return [p[0]]

        @self.pg.production('statements : statements statement')
        def statements_multiple(p):
            p[0].append(p[1])
            return p[0]

        @self.pg.production('statement : simple_statement')
        @self.pg.production('statement : compound_statement')
        def statement(p):
            return p[0]

        @self.pg.production('simple_statement : PRINT LPAREN expression RPAREN')
        def print_statement(p):
            return Print(p[2])

        @self.pg.production('simple_statement : LET IDENTIFIER ASSIGN expression')
        def let_statement(p):
            return Assignment(p[1].value, p[3])

        @self.pg.production('simple_statement : IDENTIFIER ASSIGN expression')
        def assignment_statement(p):
            return Assignment(p[0].value, p[2])

        @self.pg.production('simple_statement : RETURN expression')
        def return_statement(p):
            return Return(p[1])

        @self.pg.production('compound_statement : IF expression LBRACE statements RBRACE')
        def if_statement(p):
            return If(p[1], p[3], None)

        @self.pg.production('compound_statement : IF expression LBRACE statements RBRACE ELSE LBRACE statements RBRACE')
        def if_else_statement(p):
            return If(p[1], p[3], p[7])

        @self.pg.production('compound_statement : LOOP NUMBER TIMES LBRACE statements RBRACE')
        def loop_statement(p):
            return Loop(int(p[1].value), p[4])

        @self.pg.production('compound_statement : WHILE expression LBRACE statements RBRACE')
        def while_statement(p):
            return While(p[1], p[3])

        @self.pg.production('compound_statement : FUNCTION IDENTIFIER LPAREN param_list RPAREN LBRACE statements RBRACE')
        def function_def(p):
            return Function(p[1].value, p[3], p[6])

        @self.pg.production('param_list : ')
        def empty_params(p):
            return []

        @self.pg.production('param_list : IDENTIFIER')
        def single_param(p):
            return [p[0].value]

        @self.pg.production('param_list : param_list COMMA IDENTIFIER')
        def param_list(p):
            p[0].append(p[2].value)
            return p[0]

        @self.pg.production('expression : term')
        def expression_term(p):
            return p[0]

        @self.pg.production('expression : expression PLUS term')
        @self.pg.production('expression : expression MINUS term')
        def expression_binop(p):
            return BinaryOp(p[0], p[1].gettokentype(), p[2])

        @self.pg.production('term : factor')
        def term_factor(p):
            return p[0]

        @self.pg.production('term : term MUL factor')
        @self.pg.production('term : term DIV factor')
        def term_binop(p):
            return BinaryOp(p[0], p[1].gettokentype(), p[2])

        @self.pg.production('factor : NUMBER')
        def factor_number(p):
            value = p[0].value
            if '.' in value:
                return Number(float(value))
            return Number(int(value))

        @self.pg.production('factor : STRING')
        def factor_string(p):
            return String(p[0].value[1:-1])

        @self.pg.production('factor : IDENTIFIER')
        @self.pg.production('factor : RETURN')  # Allow RETURN token as an identifier
        def factor_variable(p):
            return Variable(p[0].value)

        @self.pg.production('factor : IDENTIFIER LPAREN arg_list RPAREN')
        def factor_call(p):
            return FunctionCall(p[0].value, p[2])

        @self.pg.production('arg_list : ')
        def empty_args(p):
            return []

        @self.pg.production('arg_list : expression')
        def single_arg(p):
            return [p[0]]

        @self.pg.production('arg_list : arg_list COMMA expression')
        def arg_list(p):
            p[0].append(p[2])
            return p[0]

        @self.pg.production('expression : expression GT expression')
        @self.pg.production('expression : expression LT expression')
        @self.pg.production('expression : expression EQ expression')
        def comparison(p):
            return BinaryOp(p[0], p[1].gettokentype(), p[2])

        @self.pg.error
        def error_handler(token):
            source_pos = token.getsourcepos()
            if source_pos:
                raise ValueError(f"Parser Error: Unexpected token {token.name} at line {source_pos.lineno}, column {source_pos.colno}")
            else:
                raise ValueError(f"Parser Error: Unexpected token {token.name}")

    def get_parser(self):
        return self.pg.build() 