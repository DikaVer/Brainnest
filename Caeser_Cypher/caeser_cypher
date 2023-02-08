def encrypt_msg(key):
    encrypted_message = ""
    message = input("Enter the message to encrypt: ")
    for letter in message:
        if ord(letter) == 32:
            encrypted_message += " "
        else:
            new_ascii_letter = ord(letter) + key
            if new_ascii_letter > 122:
                new_ascii_letter = new_ascii_letter - 26
            encrypted_message += chr(new_ascii_letter)
    return encrypted_message


def decrypt_msg(key):
    decrypted_message = ""
    message = input("Enter the message to encrypt: ")
    for letter in message:
        if ord(letter) == 32:
            decrypted_message += " "
        else:
            new_ascii_letter = ord(letter) - key
            if new_ascii_letter < 97:
                new_ascii_letter = new_ascii_letter + 26
            decrypted_message += chr(new_ascii_letter)
    return decrypted_message


encrypt_question = input("Do you want to (e)ncrypt or (d)ecrypt?:")
key_password = int(input("Please enter the key (0 to 25) to use: "))
if encrypt_question == "e":
    print(encrypt_msg(key_password))

elif encrypt_question == "d":
    print(decrypt_msg(key_password))