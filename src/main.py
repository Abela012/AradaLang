import sys
from src.translator import Translator

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <source_file>")
        sys.exit(1)

    source_file = sys.argv[1]
    
    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            source_code = f.read()
            
    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    translator = Translator()
    
    try:
        # Translate AradaLang to Python
        python_code = translator.translate(source_code)
        
        # Execute the translated code
        exec(python_code)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 