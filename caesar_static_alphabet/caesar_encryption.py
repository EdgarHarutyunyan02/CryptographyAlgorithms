def encrypt(text, key):
    text = text.lower()
    new_text = str()
    for letter in text:
        index = (ALPHABET.index(letter)+key) % len(ALPHABET)
        new_letter = ALPHABET[index]
        new_text += new_letter
    return new_text


def decrypt(text, key):
    return encrypt(text, -key)


secret = 15

ALPHABET = ['ա', 'բ', 'գ', 'դ', 'ե', 'զ', 'է', 'ը', 'թ', 'ժ',
            'ի', 'լ', 'խ', 'ծ', 'կ', 'հ', 'ձ', 'ղ', 'ճ', 'մ',
            'յ', 'ն', 'շ', 'ո', 'չ', 'պ', 'ջ', 'ռ', 'ս', 'վ',
            'տ', 'ր', 'ց', 'ո', 'ւ', 'փ', 'ք', 'և', 'օ', 'ֆ']

texts = ["դեսպանատուն", "համակարգիչ", "հայաստան"]

print("Caesar encrypion using key:", secret, "\n")
for text in texts:
    encrypted = encrypt(text, secret)
    decrypted = decrypt(encrypted, secret)

    print("Original: ", text)
    print("Encrypted: ", encrypted)
    print("Decrypted: ", decrypted, '\n')
