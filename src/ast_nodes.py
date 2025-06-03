class Node:
    pass

class Number(Node):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return str(self.value)

class String(Node):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return f'"{self.value}"'

class Print(Node):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return f'print({self.value.eval()})'

class BinaryOp(Node):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def eval(self):
        ops = {
            'PLUS': '+',
            'MINUS': '-',
            'MUL': '*',
            'DIV': '/',
            'GT': '>',
            'LT': '<',
            'EQ': '=='
        }
        return f'({self.left.eval()} {ops[self.operator]} {self.right.eval()})'

class Assignment(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def eval(self):
        # Handle the case where name is a token object
        name = self.name.value if hasattr(self.name, 'value') else self.name
        return f'{name} = {self.value.eval()}'

class Variable(Node):
    def __init__(self, name):
        # Handle the case where name is a token object
        self.name = name.value if hasattr(name, 'value') else name

    def eval(self):
        return self.name

class If(Node):
    def __init__(self, condition, true_body, false_body):
        self.condition = condition
        self.true_body = true_body
        self.false_body = false_body

    def eval(self):
        lines = []
        lines.append(f'if {self.condition.eval()}:')
        for stmt in self.true_body:
            for line in stmt.eval().split('\n'):
                lines.append(f'    {line}')
        if self.false_body:
            lines.append('else:')
            for stmt in self.false_body:
                for line in stmt.eval().split('\n'):
                    lines.append(f'    {line}')
        return '\n'.join(lines)

class Loop(Node):
    def __init__(self, times, body):
        self.times = times
        self.body = body

    def eval(self):
        lines = []
        lines.append(f'for _ in range({self.times}):')
        for stmt in self.body:
            for line in stmt.eval().split('\n'):
                lines.append(f'    {line}')
        return '\n'.join(lines)

class While(Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def eval(self):
        lines = []
        lines.append(f'while {self.condition.eval()}:')
        for stmt in self.body:
            for line in stmt.eval().split('\n'):
                lines.append(f'    {line}')
        return '\n'.join(lines)

class Function(Node):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

    def eval(self):
        lines = []
        params_str = ', '.join(self.params)
        lines.append(f'def {self.name}({params_str}):')
        for stmt in self.body:
            for line in stmt.eval().split('\n'):
                lines.append(f'    {line}')
        return '\n'.join(lines)

class Return(Node):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return f'return {self.value.eval()}'

class FunctionCall(Node):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def eval(self):
        args_str = ', '.join(arg.eval() for arg in self.args)
        return f'{self.name}({args_str})' 