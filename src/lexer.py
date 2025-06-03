from rply import LexerGenerator

class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()
        self._add_tokens()
    
    def _add_tokens(self):
        # Keywords - order matters, put longer tokens first
        keywords = [
            ('FUNCTION', r'ተግባር'),
            ('RETURN', r'ምላሽ'),
            ('PRINT', r'አሳይ'),
            ('LET', r'አስቀምጥ'),
            ('IF', r'ከሆነ'),
            ('ELSE', r'ካልሆነ'),
            ('LOOP', r'ድገም'),
            ('WHILE', r'እስከ'),
            ('TIMES', r'ጊዜ'),
        ]
        
        # Add all keywords
        for name, pattern in keywords:
            self.lexer.add(name, pattern)
        
        # Operators - put longer operators first
        operators = [
            ('EQ', r'=='),
            ('ASSIGN', r'='),
            ('GT', r'>'),
            ('LT', r'<'),
            ('PLUS', r'\+'),
            ('MINUS', r'-'),
            ('MUL', r'\*'),
            ('DIV', r'/'),
        ]
        
        # Add all operators
        for name, pattern in operators:
            self.lexer.add(name, pattern)
        
        # Delimiters
        delimiters = [
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('LBRACE', r'\{'),
            ('RBRACE', r'\}'),
            ('COMMA', r','),
        ]
        
        # Add all delimiters
        for name, pattern in delimiters:
            self.lexer.add(name, pattern)
        
        # Literals
        self.lexer.add('STRING', r'"[^"]*"')
        self.lexer.add('NUMBER', r'\d*\.\d+|\d+')
        
        # Identifiers (must come after keywords)
        self.lexer.add('IDENTIFIER', r'[a-zA-Z_\u1200-\u137F][a-zA-Z0-9_\u1200-\u137F]*')
        
        # Ignore whitespace and comments
        self.lexer.ignore(r'\s+')
        self.lexer.ignore(r'#.*')
        
    def get_lexer(self):
        return self.lexer.build() 