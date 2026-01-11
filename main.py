morse_code = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',
    'E': '.',      'F': '..-.',   'G': '--.',    'H': '....',
    'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',    'P': '.--.',
    'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',
    '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',
    '8': '---..',  '9': '----.',

    ',': '--..--', '.': '.-.-.-', '?': '..--..', '\'': '.----.',
    '!': '-.-.--', '/': '-..-.',  '(': '-.--.',  ')': '-.--.-',
    '&': '.-...',  ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-','@': '.--.-.', ' ': '/'
}

def text_to_morse(text):
    """Convert plain text to Morse code."""
    morse_text = []
    for char in text.upper():
        if char in morse_code:
            morse_text.append(morse_code[char])
        else:
            morse_text.append('?')  # Unknown character
    return ' '.join(morse_text)

def morse_to_text(morse):
    """Convert Morse code to plain text."""
    reverse_morse_code = {v: k for k, v in morse_code.items()}
    words = morse.split(' / ')
    decoded_words = []
    for word in words:
        chars = word.split()
        decoded_chars = []
        for char in chars:
            if char in reverse_morse_code:
                decoded_chars.append(reverse_morse_code[char])
            else:
                decoded_chars.append('?')  # Unknown Morse code
        decoded_words.append(''.join(decoded_chars))
    return ' '.join(decoded_words)

if __name__ == "__main__":
    app_active = True
    while app_active:
        user_input = input("Enter '1' to encode text to Morse, '2' to decode Morse to text, or 'q' to quit: ")
        if user_input == '1':
            text = input("Enter text to encode: ")
            encoded = text_to_morse(text)
            print(f"Morse Code: {encoded}")
        elif user_input == '2':
            morse = input("Enter Morse code to decode (use '/' for spaces): ")
            decoded = morse_to_text(morse)
            print(f"Decoded Text: {decoded}")
        elif user_input.lower() == 'q':
            app_active = False
        else:
            print("Invalid input. Please try again.")
        