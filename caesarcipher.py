import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    result = []
    for char in s:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            rotated = (ord(char) - ascii_offset + k) % 26
            result.append(chr(rotated + ascii_offset))
        else:
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    s = "middle-Outz"
    k = 2
    encrypted = caesarCipher(s, k)
    print(f"Original: {s}")
    print(f"Encrypted: {encrypted}")
