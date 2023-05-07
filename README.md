# cifra de vigenère


# exemplo codificação

```bash
cat input.txt | python vigenere_cipher.py -k bane -e
```

# exemplo decodificação

```bash
cat input.txt | python vigenere_cipher.py -k bane -d
```

# exemplo quebra

```bash
cat challenges/desafio2.txt | python vigenere_cracker.py -f frequencies/portuguese.txt
```
