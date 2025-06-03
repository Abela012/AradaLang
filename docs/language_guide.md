# AradaLang Documentation

## Introduction
AradaLang is a programming language designed to make programming accessible to Amharic speakers. It uses Amharic keywords while maintaining the power and simplicity of modern programming concepts.

## Installation

1. Make sure you have Python 3.7 or higher installed
2. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AradaLang.git
   cd AradaLang
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Programs
To run an AradaLang program:
```bash
python src/main.py your_program.arada
```

## Language Features

### 1. Variables
Variables are declared using the `አስቀምጥ` keyword:
```amharic
አስቀምጥ ስም = "ቤላ"
አስቀምጥ ቁጥር = 42
አስቀምጥ ፍሎት = 10.5
```

### 2. Output
Use `አሳይ` to print values:
```amharic
አሳይ("ሰላም ዓለም!")
አሳይ(ቁጥር)
```

### 3. Control Structures

#### If-Else Statements
```amharic
ከሆነ ቁጥር > 10 {
    አሳይ("ግብዳ ቁጥር ነው")
} ካልሆነ {
    አሳይ("ፈላ ቁጥር ነው")
}
```

#### For Loops
```amharic
ድገም 5 ጊዜ {
    አሳይ("እንደገና!")
}
```

#### While Loops
```amharic
አስቀምጥ ቁጥር = 10
እስከ ቁጥር > 0 {
    አሳይ(ቁጥር)
    ቁጥር = ቁጥር - 1
}
```

### 4. Functions
Functions are defined using the `ተግባር` keyword:
```amharic
ተግባር ድምር(x, y) {
    ምላሽ x + y
}

# Function call
አስቀምጥ ውጤት = ድምር(5, 7)
አሳይ(ውጤት)
```

### 5. Data Types
AradaLang supports:
- Strings (text in quotes)
- Integers (whole numbers)
- Floats (decimal numbers)

### 6. Operators
- Arithmetic: `+`, `-`, `*`, `/`
- Comparison: `>`, `<`, `==`
- Assignment: `=`

## Complete Example
```amharic
# Simple program demonstrating AradaLang features

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

አስቀምጥ ውጤት = ድምር(5, 7)
አሳይ(ውጤት)
```

## Keywords Reference

| Keyword | Meaning | Example |
|---------|---------|---------|
| `አስቀምጥ` | Variable declaration | `አስቀምጥ x = 5` |
| `አሳይ` | Print | `አሳይ(x)` |
| `ድገም` | For loop | `ድገም 5 ጊዜ { }` |
| `ጊዜ` | Times (for loop) | `ድገም 5 ጊዜ { }` |
| `ከሆነ` | If | `ከሆነ x > 5 { }` |
| `ካልሆነ` | Else | `ካልሆነ { }` |
| `ተግባር` | Function | `ተግባር ስም() { }` |
| `ምላሽ` | Return | `ምላሽ x` |
| `እስከ` | While | `እስከ x > 0 { }` |

## Best Practices

1. **Comments**
   - Use `#` for single-line comments
   - Write comments in Amharic or English to explain your code

2. **Variable Names**
   - Use meaningful Amharic names
   - Avoid using reserved keywords as variable names

3. **Code Structure**
   - Use proper indentation
   - Group related code together
   - Use functions to organize code

4. **Error Handling**
   - Check for division by zero
   - Validate input before using it
   - Use if-else statements to handle different cases

## Common Errors and Solutions

1. **Variable Not Found**
   - Make sure to declare variables with `አስቀምጥ` before using them
   - Check for typos in variable names

2. **Syntax Errors**
   - Check for missing curly braces `{}`
   - Ensure proper spacing around operators
   - Verify that all statements end properly

3. **Type Errors**
   - Make sure to use the correct data type for operations
   - Convert between types when necessary

## Contributing
Contributions are welcome! Please read our contributing guidelines before submitting pull requests.

## License
This project is licensed under the MIT License. 