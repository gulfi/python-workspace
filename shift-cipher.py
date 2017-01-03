"!/usr/local/bin/python3.5"

alpha="abcdefghijklmnopqrstuvwxyz"

def encrypt(s, shift=2):
    encrypted_str = ""
    for cipher in s:
        index = alpha.index(cipher)
        shifted_index = (index + shift) % len(alpha)
        encrypted_str += alpha[shifted_index]
    return encrypted_str

print(encrypt("Gulshan"))
