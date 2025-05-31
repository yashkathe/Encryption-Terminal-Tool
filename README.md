# Encryption Terminal Tool

A lightweight terminal-based tool to encrypt, decrypt, and crack messages using various encryption algorithms.

Features

- Encrypt and decrypt messages using:

  - Caesar Cipher
  - Vigenère Cipher
  - AES (symmetric key)
  - RSA (asymmetric key)
  - Base64 / ROT13

- "Crack Mode" to try decrypting a message with all supported algorithms

- Simple command-line interface

## Algorithms

- --algorithm
  - --caesar
  - --vigenere

### Caesar Cipher

- Flags
  - --mode
    - encrypt
    - decrypt
    - decrypt-force
  - --text
  - --shift

### Vigenère Cipher

- Flags
  - --mode
    - encrypt
    - decrypt
  - --text
  - --key
