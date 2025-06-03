# AradaLang Quick Start Guide

## Installation
```bash
# Clone the repository
git clone https://github.com/Abela012/AradaLang.git
cd AradaLang

# Install dependencies
pip install -r requirements.txt
```

## Your First Program
Create a file named `hello.arada`:
```amharic
# My first AradaLang program
አስቀምጥ መልእክት = "ሰላም ዓለም!"
አሳይ(መልእክት)
```

Run it:
```bash
python src/main.py hello.arada
```

## Basic Syntax

### Variables
```amharic
አስቀምጥ ስም = "ቤላ"
አስቀምጥ ቁጥር = 42
```

### If Statement
```amharic
ከሆነ ቁጥር > 10 {
    አሳይ("ግብዳ ቁጥር ነው")
} ካልሆነ {
    አሳይ("ፈላ ቁጥር ነው")
}
```

### Loop
```amharic
ድገም 3 ጊዜ {
    አሳይ("እንደገና!")
}
```

### Function
```amharic
ተግባር ድምር(x, y) {
    ምላሽ x + y
}

አስቀምጥ ውጤት = ድምር(5, 7)
አሳይ(ውጤት)
```

## Next Steps
- Read the full [Language Guide](language_guide.md)
- Try the examples in the `examples` directory
- Create your own programs!

## Need Help?
- Check the [Language Guide](language_guide.md) for detailed documentation
- Look at the example programs in the `examples` directory
- Report issues on GitHub 