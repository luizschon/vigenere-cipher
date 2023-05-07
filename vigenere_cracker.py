#! /usr/bin/env python3

"""
Trabalho 1 da disciplina Seguranca Computacional - CIC

Autores: Luiz Carlos Schonarth Junior
         Bruno Fernandes Teixeira

Universidade de Brasilia
"""

import sys, getopt 
from typing import List
from math import sqrt
from vigenere_cipher import vigenere_cipher 
from utils import ALPHABET, CHAR_IDX


def index_of_coincidence(sequence: str="", frequencies: list=[]):
    sum = 0
    if frequencies:
        for f in frequencies:
            sum += f*f

        return sum

    counts = [0 for _ in range(len(ALPHABET))]
    for char in sequence.lower():
        counts[CHAR_IDX[char]] += 1

    seq_len = len(sequence)
    for n in counts:
        sum += n * (n-1)

    return sum/(seq_len * (seq_len-1))


def cosangle(vec1: List[float], vec2: List[float]) -> float:
    numerator = 0   
    lengthx2 = 0    
    lengthy2 = 0    
    for i in range(len(vec1)):        
        numerator += vec1[i]*vec2[i]
        lengthx2 += vec1[i]*vec1[i]
        lengthy2 += vec2[i]*vec2[i]

    return numerator / sqrt(lengthx2*lengthy2)


def get_key(ciphertext: str, freq_file: str) -> str:
    lines = []
    with open(freq_file, 'r') as file:
        lines = file.readlines()

    if not lines:
        print('file empty')
        sys.exit(1)

    freq_histogram = [float(v) for v in lines] 
    expected_ioc = index_of_coincidence(frequencies=freq_histogram)

    found = False
    key_len = 0
    THRESHOLD = 0.007
    ciphertext = ''.join([c for c in ciphertext if c in CHAR_IDX])

    slices = []

    while not found:
        key_len += 1
        slices = ['' for _ in range(key_len)]
        for i in range(len(ciphertext)):
            slices[i % key_len] += ciphertext[i]

        avg_ioc = 0
        for slice in slices:
            avg_ioc += index_of_coincidence(sequence=slice)
        avg_ioc = avg_ioc / key_len

        if avg_ioc >= expected_ioc - THRESHOLD:
            found = True

    frequencies = []
    for i in range(key_len):   
        frequencies.append([0] * 26)
        for c in slices[i]:        
            frequencies[i][CHAR_IDX[c]] += 1   
        for n in frequencies[i]:        
            n /= len(slices[i])

    key = ""
    for freq in frequencies:
        for i in range(len(ALPHABET)):
            histogram = freq[i:] + freq[:i]
            if cosangle(freq_histogram, histogram) > 0.90:
                key += ALPHABET[i]

    return key


def main():
    # Parse command line arguments
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "f:m:", ["freq-file=", "method="])
    except getopt.GetoptError as err:
        print(err, file=sys.stderr) 
        sys.exit(1)
        
    freq_file = ""
    for o, a in opts:
        if o in ('-f', '--freq-file'):
            freq_file = a
        else:
            print("ERROR: Unhadled option.", file=sys.stderr)
            sys.exit(1)

    text = sys.stdin.read()
    
    key = get_key(text, freq_file)
    print(f"key:", key)

    res = vigenere_cipher(text, key, False)
    print(res)

if __name__ == "__main__":
    main()
