def encrypt_caesar(message, shift):

    if shift <= 0:
        raise ValueError("Number should be greater than 0")

    res = []

    for char in message:

        if char.isalpha():

            new_char = ""

            if char.isupper():
                new_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))

            elif char.islower():
                new_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))

            res.append(new_char)

        else:
            res.append(char)

    return "".join(res)


def decrypt_caesar(message, shift):

    if shift <= 0:
        raise ValueError("Number should be greater than 0")

    res = []

    for char in message:

        if char.isalpha():

            new_char = ""

            if char.isupper():
                new_char = chr((ord(char) - ord("A") - shift) % 26 + ord("A"))

            elif char.islower():
                new_char = chr((ord(char) - ord("a") - shift) % 26 + ord("a"))

            res.append(new_char)

        else:
            res.append(char)

    return "".join(res)
