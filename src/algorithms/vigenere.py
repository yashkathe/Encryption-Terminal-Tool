def generate_key(text, key):

    if len(text) == len(key):
        return key

    else:

        key = key.lower()
        new_key = ""
        key_index = 0

        for i in range(len(text)):

            if text[i].isalpha():
                new_key += key[key_index % len(key)]
                key_index += 1
            else:
                new_key += text[i]

        return new_key


def encrypt_vigenere(text, key):

    new_key = generate_key(text, key)

    res = []

    for t_char, k_char in zip(text, new_key):

        if t_char.isalpha():

            base = ord("a") if t_char.islower() else ord("A")
            new_char = chr((ord(t_char) - base + ord(k_char) - ord("a")) % 26 + base)

            res.append(new_char)

        else:
            res.append(t_char)

    return "".join(res)


def decrypt_vigenere(text, key):

    new_key = generate_key(text, key)

    res = []

    for t_char, k_char in zip(text, new_key):

        if t_char.isalpha():

            base = ord("a") if t_char.islower() else ord("A")
            new_char = chr((ord(t_char) - base - (ord(k_char) - ord("a"))) % 26 + base)

            res.append(new_char)

        else:
            res.append(t_char)

    return "".join(res)
