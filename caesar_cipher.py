def encrypt(message, key):
    encrypt = ''
    for letter in message.lower():
        if ord(letter) == 32:
            encrypt += " "
        else:
            if ord(letter) + key > ord('z'):
                encrypt += chr(ord(letter) + key - 26)
            else:
                encrypt += chr(ord(letter) + key)
    return encrypt.upper()


def decrypt(message, key):
    encrypt = ''
    for letter in message.lower():
        if ord(letter) == 32:
            encrypt += " "
        else:
            if ord(letter) - key < ord('a'):
                encrypt += chr(ord(letter) - key + 26)
            else:
                encrypt += chr(ord(letter) - key)

    return encrypt.upper()

print(encrypt('MEET ME BY THE ROSE BUSHES TONIGHT', 4))
print(decrypt('QIIX QI FC XLI VSWI FYWLIW XSRMKLX', 4))
