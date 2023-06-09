#! /usr/bin/env python3

"""
Trabalho 1 da disciplina Seguranca Computacional - CIC

Autores: Luiz Carlos Schonarth Junior
         Bruno Fernandes Teixeira

Universidade de Brasilia
"""

import sys, getopt 
from utils import ALPHABET, CHAR_IDX

MATRIX = [[ALPHABET[(i+j) % 26] for j in range(len(ALPHABET)) ] for i in range(len(ALPHABET))]

def vigenere_cipher(text: str, secret: str, should_encode: bool) -> str:
    res = ""
    i = 0
    secret = secret.lower()

    for text_char in text.lower():
        if text_char not in ALPHABET:
            res += text_char
            continue

        secret_idx = i % len(secret)
        secret_char = secret[secret_idx]
        i += 1

        x, y = CHAR_IDX[secret_char], CHAR_IDX[text_char]

        if should_encode:
            encoded_char = MATRIX[x][y]
            res += encoded_char
        else:
            decoded_char = ALPHABET[MATRIX[x].index(text_char)]
            res += decoded_char

    return res

def main():
    # Parse command line arguments
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "k:ed", ["key=", "encode", "decode"])
    except getopt.GetoptError as err:
        print(err, file=sys.stderr) 
        sys.exit(1)
    key = '';
    should_encode = True
    for o, a in opts:
        if o in ('-k', '--key'):
            key = a
        elif o in ('-e', '--encode'):
            should_encode = True
        elif o in ('-d', '--decode'):
            should_encode = False
        else:
            print("ERROR: Unhadled option.", file=sys.stderr)
            sys.exit(1)

    if not key:
        key = input("Key: ")

    if not key.isalpha():
        print("ERROR: Key must be alphabetical.", file=sys.stderr)
        sys.exit(1)

    text = sys.stdin.read()
    sys.stdout.write(vigenere_cipher(text, key, should_encode))

if __name__ == "__main__":
    main()
