# Text to Morse Code Converter

A Python application that converts text to Morse code and vice versa.

## Features

- **Text to Morse Code**: Convert plain text into Morse code
- **Morse Code to Text**: Decode Morse code back into readable text
- **Support for Multiple Characters**: Handles letters (A-Z), numbers (0-9), and special characters (punctuation marks)
- **Interactive CLI**: User-friendly command-line interface

## Requirements

- Python 3.x

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Run the program using Python

## Usage

Run the program:

```bash
python main.py
```

### Menu Options

- Enter `1` to encode text to Morse code
- Enter `2` to decode Morse code to text
- Enter `q` to quit the application

### Examples

**Encoding Text to Morse Code:**
```
Enter '1' to encode text to Morse, '2' to decode Morse to text, or 'q' to quit: 1
Enter text to encode: Hello World
Morse Code: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

**Decoding Morse Code to Text:**
```
Enter '1' to encode text to Morse, '2' to decode Morse to text, or 'q' to quit: 2
Enter Morse code to decode (use '/' for spaces): .... . .-.. .-.. --- / .-- --- .-. .-.. -..
Decoded Text: HELLO WORLD
```

## Morse Code Reference

### Letters
- A: .-    B: -...   C: -.-.
- D: -..   E: .      F: ..-.
- And so on...

### Numbers
- 0: -----  1: .----  2: ..---
- 3: ...--  4: ....-  5: .....
- And so on...

### Special Characters
- Space: / (forward slash)
- Period: .-.-.-
- Comma: --..--
- Question Mark: ..--..
- And more...

## How It Works

The program uses a dictionary to map characters to their Morse code equivalents:
- For encoding: Characters are converted to uppercase and mapped to Morse code
- For decoding: Morse code patterns are mapped back to characters
- Spaces between words are represented by forward slashes (/)

## Notes

- Unknown characters are replaced with `?`
- Text input is automatically converted to uppercase for encoding
- When entering Morse code for decoding, use spaces between letters and `/` for spaces between words

## License

This project is free to use for educational purposes.
