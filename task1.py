def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            # Determine base (uppercase or lowercase)
            base = ord('A') if char.isupper() else ord('a')
            
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            # Keep spaces and special characters unchanged
            result += char

    return result

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
choice = input("Type 'encrypt' or 'decrypt': ").lower()

output = caesar_cipher(message, shift, choice)

print(f"Result: {output}")
