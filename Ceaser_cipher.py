#Task 1
#Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.

def caesar_cipher(text, shift, mode):
    shift = shift if mode == 1 else -shift
    return ''.join(chr((ord(c) - (65 if c.isupper() else 97) + shift) % 26 + (65 if c.isupper() else 97)) if c.isalpha() else c for c in text)
print(" >> Caesar Cipher <<")
print("1. Encrypt\n2. Decrypt")
mode = int(input("Enter 1 for Encrypt or 2 for Decrypt: "))
if mode in [1, 2]:
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    print(f"Result: {caesar_cipher(text, shift, mode)}")
else:
    print("Invalid choice!")