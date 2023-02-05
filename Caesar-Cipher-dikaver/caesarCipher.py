def encrypt(msg, num):
    msg = msg.upper()
    new_msg = ''
    for i in range(0, len(msg)):
        ascii_num = ord(msg[i])
        if 65 <= ascii_num <= 90:
            ascii_num += num
            if ascii_num > 90:
                ascii_num -= 26
            new_msg += chr(ascii_num)
        else:
            new_msg += msg[i]
    return new_msg

def decrypt(msg, num):
    msg = msg.upper()
    new_msg = ''
    for i in range(0, len(msg)):
        ascii_num = ord(msg[i])
        if 65 <= ascii_num <= 90:
            ascii_num -= num
            if ascii_num < 65:
                ascii_num += 26
            new_msg += chr(ascii_num)
        else:
            new_msg += msg[i]
    return new_msg



def get_input():
    print("Please enter the key (0 to 25) to use.")
    num_input = input("> ")
    num_input = int(num_input)
    if 0 <= num_input <= 25:
        return num_input
    else:
        raise Exception("Wrong input!")


print("Do you want to (e)ncrypt or (d)ecrypt?")
user_input = input("> ")

try:
    if user_input == "e":
        num_input = get_input()
        print("Enter the message to encrypt.")
        message = input("> ")
        print(encrypt(message, num_input))
    elif user_input == "d":
        num_input = get_input()
        print("Enter the message to encrypt.")
        message = input("> ")
        print(decrypt(message, num_input))
    else:
        print("Wrong input!")
except Exception as e:
    print(e)

