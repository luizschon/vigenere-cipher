# Cifra de Vigenère

## Autores

- Bruno Fernandes Teixeira - 190097540
- Luiz Carlos Schonarth Junior - 190055171

# Exemplo codificação

```bash
cat input.txt | python vigenere_cipher.py -k bane -e
```

# Exemplo decodificação

```bash
cat input.txt | python vigenere_cipher.py -k bane -d
```

# Exemplo quebra

```bash
cat challenges/desafio2.txt | python vigenere_cracker.py -f frequencies/portuguese.txt
```
