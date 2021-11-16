def encrypt(text, alphabet, key):
    words = text.split(' ')
    new_text = str()
    for word in words:
        word = word.lower()
        for letter in word:
            index = alphabet.index(letter)
            new_letter = key[index]
            new_text += new_letter
        new_text += ' '
    return new_text


def decrypt(text, alphabet, key):
    return encrypt(text, key, alphabet)


def generateKey(secret):
    secret = secret.lower()
    secret_without_spaces = secret.replace(' ', '')
    secret_unique_letters = list(dict.fromkeys(secret_without_spaces))
    second_part = list(filter(
        lambda letter: letter not in secret_unique_letters, ALPHABET))
    return ''.join(secret_unique_letters + second_part)


SECRET = "բանալի"

ALPHABET = ['ա', 'բ', 'գ', 'դ', 'ե', 'զ', 'է', 'ը', 'թ', 'ժ',
            'ի', 'լ', 'խ', 'ծ', 'կ', 'հ', 'ձ', 'ղ', 'ճ', 'մ',
            'յ', 'ն', 'շ', 'ո', 'չ', 'պ', 'ջ', 'ռ', 'ս', 'վ',
            'տ', 'ր', 'ց', 'ո', 'ւ', 'փ', 'ք', 'և', 'օ', 'ֆ']

texts = ["Երևանի Պետական Բժշկական համալսարան", "Մատենադարան"]

KEY = generateKey(SECRET)
print("SECRET: ", SECRET)
print("KEY: ", KEY)

for text in texts:
    encrypted = encrypt(text, ALPHABET, KEY)
    decrypted = decrypt(encrypted, ALPHABET, KEY)

    print("Original: ", text)
    print("Encrypted: ", encrypted)
    print("Decrypted: ", decrypted, '\n')
