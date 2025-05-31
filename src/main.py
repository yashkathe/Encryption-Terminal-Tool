import argparse

from src.algorithms.caesar import decrypt_caesar, encrypt_caesar
from src.algorithms.vigenere import decrypt_vigenere, encrypt_vigenere

# ArgParse setup
parser = argparse.ArgumentParser()

parser.add_argument("--algorithm", choices=["caesar", "vigenere"], required=True)
parser.add_argument("--text", type=str)
parser.add_argument("--shift", type=int)
parser.add_argument("--key", type=str)
parser.add_argument(
    "--mode", choices=["encrypt", "decrypt", "decrypt-force"], required=True
)

args = parser.parse_args()


if __name__ == "__main__":

    ## Algorithm Selection
    # Caesar
    if args.algorithm == "caesar":
        if args.mode == "encrypt":
            print(encrypt_caesar(args.text, args.shift))

        elif args.mode == "decrypt":
            print(decrypt_caesar(args.text, args.shift))

        elif args.mode == "decrypt-force":
            for shift in range(1, 26):
                print(f"{shift} - {decrypt_caesar(args.text, shift)}")

    # Vigenere
    if args.algorithm == "vigenere":
        if args.mode == "encrypt":
            print(encrypt_vigenere(args.text, args.key))

        elif args.mode == "decrypt":
            print(decrypt_vigenere(args.text, args.key))
