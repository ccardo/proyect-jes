##
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()


def main():

    tmp_encryption_key = input("\nInsert encryption key: ").lower()
    tmp_encryption_key = [i for i in tmp_encryption_key]

    with open("input.txt", "r") as file:
        lines = [line.strip().split() for line in file.readlines()]

    Mode = input("Encrypt or decrypt? ").lower().startswith("d")
    with open("output.txt", "w") as output:
        for line in lines:
            for word in line:
                output.write(crypt(tmp_encryption_key, word, decrypt=Mode) + " ")
            output.write("\n")


def clean_key(key):

    key = [i for i in key]
    encryption_key = ""
    for idx, letter in enumerate(key):
        if key.index(letter) == idx:
            encryption_key += letter
    return encryption_key


def encrypt_alphabet(key):
    key = clean_key(key)

    encrypted_alpha = [i for i in ALPHABET]
    encryption_key = []

    for letter in key:
        encrypted_alpha.remove(letter)
        encryption_key += letter
    encrypted_alpha = encrypted_alpha[::-1]

    return encryption_key + encrypted_alpha


def crypt(key, word, decrypt=False):
    global ALPHABET

    encrypt = True if decrypt is False else False
    new_alpha = encrypt_alphabet(key)

    crypted = ""
    for letter in word:
        if encrypt:
            if letter in ALPHABET:
                idx = ALPHABET.index(letter)
                crypted += new_alpha[idx]
        elif decrypt:
            if letter in new_alpha:
                idx = new_alpha.index(letter)
                crypted += ALPHABET[idx]

    return crypted

if __name__ == '__main__':
    main()
