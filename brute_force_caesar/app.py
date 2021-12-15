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


key_range = range(0, 26)

if __name__ == "__main__":
    encrypted = input("Enter the text you want to decrypt:")
    print("Brute forcing with all possible keys.")
    for key in key_range:
        decrypted = encrypt(encrypted, -key)
        print(f"Trying key:{key}, \t got: {decrypted}")
