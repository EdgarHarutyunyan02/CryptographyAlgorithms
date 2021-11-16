def encrypt(text, key):
    new_text = str()
    for char in text:
        new_sumbol = ''
        if(char == " "):
            new_sumbol = " "
        elif (char.isupper()):
            new_sumbol += chr((ord(char) + key-65) % 26 + 65)
        else:
            new_sumbol += chr((ord(char) + key - 97) % 26 + 97)
        new_text += new_sumbol
    return new_text


def getNumeric(keyString):
    key_num = str()
    for char in keyString:
        key_num += str(ord(char))
    return int(key_num)


if __name__ == "__main__":
    user_text = input("Enter the text you want to encrypt:")
    key = int(input("Enter the key to encrypt with:"))
    encrypted = encrypt(user_text, key)
    decrypted = encrypt(encrypted, -key)

    print("Key: ", key)
    print("Original: ", user_text)
    print("Encrypted: ", encrypted)
    print("Decrypted: ", decrypted, '\n')
