import argparse

from src.algorithms.caesar import decrypt_caesar, encrypt_caesar

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--algorithm", type=str)
    parser.add_argument("--text", type=str)
    parser.add_argument("--shift", type=int)
    parser.add_argument("--encrypt", action="store_true")
    parser.add_argument("--decrypt", action="store_true")

    args = parser.parse_args()

    # Caesar
    if args.algorithm == "caesar" and args.text and args.shift:

        if args.encrypt:
            print(encrypt_caesar(args.text, args.shift))

        elif args.decrypt:
            print(decrypt_caesar(args.text, args.shift))
