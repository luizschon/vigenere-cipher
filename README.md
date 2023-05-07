# Cifra de Vigenère

## Autores

- Bruno Fernandes Teixeira - 190097540
- Luiz Carlos Schonarth Junior - 190055171

# Exemplo codificação

Insira o texto a ser cifrado em `input.txt` e use o seguinte comando:

```bash
cat input.txt | python vigenere_cipher.py --key bane --encode
```

# Exemplo decodificação

Insira o texto a ser decifrado em `input.txt` e use o seguinte comando:

```bash
cat input.txt | python vigenere_cipher.py --key bane --decode
```

# Quebrando desafios

```bash
cat challenges/desafio1.txt | python vigenere_cracker.py -f frequencies/english.txt
cat challenges/desafio2.txt | python vigenere_cracker.py -f frequencies/portuguese.txt
```
