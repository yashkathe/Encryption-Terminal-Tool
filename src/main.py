import argparse

from src.algorithms.caesar import decrypt_caesar, encrypt_caesar

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--algorithm", choices=["caesar"], required=True)
    parser.add_argument("--text", type=str)
    parser.add_argument("--shift", type=int)
    parser.add_argument(
        "--mode", choices=["encryt", "decrypt", "decrypt-force"], required=True
    )

    args = parser.parse_args()

    # Caesar
    if args.algorithm == "caesar":
        print(args.mode)
        if args.mode == "encrypt":
            print(encrypt_caesar(args.text, args.shift))

        elif args.mode == "decrypt":
            print(decrypt_caesar(args.text, args.shift))

        elif args.mode == "decrypt-force":
            for shift in range(1, 26):
                print(f"{shift} - {decrypt_caesar(args.text, shift)}")
