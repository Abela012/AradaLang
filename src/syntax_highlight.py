from colorama import init, Fore, Style

# Initialize colorama
init()

# Define colors for different token types
COLORS = {
    'KEYWORD': Fore.CYAN,  # Cyan for keywords
    'STRING': Fore.GREEN,  # Green for strings
    'NUMBER': Fore.YELLOW, # Yellow for numbers
    'OPERATOR': Fore.RED,  # Red for operators
    'DEFAULT': Fore.WHITE  # White for everything else
}

# AradaLang keywords
KEYWORDS = {
    'አስቀምጥ': 'KEYWORD',
    'አሳይ': 'KEYWORD',
    'ድገም': 'KEYWORD',
    'ጊዜ': 'KEYWORD',
    'ከሆነ': 'KEYWORD',
    'ካልሆነ': 'KEYWORD',
    'ተግባር': 'KEYWORD',
    'ምላሽ': 'KEYWORD',
    'እስከ': 'KEYWORD'  # While loop keyword
}

def highlight_code(code):
    """Add syntax highlighting to AradaLang code."""
    lines = code.split('\n')
    highlighted_lines = []
    
    for line in lines:
        # Skip comments
        if line.strip().startswith('#'):
            highlighted_lines.append(Fore.BLUE + line + Style.RESET_ALL)
            continue
            
        # Split the line into tokens
        tokens = line.split()
        highlighted_tokens = []
        
        for token in tokens:
            # Check if token is a keyword
            if token in KEYWORDS:
                highlighted_tokens.append(COLORS['KEYWORD'] + token + Style.RESET_ALL)
            # Check if token is a string
            elif token.startswith('"') and token.endswith('"'):
                highlighted_tokens.append(COLORS['STRING'] + token + Style.RESET_ALL)
            # Check if token is a number
            elif token.replace('.', '').isdigit():
                highlighted_tokens.append(COLORS['NUMBER'] + token + Style.RESET_ALL)
            # Check if token is an operator
            elif token in ['+', '-', '*', '/', '>', '<', '=', '==']:
                highlighted_tokens.append(COLORS['OPERATOR'] + token + Style.RESET_ALL)
            else:
                highlighted_tokens.append(COLORS['DEFAULT'] + token + Style.RESET_ALL)
        
        highlighted_lines.append(' '.join(highlighted_tokens))
    
    return '\n'.join(highlighted_lines) 