import random
import hashlib


def generate_key():
    random_num = random.randint(0, 4)
    randoms_nums = [11, 22, 33, 44, 55]
    bytes_list = bytearray(b'\x01\x02\x03')

    bytes_list.append(randoms_nums[random_num])

    return hashlib.sha256(bytes_list).hexdigest()


print(generate_key())
