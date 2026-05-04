# Assignment: AES Encryption and Decryption
# Aim: To implement AES encryption and decryption

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# 16-byte secret key
key = b"ABCDEFGHIJKLMNOP"

# Create AES cipher in ECB mode
cipher = AES.new(key, AES.MODE_ECB)

# Input plaintext
plaintext = input("Enter Plain Text: ").encode()

# Padding plaintext to multiple of 16 bytes
padded_text = pad(plaintext, 16)

# Encryption
encrypted_text = cipher.encrypt(padded_text)

# Display encrypted text
print("Encrypted Text:", encrypted_text)

# Decryption
decrypted_padded = cipher.decrypt(encrypted_text)

# Remove padding
decrypted_text = unpad(decrypted_padded, 16)

# Display decrypted text
print("Decrypted Text:", decrypted_text.decode())