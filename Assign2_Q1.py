# HIT 137 Software Now 

# Assignment 2

# Group: CAS/DAN 21
# Abu Saeed Md Shafiqur Rahman (Shafiq Rahman) - S386795
# Annafi Bin Alam (Rafin Alam) - S387086
# Neville James Doyle (Nev Doyle) - S371207
# Yuvraj Singh (Yuvraj Singh) - S383324

# GitHub Repository: https://github.com/shafiqsaeed/HIT137-G21-Assign2

# Submitted: 17 January 2025


# Question 1 - Simple encryption/ decryption 
# This program encrypts file contents using rules and user shift key input 
# and writes the encrypted text to a new file. It also can decrypt 
# the content and check the correctness of decrypted text.


import string


def encrypt_text(input_file, output_file, n, m):
    
    # Encrypts the content of the input file and writes to the output file.
    # Prints the encrypted content on the console.
    
    def encrypt_char(char):
        if char in string.ascii_lowercase:  # Lowercase letters
            if char <= 'm':
                return chr((ord(char) - ord('a') + n * m) % 26 + ord('a'))
            else:
                return chr((ord(char) - ord('a') - (n + m)) % 26 + ord('a'))
        elif char in string.ascii_uppercase:  # Uppercase letters
            if char <= 'M':
                return chr((ord(char) - ord('A') - n) % 26 + ord('A'))
            else:
                return chr((ord(char) - ord('A') + m**2) % 26 + ord('A'))
        else:  # Special characters and numbers
            return char

    with open(input_file, 'r') as infile:
        raw_text = infile.read()
        encrypted_text = ''.join(encrypt_char(c) for c in raw_text)

    with open(output_file, 'w') as outfile:
        outfile.write(encrypted_text)

    # Print encrypted text to the console
    print("Encrypted Text:")
    print(encrypted_text)


def decrypt_text(encrypted_text, n, m):
    
    # Decrypts the given encrypted text and prints the result on the console.
    
    def decrypt_char(char):
        if char in string.ascii_lowercase:  # Lowercase letters
            if char <= 'm':
                return chr((ord(char) - ord('a') - n * m) % 26 + ord('a'))
            else:
                return chr((ord(char) - ord('a') + (n + m)) % 26 + ord('a'))
        elif char in string.ascii_uppercase:  # Uppercase letters
            if char <= 'M':
                return chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            else:
                return chr((ord(char) - ord('A') - m**2) % 26 + ord('A'))
        else:  # Special characters and numbers
            return char

    decrypted_text = ''.join(decrypt_char(c) for c in encrypted_text)

    # Print decrypted text to the console
    print("\nDecrypted Text:")
    print(decrypted_text)

    return decrypted_text


def check_correctness(raw_text, decrypted_text):
    
    # Compares the raw text with the decrypted text and prints the result to the console.
    
    if raw_text == decrypted_text:
        print("\nCorrectness Check: The decrypted text matches the original.")
    else:
        print("\nCorrectness Check: The decrypted text does NOT match the original.")


# Main program
def main():
    raw_file = "raw_text.txt"
    encrypted_file = "encrypted_text.txt"

    # Take user inputs for n and m
    n = int(input("Enter the value of n: "))
    m = int(input("Enter the value of m: "))

    # Encrypt the content of raw_text.txt
    encrypt_text(raw_file, encrypted_file, n, m)

    # Read the encrypted text from the file
    with open(encrypted_file, 'r') as infile:
        encrypted_text = infile.read()

    # Read the raw text from the file
    with open(raw_file, 'r') as infile:
        raw_text = infile.read()

    # Decrypt the encrypted text and print it on the console
    decrypted_text = decrypt_text(encrypted_text, n, m)

    # Check correctness of the decryption and display the result
    check_correctness(raw_text, decrypted_text)


main()
