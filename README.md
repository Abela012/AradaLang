# AradaLang - አራዳ Programming Language

AradaLang is an educational programming language designed to make programming accessible to Amharic speakers. It allows users to write code using familiar Amharic terms while maintaining the simplicity and power of modern programming concepts.

## Features

- Amharic keywords for basic programming constructs
- Simple and intuitive syntax
- Automatic translation to Python
- Support for basic data types, control structures, and functions
- Built-in support for Amharic text processing

## Installation

1. Make sure you have Python 3.7 or higher installed on your system
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/AradaLang.git
   cd AradaLang
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run an AradaLang program:

```bash
python src/main.py examples/hello.arada
```

## Language Syntax

Here are the current keywords in AradaLang:

- `አስቀምጥ` - Variable declaration (let)
- `አሳይ` - Print statement
- `ድገም` - Loop keyword
- `ጊዜ` - Times (for loop count)
- `ከሆነ` - If statement
- `ካልሆነ` - Else statement
- `ተግባር` - Function declaration
- `ምላሽ` - Return statement

Example program:

```amharic
# Variables
አስቀምጥ መልእክት = "ሰላም ጀማው!"
አሳይ(መልእክት)

# Loop example
ድገም 3 ጊዜ {
    አሳይ("እንደገና!")
}

# If-else example
አስቀምጥ ቁጥር = 42
ከሆነ ቁጥር > 10 {
    አሳይ("ግብዳ ቁጥር ነው")
} ካልሆነ {
    አሳይ("ፈላ ቁጥር ነው")
}

# Function example
ተግባር ድምር(x, y) {
    ምላሽ x + y
}
```

## Project Structure

```
AradaLang/
├── src/
│   ├── lexer.py        # Tokenizer for AradaLang
│   ├── parser.py       # Parser that converts tokens to AST
│   ├── translator.py   # Converts AradaLang AST to Python code
│   └── main.py         # Main entry point
├── examples/           # Example programs written in AradaLang
├── docs/              # Documentation
└── requirements.txt    # Python dependencies
```

## Contributing

Contributions are welcome! Please read our contributing guidelines before submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 