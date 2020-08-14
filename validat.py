import random
import hashlib


def validate_key(key):

    key_found = False
    for n in range(11, 66, 11):
        bytes_list = bytearray(b'\x01\x02\x03')
        bytes_list.append(n)
        decoded_key = hashlib.sha256(bytes_list).hexdigest()
        if key == decoded_key:
            key_found = True
            break

    if key_found:
        return True
    else:
        return False


user_input = input("please enter the key : ")
print(validate_key(user_input))
